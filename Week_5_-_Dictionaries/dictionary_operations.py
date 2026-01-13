# Adding new entries to a dictionary
from pprint import pprint

person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 50,
    "pets": { "dog": "Frieda", "cat": "Sox" },
    "kids": ["Joe", "Martha", "Sarah"]
}

person["dob"] = "05/05/2025"

print("")

if "gender" in person:
    print("Found the key: gender")
else:
    print("Could not find the key!")

print("")
person["middle_name"] = "Dummy"

pprint(person)
