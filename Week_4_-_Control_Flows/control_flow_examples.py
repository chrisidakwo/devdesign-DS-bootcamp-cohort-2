print("")
print("=================================================")
print("Password Length Check")
print("=================================================")
print("")

password = input("Enter a password: ")

# # Rules:
# # At least one uppercase letter
# # At least one lowercase letter
# # 8 characters minimum

# TODO: Use loops to validate on special characters
# TODO: Use while loop


min_length = len(password) >= 8
has_uppercase = password.lower() != password
has_lowercase = password.upper() != password

print("Has ~ 8 characters", min_length)
print("Has uppercase", has_uppercase)
print("Has lowercase", has_lowercase)

if min_length and has_uppercase and has_lowercase:
    print("Welcome to Dev & Design!")
else:
    print("Your password is not secure enough!")


print("")
print("")
print("=================================================")
print("Grade Classification")
print("=================================================")
print("")

# Take a score and convert to a grade letter, ranging from A to F
# Where A is for scores between 85 and 100
# B is for scores between 70 and 85
# C is for scores between 55 and 70
# D is for scores between 45 and 55
# E is for scores between 30 and 45
# F is for scores below 30 (0 and 30)

score = input("Enter your score (0 to 100): ")

if score.isnumeric():
    score = int(score)

    # TODO: Write a check for when score is above 100
    
    # TODO: Handle decimal values (Lists)

    if score >= 85 and score <= 100:
        print("Grade is A")
    elif score >= 70 and score < 85:
        print("Grade is B")
    elif score >= 55 and score < 70:
        print("Grade is C")
    elif score >= 45 and score < 55:
        print("Grade is D")
    elif score >= 30 and score < 45:
        print("Grade is E")
    elif score >= 0 and score < 30:
        print("Grade is F")
else:
    print("Please enter a valid number between 0 and 100")
