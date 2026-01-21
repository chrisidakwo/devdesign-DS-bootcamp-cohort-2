# What is Scope?
# Scope = Where can Python "see" your variable?

# 1. Global Scope (The Living Room)
# Variables created at the main level - everyone can see them

# This is GLOBAL - created outside any function, class, etc
customer_name = "Alice"

def greet():
    # Inside this function, we can see the global variable
    print(f"Hello, {customer_name}") 

greet() # Works! Prints: Hello, Alice
print(customer_name) # Works! Prints: Alice

# 2. Local Scope (The Bedroom)
# Variables created inside a function - only that function can see them

def calculate_tax():
    # The variable "tax_rate" is LOCAL - only exists inside this function
    tax_rate = 0.08
    return tax_rate * 100

print(calculate_tax()) # Works! Prints 8.0
try:
    print(tax_rate) # ERROR! Can't see tax_rate outside the "calculate_tax" function
except:
    print("Cannot see tax_rate outside the `calculate_tax` function")


# --------------------------------------------------------------
# READING GLOBAL VARIABLES - Works Fine
# --------------------------------------------------------------
discount_rate = 0.10

def calculate_discount(price):
    discount = price * discount_rate
    return discount

result = calculate_discount(800)

print(result)

# --------------------------------------------------------------
# REASSIGNING GLOBAL VARIABLES
# --------------------------------------------------------------

def calculate_total_a(price):
    discount_rate = 0.13 # re-assigned the value of discount_rate
    discount = price * discount_rate
    
    # Here the value of `discount_rate` has been temporarily re-assigned (within the function) to a new value
    # However, the initial value of the variable remains the same outside of the function
    print("What is discount rate?", discount_rate)

    return price - discount

# --------------------------------------------------------------
# MODIFYING GLOBAL VARIABLES
# --------------------------------------------------------------

def calculate_total_b(price):
    global discount_rate

    # Can't modify global variables in this manner (within a function)
    # Except in the case where the global keyword is used (just like above) to notify Python that the variable
    # should be referenced from the global scope
    # Any change/modification made to the value of the variable at this point will be reflected at the global scope 
    discount_rate = discount_rate + 0.0

    discount = price * discount_rate

    return price - discount

