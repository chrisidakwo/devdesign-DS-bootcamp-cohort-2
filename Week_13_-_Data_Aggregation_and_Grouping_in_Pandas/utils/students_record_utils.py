import pandas as pd

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