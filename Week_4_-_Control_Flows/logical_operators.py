# Logical operators are used to combine or modify comparison operations

# "and" operator - all sides of the statement must be true, else it resolves to False
# all conditions must be true
age = input("Enter your age: ")
has_id = input("Do you have an ID? (Enter 'Yes' or 'No') ")

if age.isnumeric() and (has_id.lower() is "yes" or has_id.lower() is "no"):
    # Validation on the age to ensure it's numeric, and validation on "has_id",
    # to ensure that it holds either "yes" or "no"

    if int(age) >= 18 and has_id == True:
        print("Give access!")
    else:
        print("No access!")
else:
    print("Invalid response!")


print("")
print("---------------------------------------------")
print("")


# "or" operator - only one side of the statement must be true for it to resolve as True
# at least one condition must be true
if int(age) >= 18 or has_id == True:
    print("Give access!")
else:
    print("No access")


print("")
print("---------------------------------------------")
print("")


# "not" operator - negates the result of an operation
# reverses a condition
print(not (5 == 5))

logged_in = False

if not logged_in:
    print("You're a guest")
else:
    print("Welcome back")


print("")
print("---------------------------------------------")
print("")

# Discount eligibility
age = 65
is_student = False

if age >= 60 or is_student:
    print("Yay, discount applied!")
else:
    print("Sorry, no discount for you! :(")