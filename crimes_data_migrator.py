"""
Migrates the Chicago crime dataset from CSV to a MySQL database.
"""
import os
import sys
import logging

from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from tqdm import tqdm
import pandas as pd

import warnings
warnings.filterwarnings('ignore')

# -------------------------------------
# CONFIGURATION
# -------------------------------------

# Path to the CSV file (relative to this script)
CSV_FILE_PATH = "data/Chicago_Crimes_2001_to_Present.csv"

# Number of rows to insert per batch
# Increase for faster migration on powerful machines
# Decrease if you run into memory issues
CHUNK_SIZE = 20_000

# Name of the table to create in MySQL
TABLE_NAME = "incidents"

# Max rows to migrate per run (set to None for no limit)
BATCH_LIMIT = 3_000_000

CHECKPOINT_FILE  = "logs/migration_checkpoint.txt"

# -------------------------------------
# COLUMN RENAMING MAP
# -------------------------------------
# The CSV has column names with spaces and mixed casing.
# We rename them to clean, snake_case names suitable for a database.

COLUMN_RENAME_MAP = {
    "ID": "id",
    "Case Number": "case_number",
    "Date": "incident_date",
    "Block": "block",
    "IUCR": "iucr",
    "Primary Type": "primary_type",
    "Description": "description",
    "Location Description": "location_description",
    "Arrest": "arrest",
    "Domestic": "domestic",
    "Beat": "beat",
    "District": "district",
    "Ward": "ward",
    "Community Area": "community_area",
    "FBI Code": "fbi_code",
    "X Coordinate": "x_coordinate",
    "Y Coordinate": "y_coordinate",
    "Year": "year",
    "Updated On": "updated_on",
    "Latitude": "latitude",
    "Longitude": "longitude",
    "Location": "location",
}

# -------------------------------------
# MYSQL DATA TYPES
# -------------------------------------
# Explicitly define the MySQL column types for each field.
# This gives us proper data types in the database instead
# of letting pandas guess and defaulting everything to TEXT.

COLUMN_DTYPES = {
    "id": "BIGINT",
    "case_number": "VARCHAR(20)",
    "incident_date": "DATETIME",
    "block": "VARCHAR(100)",
    "iucr": "VARCHAR(10)",
    "primary_type": "VARCHAR(100)",
    "description": "VARCHAR(255)",
    "location_description": "VARCHAR(255)",
    "arrest": "BOOLEAN",
    "domestic": "BOOLEAN",
    "beat": "VARCHAR(10)",
    "district": "VARCHAR(10)",
    "ward": "VARCHAR(10)",
    "community_area": "VARCHAR(10)",
    "fbi_code": "VARCHAR(10)",
    "x_coordinate": "FLOAT",
    "y_coordinate": "FLOAT",
    "year": "SMALLINT",
    "updated_on": "DATETIME",
    "latitude": "DECIMAL(10, 7)",
    "longitude": "DECIMAL(10, 7)",
    "location": "VARCHAR(50)",
}

# ------------------------------------------------
# LOGGING SETUP
# ------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout), # Print to terminal
        logging.FileHandler("logs/csv_migration.log"), # Save to a log file
    ]
)

logger = logging.getLogger(__name__)

# -------------------------------------
# DATABASE CONNECTION
# -------------------------------------

def build_connection_string() -> str:
    """
    Build the SQLAlchemy connection string from environment variables.
    Credentials are never hardcoded — they come from the .env file.
    """
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT", "3306")
    db_name = os.getenv("DB_NAME")

    # Validate that all required variables are present
    missing = [key for (key, val) in {
        "DB_USER": user,
        "DB_PASSWORD": password,
        "DB_HOST": host,
        "DB_NAME": db_name
    }.items() if not val]

    if missing:
        logger.critical("Missing environment variables: {}. Please check your .env file".format(missing))

        raise EnvironmentError(
            f"Missing required environment variables: {', '.join(missing)}\n"
            f"Please check your .env file."
        )

    return f"mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}"

