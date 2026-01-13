# A dictionary is a data structure used to store data values in key-value pairs.
# Values in a dictionary can be of any data type
# Keys must be strings
# A dictionary is an ordered collection (as from version 3.17) which is changeable/mutable.
# Keys must be unique. Duplicate keys will overwrite the previous value.
from pprint import pprint

empty_dict = {}

# You can create a dictionary using the dictionary literal (curly brackets)
student_a = {
    "first_name": "Chris",
    "last_name": "Idakwo",
    "age": 20,
    "height": 1.65,
    "gender": "Male",
    "registered": True,
    "skills": [],
}

# You can create a dictionary using the dict() constructor
student_b = dict(
    first_name = "Chris",
    last_name = "Idakwo",
    age = 20,
    height = 20,
    gender = "Male"
)

print("="*50)
pprint(student_a)
print("="*50)
pprint(student_b)
