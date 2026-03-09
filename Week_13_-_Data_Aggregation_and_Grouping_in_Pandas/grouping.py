from utils.students_record_utils import load_students

# groupby()
students_df = load_students("../data/students.csv")

students_df['Agriculture'].fillna(students_df['Agriculture'].mean(), inplace=True)

gender_students_df = students_df.copy()
gender_groups = gender_students_df.groupby("gender")

# Calculate average score across different subjects for each gender category/group
gender_performance = gender_groups[["Mathematics", "English Language", "Physics", "Computer Science", "Economics", "Agriculture"]].mean()

print("\n")

print(gender_performance)

print("\n")
print("="*50)
print("\n")

result = gender_groups["Mathematics"].agg(["mean", "count"])

print(result)

# Multiple aggregation at once
gender_stats = gender_groups["Further Mathematics"].agg(["min", "max", "mean", "count"])
print(gender_stats)

print("\n")
print("="*50)
print("\n")


# You can group by multiple columns
level_students_df = students_df.copy()

level_gender_groups = level_students_df.groupby(["class_level", "gender", "study_group", "daily_study_hours"]).mean()
level_gender_performance = level_gender_groups[["Mathematics", "English Language"]].mean()

print("================== LEVEL GENDER PERFORMANCE ==================")
print(level_gender_performance)

print("\n")