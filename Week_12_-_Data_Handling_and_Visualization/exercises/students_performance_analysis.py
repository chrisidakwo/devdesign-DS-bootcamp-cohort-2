from csv import DictReader
from pprint import pprint

def load_student_records(filename):
    """
    Load student data from CSV file
    """

    students = []

    try:
        with open(filename, "r") as file:
            reader = DictReader(file)
            
            for row in reader:
                # Convert numeric fields from strings to their appropriate types
                keys = list(row.keys())
                
                for key in keys:
                    # Handle empty/missing values
                    if "_score" in key and row[key] == "":
                        row[key] = 0
                    
                    if "_score" in key:
                        row[key] = float(row[key])

                # Convert grade level and age to integers
                if row["grade_level"] != "":
                    row["grade_level"] = int(row["grade_level"])

                if row["age"] != "":
                    row["age"] = int(row["age"])

                # Convert attendance_rate to float (and over 100%)
                if row["attendance_rate"] != "":
                    attendance_rate = float(row["attendance_rate"])
                    row["attendance_rate"] = attendance_rate * 100

                # Append row to students list
                students.append(row)
    except FileNotFoundError:
        print(f"Error: {filename} not found!")
        return []
    except Exception as e:
        print(f"Error loading data: {e}")
        return []

    return students


def calculate_student_average(student: dict):
    subject_fields = []

    for key in student.keys():
        if "_score" in key:
            subject_fields.append(key)

    # What is the total score? What is the count of subjects?
    total_score = 0
    count = len(subject_fields)

    for subject in subject_fields:
        total_score += student[subject]

    # Calculate average and return
    avg = total_score / count

    return round(avg, 2)


def assign_grade_letter(avg_score):
    if avg_score > 100:
        raise Exception("Average score cannot be greater than 100")

    if avg_score >= 90:
        return "A"
    elif avg_score >= 80:
        return "B"
    elif avg_score >= 70:
        return "C"
    elif avg_score >= 60:
        return "D"
    elif avg_score >= 50:
        return "E"
    else:
        return "F"
    

def find_top_performer_in_subject(students, subject_name):
    top_performer = {}
    top_score = -1 # Start with an impossible score

    for student in students:
        subject_score = student[subject_name]

        if subject_score > top_score:
            top_score = subject_score
            top_performer = student

    return {
        "student_id": top_performer["student_id"],
        "name": f"{top_performer["first_name"]} {top_performer["last_name"]}",
        "score": top_score,
        "subject": subject_name.replace("_score", "").title()
    }

# TODO: Create a variation of the `find_top_performer_in_subject()` 
# function above that returns a list of the top 3 performers in 
# each subject. Function should be named `find_top_performers_in_subject()`

def category_by_attendance(students):
    """
    Group students into attendance categories based on their attendance rate
    """

    categories = {
        "Excellent": {"count": 0, "total_score": 0, "students": []},
        "Good": {"count": 0, "total_score": 0, "students": []},
        "Fair": {"count": 0, "total_score": 0, "students": []},
        "Poor": {"count": 0, "total_score": 0, "students": []}
    }

    for student in students:
        attendance_rate = student["attendance_rate"]
        avg_score = student["average_score"]

        # Determine attendance category
        if attendance_rate >= 95:
            category = "Excellent"
        elif attendance_rate >= 90:
            category = "Good"
        elif attendance_rate >= 85:
            category = "Fair"
        else:
            category = "Poor"

        # Add to catetgory
        categories[category]["count"] += 1
        categories[category]["total_score"] += avg_score
        categories[category]["students"].append({
            "name": f"{student["first_name"]} {student["last_name"]}",
            "attendance_rate": attendance_rate,
            "average": avg_score
        })

    # Calculate averages for each category
    for category in categories:
        if categories[category]["count"] > 0:
            avg = categories[category]["total_score"] / categories[category]["count"]
            categories[category]["average_score"] = round(avg, 2)
        else:
            categories[category]["average_score"] = 0.0

    return categories


def calc_simple_correlation(students):
    """
    Calculates a simple correlation indicator between attendance and performance.

    This is a simplified correlation check.

    All we're doing is categorizing students by their attendance rate and seeing if
    higher attendance = higher scores
    """
    attendance_performance = category_by_attendance(students)

    # Extract average scores for each category
    category_order = ["Excellent", "Good", "Fair", "Poor"]

    averages = []
    for category in category_order:
        if attendance_performance[category]["count"] > 0:
            averages.append(attendance_performance[category]["average_score"])

    # Check if scores generally decrease as attendance decreases
    if len(averages) >= 2:
        # Simple check: is there a general downward trend?
        decreasing = True

        for i in range(len(averages) - 1):
            if averages[i] < averages[i + 1]:
                decreasing = False
                break

        correlation_strength = "STRONG POSITIVE" if decreasing else "WEAK/MIXED"
    else:
        correlation_strength = "INSUFFICIENT DATA"

    
    return {
        "strength": correlation_strength,
        "pattern": "Higher attendance correlates with higher performance" if decreasing else "Pattern unclear",
        "categories": attendance_performance
    }


def main():
    """Entry point"""
    students = load_student_records("../files/students_record.csv")

    for student in students:
        student_avg = calculate_student_average(student)
        student["average_score"] = student_avg
        student["grade_letter"] = assign_grade_letter(student_avg)

    correlation_result = calc_simple_correlation(students)
    print(correlation_result)


if __name__ == "__main__":
    main()