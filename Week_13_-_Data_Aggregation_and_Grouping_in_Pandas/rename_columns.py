import pandas as pd
from utils.students_record_utils import load_students

students_df = load_students("../data/students.csv")

students_df.rename(
    columns={
        "Further Mathematics": "further_mathematics",
        "Civic Education": "civic_education",
        "Computer Science": "computer_science",
        "English Language": "english_language",
        "Literature in English": "literature_in_english",
    },
    inplace=True,
)

print(students_df[["student_id", "further_mathematics", "civic_education", "computer_science", "english_language"]])



# Further Mathematics,Civic Education,Computer Science,English Language,
# Literature in English