def create_db_engine():
    """
    Create and return a SQLAlchemy engine.
    Tests the connection before returning.
    """
    connection_string = build_connection_string()
    engine = create_engine(
        connection_string,
        pool_pre_ping=False,  # Checks connection health before using it
    )

    # Test the connection
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        logger.info("Database connection established successfully.")
    except Exception as e:
        logger.critical(f"Database connection failed!", exc_info=e)
        raise ConnectionError(f"Could not connect to the database: {e}")

    return engine

# -------------------------------------
# TABLE CREATION
# -------------------------------------

def create_table(engine, skip_if_exists: bool = False):
    """
    Create the incidents table in MySQL with proper column types.

    Args:
        engine: SQLAlchemy engine object.
        skip_if_exists (bool): If True, skip creation if the table already exists.
                                Used when resuming a checkpointed migration.
    """
    if skip_if_exists:
        logger.info(f"Resuming migration from the last checkpoint. Table '{TABLE_NAME}' already exists.")
        return

    column_definitions = ",\n    ".join(
        f"`{col}` {dtype}" for col, dtype in COLUMN_DTYPES.items()
    )

    # Did not use parameterized query because we had to inject `column_definitions`
    # which holds the SQL definitions of the columns for the table
    create_table_sql = f"""
        CREATE TABLE IF NOT EXISTS `{TABLE_NAME}` (
            {column_definitions},
            PRIMARY KEY (`id`),
            INDEX idx_primary_type (`primary_type`),
            INDEX idx_year (`year`),
            INDEX idx_district (`district`),
            INDEX idx_arrest (`arrest`),
            INDEX idx_domestic (`domestic`),
            INDEX idx_community_area (`community_area`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    """

    with engine.begin() as conn:
        logger.info(f"Creating table '{TABLE_NAME}'...")
        conn.execute(text(f"DROP TABLE IF EXISTS `{TABLE_NAME}`"))
        conn.execute(text(create_table_sql))
        logger.info(f"Table '{TABLE_NAME}' created successfully.")

# -------------------------------------
# DATA CLEANING
# -------------------------------------

