import pandas as pd

from utils.students_record_utils import load_student_records

students_df = load_student_records("files/students_record.csv")

print("\n")
print(students_df.head(6))
print("\n")
print(students_df["math_score"])

# 1. Boolean Indexing (using [])
math_high_performers = students_df[students_df["math_score"] > 90] # Single condition/criteria
print(math_high_performers)


print("\n")
print("="*50)
print("\n")


# Filter for students who scored above 85 in Maths and 75 in Science - multiple conditions/criteria
science_high_performers = students_df[
    ((students_df["math_score"] > 85) & (students_df["science_score"] > 90))
]
print(science_high_performers)

print("\n")
print("="*50)
print("\n")

# Filter for students who excel in either Maths (above 90) or English (above 90)
math_or_english = students_df[
    (students_df["math_score"] > 90) |
    (students_df["english_score"] > 90)
]

print(math_or_english)

print("\n")
print("="*50)
print("\n")

# 2. Query Indexing (using SQL-Like Syntax)
results = students_df.query("math_score >= 80 and english_score > 90 and grade_level == 10")
print("Query Result")
print(results)

print("\n")
print("="*50)
print("\n")

# 3. filter() method - primarily used to filter rows or columns based on their labels (not content)
filtered_cols = students_df.filter(like="_score", axis=1)
# TODO: Filter across rows
print(filtered_cols)

print("\n")
print("="*50)
print("\n")

# 4. isin() method
# Take for example, we're looking for students with the last name "Hernandez"
filtered_students = students_df[students_df["last_name"].isin(["Hernandez", "Thomas", "Taylor"])]
print(filtered_students)

print("\n")
print("="*50)
print("\n")

# 5 .loc[] Accessor (label-based indexing) Label Location
filtered_df = students_df.loc[students_df["history_score"] > 80, ["student_id", "first_name", "history_score"]]
print(filtered_df)

# 6 .iloc[] Accessor (Integer-based indexing) Integer location
filtered_df = students_df.iloc[students_df["history_score"] > 80, [0, 1, 9]]
print(filtered_df)