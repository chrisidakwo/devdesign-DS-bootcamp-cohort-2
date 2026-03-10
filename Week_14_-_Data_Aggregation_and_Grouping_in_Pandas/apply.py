import pandas as pd
from datetime import date, datetime

df = pd.read_csv("../data/students.csv")

def calc_age(dob):
    today = date.today()

    _dob = datetime.strptime(dob, "%Y-%m-%d").date()

    age = today.year - _dob.year

    return age

# 1 - Appying across single solumn

df["age"] = df["date_of_birth"].apply(calc_age)

print(df[["student_id", "first_name", "date_of_birth", "age"]].head(30))

# 2 - Applying across multiple columns
def find_best_students(row):
    avg = (row["Mathematics"] + row["English Language"]) / 2
    if avg >= 70:
        return "Amazing"
    else:
        return "Needs support"

df["status"] = df.apply(find_best_students, axis=1)


print(df[["student_id", "Mathematics", "English Language", "status"]].head(30))