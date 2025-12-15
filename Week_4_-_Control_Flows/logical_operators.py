# Logical operators are used to combine or modify comparison operations

# "and" operator - all sides of the statement must be true, else it resolves to False
# all conditions must be true
age = 17
has_id = True

# TODO: Use input to take in data. Validate response for has_id to Yes or No.

if age >= 18 and has_id == True:
    print("Give access!")
else:
    print("No access!")


print("")
print("---------------------------------------------")
print("")


# "or" operator - only one side of the statement must be true for it to resolve as True
# at least one condition must be true
if age >= 18 or has_id == True:
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