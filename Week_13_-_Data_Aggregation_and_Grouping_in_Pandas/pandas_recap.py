import pandas as pd

# Load dataset (from a csv) into a pandas DataFrame
df = pd.read_csv("file path")

# Dataset preview
df.head()

# Select specific columns (using the subject columns in students_record.csv)
subjects = df[["history_score", "english_score", "math_score"]]