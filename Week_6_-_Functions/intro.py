# Functions are named, reusable blocks of code that perform a specific task, helping to organize your program into smaller, more manageable parts. 
# Functions are state less
# Functions are first-class citizens in Python

# - Understand what functions are and why they're essential
# - Define and call functions with parameters
# - Variable scope
# - Use return values to get results from functions
# - Parameters and Arguments (Multiple Parameters, Positional vs Keyword Arguments)
# - Write functions with default parameters
# - Multiple return values (as lists, tuples, dictionaries)
# - Apply functions to solve data science problems
# - Organize code with reusable function libraries

# --------------------------------------------------------------
# Syntax of a function
# --------------------------------------------------------------
# def <name of function>:
#     function body (must be 1 to ~ number of lines)

print("\nHello, I'm above the function")

def test():
    print("\nHello, I'm inside the function")
    print("This is another line inside the function!")

# Call/Execute the function
test()

print("\nHello, I'm below the function")

# --------------------------------------------------------------
# FUNCTION WITH PARAMETERS
# When defining a function, the placeholder variables you place in-between the brackets are referred to as "parameters"
# --------------------------------------------------------------
def add(a, b):
    print(a + b)

# When you call a function, the values you pass in-between the brackets are referred to as "arguments"
add(20, 9) 
add(13, 48)
add(90, 14)


# --------------------------------------------------------------
# Functions are first-class citizens in Python
# --------------------------------------------------------------

# 1. A function being assigned to a variable
addition = add

# 2. Pass a function as an arugment to other functions
def operations(a, args):
    return a(*args)

operations(add, [12, 5])

# 3. Return a function from another function
def _operations():
    def addition(values):
        return sum(values)

    return addition

result = _operations()([12, 5])
print(result)

def calc():
    return "Calculation"

# 4. A function can be stored in a data structure (like lists, dictionaries)
student = {
    "name": "Chris Idakwo",
    "gender": "Male",
    "calculate_scores": calc,
}
