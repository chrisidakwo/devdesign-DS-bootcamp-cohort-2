import pandas as pd

def load_students(filename: str) -> pd.DataFrame:
    df = pd.read_csv(filename)

    class_level_map = {
        10: "SS1",
        11: "SS2",
        12: "SS3"
    }

    df["English Language"] = pd.to_numeric(df["English Language"], errors="coerce")
    df["Literature in English"] = pd.to_numeric(df["Literature in English"], errors="coerce")

    #  Replaces all values. Any value for the column that's not mapped in the dictionary key, is replace with NaN (meaning an empty value)
    # df["class_level"] = df["class_level"].map(class_level_map)

    # Only replaces matched values. Does not attempt to replace values not provided in the dictionary key.
    df["class_level"] = df["class_level"].replace(class_level_map)

    return df

def load_student_records(filename: str):
    df = pd.read_csv(filename)

    subject_cols = [col for col in df.columns.to_list() if "_score" in col]

    for col in subject_cols:
        # Fill missing values with either the mean of all values in the respective columns or the minimum value present in the column
        # df.fillna({ col: df[col].mean() }, inplace=True)
        df.fillna({ col: df[col].min() }, inplace=True)

        # Convert all numeric values to their respective data types of either float or integer
        df[col] = pd.to_numeric(df[col], errors="coerce")

    
    pd.to_numeric(df["attendance_rate"], errors="coerce")

    return df