file_path = "../files/registrations.txt"

full_name = input("Enter your full name: ")
class_level = input("Enter your class level (SS1, SS2, SS3): ")
age = input("Enter your age: ")

with open(file_path, "a") as file:
    file.write(f"{full_name} | {age} | {class_level}" + "\n")