def clean_chunk(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and prepare a single chunk of the CSV before inserting into MySQL.

    Steps:
        1. Rename columns to snake_case
        2. Parse date columns
        3. Convert boolean columns from True/False strings to 0/1
        4. Replace NaN values with None (MySQL-compatible nulls)
        5. Strip whitespace from string columns
    """
    # 1. Rename columns
    df = df.rename(columns=COLUMN_RENAME_MAP)

    # 2. Parse date columns — handle mixed date formats gracefully
    for date_col in ["incident_date", "updated_on"]:
        if date_col in df.columns:
            df[date_col] = pd.to_datetime(df[date_col], errors="coerce")

    # 3. Convert boolean columns
    for bool_col in ["arrest", "domestic"]:
        if bool_col in df.columns:
            df[bool_col] = df[bool_col].map(
                {
                    True: 1,
                    "true": 1,
                    "True": 1,
                    False: 0,
                    "false": 0,
                    "False": 0
                }
            )

    # 4. Strip whitespace from all string columns
    str_cols = df.select_dtypes(include="str").columns
    df[str_cols] = df[str_cols].apply(lambda col: col.str.strip())

    # 5. Replace NaN with None so MySQL gets proper NULLs
    df = df.where(pd.notnull(df), None)

    return df

# -------------------------------------
# MIGRATION
# -------------------------------------

def get_total_rows(filepath: str) -> int:
    """
    Count the total number of rows in the CSV for progress tracking.
    Reads only the row count without loading data into memory.
    """
    file = open(filepath, encoding="utf-8")

    logger.info("Counting total rows in CSV (this may take a moment)...")
    total = sum(1 for _ in file) - 1  # subtract header
    logger.info(f"Total rows to migrate: {total:,}")

    file.close()

    return total

def get_checkpoint() -> int:
    """
    Read the last saved row position from the checkpoint file.
    Returns 0 if no checkpoint exists (fresh migration).
    """
    if os.path.exists(CHECKPOINT_FILE):
        with open(CHECKPOINT_FILE, "r") as f:
            value = f.read().strip()
            if value.isdigit():
                return int(value)
    return 0


def save_checkpoint(total_rows_migrated: int):
    """
    Save the current total rows migrated to the checkpoint file.
    This is called after every successful chunk insert so that
    even a mid-run failure only loses at most one chunk.

    Args:
        total_rows_migrated (int): Total rows successfully inserted across all runs so far.
    """
    os.makedirs(os.path.dirname(CHECKPOINT_FILE), exist_ok=True)
    with open(CHECKPOINT_FILE, "w") as f:
        f.write(str(total_rows_migrated))

def migrate(engine):
    """
    Read the CSV in chunks and insert into MySQL in batches.
    Resumes from the last checkpoint if one exists.

    On each run, migrates up to BATCH_LIMIT rows then stops.
    Run the script again to continue from where it left off.
    The checkpoint file is updated after every successful chunk
    so a failure mid-run loses at most one chunk of rows.
    """
    if not os.path.exists(CSV_FILE_PATH):
        raise FileNotFoundError(
            f"CSV file not found at: {CSV_FILE_PATH}\n"
            f"Please place the CSV in the data/raw/ folder."
        )

    # Read checkpoint - how many rows have already been migrated?
    rows_already_done = get_checkpoint()
    is_resuming       = rows_already_done > 0

    if is_resuming:
        logger.info(f"Resuming from checkpoint: {rows_already_done:,} rows already migrated.")
        logger.info(f"Skipping first {rows_already_done:,} rows of CSV...")
    else:
        logger.info("No checkpoint found - starting fresh migration.")

    # Count remaining rows for progress bar
    total_csv_rows  = get_total_rows(CSV_FILE_PATH)
    remaining_rows  = total_csv_rows - rows_already_done

    if remaining_rows <= 0:
        logger.info("Checkpoint matches total CSV rows - migration already complete.")
        return 0, 0

    # Apply batch limit
    rows_to_migrate = remaining_rows
    if BATCH_LIMIT is not None:
        rows_to_migrate = min(remaining_rows, BATCH_LIMIT)
        logger.info(
            f"Batch limit: {BATCH_LIMIT:,} rows. "
            f"This run will migrate up to {rows_to_migrate:,} rows."
        )
        if remaining_rows > BATCH_LIMIT:
            logger.info(
                f"After this run, {remaining_rows - BATCH_LIMIT:,} rows "
                f"will remain. Run the script again to continue."
            )

    rows_this_run = 0
    rows_failed   = 0

    # skiprows skips rows 1..N (preserving the header at row 0)
    skip = range(1, rows_already_done + 1) if rows_already_done > 0 else None

    csv_reader = pd.read_csv(
        CSV_FILE_PATH,
        chunksize=CHUNK_SIZE,
        skiprows=skip,
        header=0,
        low_memory=False,
    )

    with tqdm(total=rows_to_migrate, unit="rows", desc="Migrating") as progress_bar:
        for chunk_number, chunk in enumerate(csv_reader, start=1):

            # Stop if we have hit the batch limit for this run
            if BATCH_LIMIT is not None and rows_this_run >= BATCH_LIMIT:
                break

            # Trim the last chunk if it would exceed the batch limit
            if BATCH_LIMIT is not None:
                remaining_budget = BATCH_LIMIT - rows_this_run
                if len(chunk) > remaining_budget:
                    chunk = chunk.iloc[:remaining_budget]

            try:
                cleaned_chunk = clean_chunk(chunk)

                cleaned_chunk.to_sql(
                    name=TABLE_NAME,
                    con=engine,
                    if_exists="append",
                    index=False,
                    method="multi",
                )

                rows_this_run += len(cleaned_chunk)

                # Save checkpoint after every successful chunk
                # so a crash only loses at most one chunk
                save_checkpoint(rows_already_done + rows_this_run)

                progress_bar.update(len(chunk))

            except Exception as e:
                rows_failed += len(chunk)
                logger.error(
                    f"Chunk {chunk_number} failed: {e}. "
                    f"Skipping {len(chunk):,} rows."
                )
                progress_bar.update(len(chunk))
                continue

    return rows_this_run, rows_failed

# -------------------------------------
# VERIFICATION
# -------------------------------------

def verify_migration(engine):
    """
    Run a few quick queries to verify the migration was successful.
    Prints a summary of what landed in the database.
    """
    logger.info("Verifying migration...")

    with engine.connect() as conn:
        # Total row count
        total = conn.execute(
            text(f"SELECT COUNT(*) FROM `{TABLE_NAME}`")
        ).scalar()

        # Year range
        year_range = conn.execute(
            text(f"SELECT MIN(year), MAX(year) FROM `{TABLE_NAME}`")
        ).fetchone()

        # Top 5 crime types
        top_crimes = conn.execute(text(f"""
            SELECT primary_type, COUNT(*) as count
            FROM `{TABLE_NAME}`
            GROUP BY primary_type
            ORDER BY count DESC
            LIMIT 5
        """)).fetchall()

        # Null check on key columns
        nulls = conn.execute(text(f"""
            SELECT
                SUM(CASE WHEN incident_date IS NULL THEN 1 ELSE 0 END) AS null_dates,
                SUM(CASE WHEN primary_type IS NULL THEN 1 ELSE 0 END) AS null_types,
                SUM(CASE WHEN district IS NULL THEN 1 ELSE 0 END)     AS null_districts
            FROM `{TABLE_NAME}`
        """)).fetchone()

        # Using the "IF" clause, instead of "CASE"
        # nulls = conn.execute(text(f"""
        #     SELECT
        #         SUM(IF(incident_date IS NULL, 1, 0)) AS null_dates,
        #         SUM(IF(primary_type IS NULL, 1, 0)) AS null_types,
        #         SUM(IF(district IS NULL, 1, 0))     AS null_districts
        #     FROM `{TABLE_NAME}`
        # """)).fetchone()

    print("\n" + "=" * 55)
    print("  MIGRATION VERIFICATION REPORT")
    print("=" * 55)
    print(f"  Total rows in database : {total:,}")
    print(f"  Year range             : {year_range[0]} — {year_range[1]}")
    print(f"\n  Top 5 Crime Types:")
    for crime_type, count in top_crimes:
        print(f"    {crime_type:<30} {count:>10,}")
    print(f"\n  Null Values in Key Columns:")
    print(f"    incident_date  : {nulls[0]:,}")
    print(f"    primary_type   : {nulls[1]:,}")
    print(f"    district       : {nulls[2]:,}")
    print("=" * 55 + "\n")


def main():
    """
    Entry point
    """
    print("\n" + "=" * 55)
    print("  CHICAGO CRIME DATASET - CSV TO MYSQL MIGRATION")
    print("=" * 55 + "\n")

    # Step 1: Load environment variables from .env
    load_dotenv()
    logger.info(".env file loaded!")

    # Step 2: Create the database engine
    engine = create_db_engine()

    # Step 3: Create the table with proper schema
    # Only create (and drop+recreate) the table on a fresh run.
    # If a checkpoint exists, the table is already populated -
    # skip creation and append to what is already there.
    rows_already_done = get_checkpoint()
    create_table(engine, skip_if_exists=(rows_already_done > 0))

    # Step 4: Run the migration
    (rows_inserted, rows_failed) = migrate(engine)

    # Step 5: Verify what landed in the database
    verify_migration(engine)

    # Step 6: Final summary
    logger.info(f"Run complete.")
    logger.info(f"  Rows inserted          : {rows_inserted:,}")
    logger.info(f"  Rows failed            : {rows_failed:,}")
    logger.info(f"  Total rows in DB       : {rows_already_done + rows_inserted:,}")

    # Step 7: Check if migration is fully complete
    total_csv_rows = get_total_rows(CSV_FILE_PATH)
    total_migrated = rows_already_done + rows_inserted
    if total_migrated >= total_csv_rows:
        logger.info("Migration fully complete. All rows migrated.")
        # Optionally delete the checkpoint file
        if os.path.exists(CHECKPOINT_FILE):
            os.remove(CHECKPOINT_FILE)
            logger.info("Checkpoint file removed.")
    else:
        remaining = total_csv_rows - total_migrated
        logger.info(
            f"-> {remaining:,} rows remaining. "
            f"Run the script again to continue."
        )

    if rows_failed > 0:
        logger.warning(
            f"{rows_failed:,} rows failed to insert. Check logs/migration.log for details."
        )

if __name__ == "__main__":
    main()


