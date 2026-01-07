from pprint import pprint

car = dict(
    brand = "Ford",
    model = "Mustang",
    engineLitre = 5.0,
    transmission = "manual"
)

print("\n")

# You access values in a dictionary using a square bracket and the name of the key as a string within the brackets
trans = car["transmission"]
print("Car transmission is:", trans)

print("\n")


person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 50,
    "pets": { "dog": "Frieda", "cat": "Sox" },
    "kids": ["Joe", "Martha", "Sarah"]
}

print("What's the name of the 2nd child? ")

second_child = person["kids"][1]
print("Name of the 2nd child is:", second_child)

print("\n")
print("What is the name of his dog? ")

dog_name = person["pets"]["dog"]
print("Name of the dog is:", dog_name)




