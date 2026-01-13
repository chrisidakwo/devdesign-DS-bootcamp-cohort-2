from pprint import pprint

print("")
print("")
print("=================================================")
print("get() method -- Used to retrieve a dictionary item using the key name")
print("=================================================")
print("")

person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 50,
    "pets": { "dog": "Frieda", "cat": "Sox" },
    "kids": ["Joe", "Martha", "Sarah"]
}

# middle_name = person.get("middle_name")
# middle_name = person["middle_name"]

print("First Name (with get() method): ", person.get("first_name"))
print("First Name (without method): ", person["first_name"])

# Note that when using the get() method, if the key provided does not exist in the dictionary object,
# a value "None" will be returned. However, when using the square bracket, an error will be thrown

print("")
print("")
print("=================================================")
print("clear() method -- Deletes the dictionary content")
print("=================================================")
print("")

person_b = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 50,
    "pets": { "dog": "Frieda", "cat": "Sox" },
    "kids": ["Joe", "Martha", "Sarah"]
}

person_b.clear()
pprint(person_b)


print("")
print("")
print("=================================================")
print("copy() - Creates a shallow mirror/copy of the dictionary")
print("=================================================")
print("")

person_a = person.copy()
pprint(person_a)
print("")
pprint(person)


print("")
print("")
print("=================================================")
print("items() - Returns a list containing the content of the dictionary where each key-value pair is presented as a tuple")
print("=================================================")
print("")

pprint(person.items())


print("")
print("")
print("=================================================")
print("values() - Returns a list of all the values in the dictionary")
print("=================================================")
print("")

pprint(person.values())


print("")
print("")
print("=================================================")
print("keys() - Returns a list of all the keys in the dictionary")
print("=================================================")
print("")

pprint(person.keys())


print("")
print("")
print("=================================================")
print("pop() - Removes the element with the specified key and returns the value")
print("=================================================")
print("")

lastName = person.pop("last_name")
print("The last name is", lastName)
pprint(person["last_name"])
print("\n")