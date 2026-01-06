# 
# Without Loop Control
# 

# found = False

# for num in range(1, 1001):
#     guess = int(input("Guess the number: "))
#     if guess == 42:
#         found = True
#         print("Correct! You've found the number 42")

#     if not found:
#         print("Try again!")


# 
# With Loop Control
# 

for num in range(1, 1001):
    guess = int(input("Guess the number: "))
    if guess == 42:
        print("Correct! You've found the number 42")
        break # This ends/exits the parent loop completely
    
    print("Try again!")

# 
# Even numbers (up to 20)
# 
for num in range(1, 1001):
    if num > 20:
        break

    if num % 2 == 0:
        print(num)

