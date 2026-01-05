# A for loop repeats code a specific number of times. Not based on a condition.
# Starts and ends on its own, unlike the while loop

# Syntax of a for loop

# for item in iterable:
#     run this indented code block

name = "Chris Idakwo"
for char in name:
    print(char)

print("")
print("")
print("=================================================")
print("Loop through range of numbers")
print("=================================================")
print("")

for num in range(1, 6):
    print(num)

# TODO: Use break and continue statement