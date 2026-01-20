# Functions are named, reusable blocks of code that perform a specific task, helping to organize your program into smaller, more manageable parts. 
# Functions are state less

# - Understand what functions are and why they're essential
# - Define and call functions with parameters
# - Variable scope
# - Use return values to get results from functions
# - Write functions with default parameters
# - Apply functions to solve data science problems
# - Organize code with reusable function libraries

# Syntax of a function:

# def <name of function>:
#     function body (must be 1 to ~ number of lines)

print("\nHello, I'm above the function")

def test():
    print("\nHello, I'm inside the function")
    print("This is another line inside the function!")

# CALL/EXECUTE THE FUNCTION
test()

print("\nHello, I'm below the function")


def add(a, b): # When defining a function, the placeholder variables you place in-between the brackets are referred to as "parameters"
    print(a + b)
    tuple = (a, b)
    print(tuple)

# print(a)
# print(b)

# Variable Scope

add(20, 9) # When you call a function, the values you pass in-between the brackets are referred to as "arguments"
add(13, 48)
add(90, 14)