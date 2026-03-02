# The difference between the loc and iloc functions is that the loc function selects rows using row labels whereas the iloc function selects rows using their index position (starting from 0)

from utils.students_record_utils import load_student_records

students_df = load_student_records("files/students_record.csv")

students_df.set_index("grade_level", inplace=True)
print(students_df.loc["JSS2":"JSS3"])

print(students_df.iloc[0:4])