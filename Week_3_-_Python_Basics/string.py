state = "Kaduna"

print(state)
print(type(state))


print("")
print("---------------------------------------------")
print("")

# Length of a string
print("******** String Length ********")
print("")
print("The length of the string 'Kaduna' is:", len(state))

country = "Nigeria"

print("")
print("---------------------------------------------")
print("")

# Transform to lower case
print("******** Lowercase ********")
print("")
print(country.lower())


print("")
print("---------------------------------------------")
print("")

# Transform to upper case
print("******** Uppercase ********")
print("")
print(country.upper())


print("")
print("---------------------------------------------")
print("")

# Transform to title case
event_name = "uefa champions league"

print("******** Titlecase ********")
print("")
print(event_name.title())

age = "9089"
print("Is 9089 numeric?", age.isnumeric())

print("")
print("---------------------------------------------")
print("")

# Conversions
print("******** Conversions ********")
# Int => Float
# Int => Float
# Int => Float

age = 45
print(type(age))
print(type(str(age)))

is_student = False
print("Is student?", float(is_student))


print('===========================')

# names = None
# print(float(names))

# text = "He8950llo"
# num = int(text)
# print(num)

# String slicing
sentence = "Chris Idakwo is in the class session which starts at 9am"
students = "David,Daniel,Sarah,Lola,Iniye,Irine"
# TODO: Talk about string split when looking at lists

# Index position by computing
# -1 less
greeting = "Hello, good morning"
print(greeting[:])
# ---> Format: string[start:end:step]

# Reversing a string using a negative step
print(greeting[::-1])



print("")
print("---------------------------------------------")
print("")

# Strip
print("******** Strip ********")

username = "  chris.idakwo@email.com  "
print("Username", username)

# lstrip() removes leading and trailing characters (on the both sides of the string)
print("Username", username.strip("  "))
print("-/user@gmail.com&-".strip("-&/"))

# lstrip() removes leading characters (on the left-hand side of the string)
print("Username", username.lstrip("  "))

#  rstrip() removes trailing characters (on the right-hand side of the string)
print("Username", username.rstrip("  "))


print("")
print("---------------------------------------------")
print("")

# String Concatenation
print("******** String Concatenation ********")

first_name = "John"
last_name = "Doe"
score = 80

full_name = first_name + " " + last_name
print("Full Name:", full_name)

# Print out: John Doe scored 80 out of 100
sentence = first_name + " " + last_name + " scored " + str(score) + " out of 100"
print(sentence)


# print("")
print("---------------------------------------------")
print("")

# String Formatting
print("******** String Formatting ********")
# F-String: Formatted string
sentence_f = f"{first_name} {last_name} scored {score} out of 100"
print(sentence_f)

sentence_fa = "{lname} {fname} scored {sc} out of 100 for this session!".format(
    fname=first_name, lname=last_name, sc=score
)
print(sentence_fa)

