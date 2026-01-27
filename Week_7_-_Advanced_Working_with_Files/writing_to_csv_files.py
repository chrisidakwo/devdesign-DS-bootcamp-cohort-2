import csv
from pprint import pprint

# Sample data
dataset = [
    # ["Name", "Score", "Grade"]
    ["Alice", 92, "A"],
    ["Bob", 85, "B"],
    ["Mike", 73, "C"],
    ["Harrison", 97, "A"],
    ["Florence", 61, "D"]
]

def write_to_csv(list_data):
    # Assuming the headers were not defined
    headers = ["Name", "Score", "Grade"]
    __data = [headers] + list_data

    # Write to the a CSV file
    with open("files/students_grades.csv", "w", newline = '') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(__data)

    print("Done writing to `students_grades.csv`")


def write_to_csv_dict(list_data):
    students = []

    # {
    #     "name": "David",
    #     "score": 95,
    #     "grade": A
    # },

    for item in list_data:
        name = item[0]
        score = item[1]
        grade = item[2]

        students.append({
            "Name": name,
            "Score": score,
            "Grade": grade,
        })

    with open("files/students_grades_dict.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Score", "Grade"])
        writer.writeheader() # First write the header row
        writer.writerows(students) # Write all rows at once


write_to_csv(dataset)
write_to_csv_dict(dataset)
