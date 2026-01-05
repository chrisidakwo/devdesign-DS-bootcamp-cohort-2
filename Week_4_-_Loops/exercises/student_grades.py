# Ask the teacher for the number of students
# For each student:
#  Ask for the student's name
#  Ask for their test score
# Check if each score is valid (between 0 and 100)
# Calculate the average of all scores
# Tell the teacher:
#  Who passed (score >= 60)
#  Who failed (score < 60)
#  The class average
#  The highest and lowest scores

print("")
print("")
print("=================================================")
print("""
    Student Grades Tracker Project
    Author: Ekojoka Chris Idakwo
    Description: A program that tracks student grades, calculates class average, and identifies who passed or failed.
""")
print("=================================================")
print("")

# Step 1: Ask how many students
num_students = int(input("How many student do you want to grade? "))

# Initialize all necessary variables for calculations
total_score = 0
passed_students = []
failed_students = []

for num in range(num_students):
    print(f"\n--- Student {num + 1} ---")

    # Get the student name
    student_name = input("Enter student name: ")

    # Get and validate test score
    student_score = float(input(f"Enter score for {student_name}: "))

    while student_score < 0 or student_score > 100:
        print("Invalid score! Please enter a score between 0 and 100")
        student_score = float(input(f"Enter score for {student_name}: "))

    # Add to the total for calculation of average
    total_score = total_score + student_score

    # Check if the student passed or failed
    if student_score >= 60:
        passed_students.append((student_name, student_score)) # tuple
    else:
        failed_students.append((student_name, student_score))

class_average = total_score / num_students

print("\n" + "=" * 50)
print("GRADE REPORT")
print("=" * 50)

print("\nSTUDENTS WHO PASSED:")
for student in passed_students:
    print(f"   - {student[0]}: {student[1]}")


print("\nSTUDENTS WHO FAILED:")
for student in failed_students:
    print(f"   - {student[0]}: {student[1]}")


print(f"\nCLASS AVERAGE: {class_average:.1f}")
print("=" * 50)