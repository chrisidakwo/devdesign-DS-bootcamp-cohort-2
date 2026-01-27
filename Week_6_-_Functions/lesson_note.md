# Introduction to Functions in Python

## Week 5, Lesson 1

---

# Agenda

* Why Functions? The Problem They Solve
* Function Basics and Syntax
* Parameters and Arguments
* Return Values and Multiple Returns
* Functions for Data Analysis
* Organizing Code with Function Libraries
* Best Practices and Common Patterns
* Hands-On Exercises
* Mini-Project: Sales Analytics Library

---

# Brief Review: Where We Are

* Previous weeks: Variables, loops, conditionals, file handling
* Today: **Functions** - Reusable blocks of code
* Why now? Functions are essential for:
  * Organizing complex code
  * Building data analysis pipelines
  * Creating reusable tools
  * Preparing for pandas and libraries (next week)

---

# The Copy-Paste Problem

Without functions, analyzing multiple regions requires repetition:

```python
# North region analysis
north_total = 0
north_count = 0
north_sales = [1200, 850, 2100, 1450, 980]
for sale in north_sales:
    north_total += sale
    north_count += 1
north_average = north_total / north_count
print(f"North Average: ${north_average:.2f}")

# South region analysis (copy-pasted!)
south_total = 0
south_count = 0
south_sales = [1500, 920, 1800, 1100, 2200]
for sale in south_sales:
    south_total += sale
    south_count += 1
south_average = south_total / south_count
print(f"South Average: ${south_average:.2f}")

# ... and so on for East, West, etc.
```

**Problems:** Repetitive, error-prone, hard to maintain, doesn't scale

---

# The Function Solution

Write once, use everywhere:

```python
def calculate_average(sales_list):
    """Calculate average of sales values"""
    total = sum(sales_list)
    count = len(sales_list)
    average = total / count
    return average

# Now analyze all regions easily
north_sales = [1200, 850, 2100, 1450, 980]
south_sales = [1500, 920, 1800, 1100, 2200]
east_sales = [1100, 1300, 950, 1700, 1200]

print(f"North: ${calculate_average(north_sales):.2f}")
print(f"South: ${calculate_average(south_sales):.2f}")
print(f"East: ${calculate_average(east_sales):.2f}")
```

**Benefits:** DRY (Don't Repeat Yourself), maintainable, scalable, testable

---

# Anatomy of a Function

```python
def function_name(parameters):
    """
    Docstring: describes what the function does
    """
    # Function body - code that runs when function is called
    result = # do calculations or processing
    return result  # Send back the answer
```

**Key Parts:**
1. `def` keyword - defines a function
2. Function name - descriptive, uses verbs
3. Parameters - inputs in parentheses
4. Docstring - documentation (optional but recommended)
5. Function body - indented code block
6. `return` statement - sends back result

---

# Simple Function Examples

**No Parameters:**
```python
def greet_class():
    """Display a welcome message"""
    print("Welcome to Data Science Bootcamp!")
    print("Let's learn functions today!")

greet_class()  # Call the function
```

**One Parameter:**
```python
def greet_student(name):
    """Greet a student by name"""
    print(f"Hello, {name}! Ready to learn?")

greet_student("Alice")  # Hello, Alice! Ready to learn?
greet_student("Bob")    # Hello, Bob! Ready to learn?
```

**With Return Value:**
```python
def calculate_tax(price):
    """Calculate 8% sales tax"""
    tax = price * 0.08
    return tax

item_price = 100
tax_amount = calculate_tax(item_price)
print(f"Tax: ${tax_amount:.2f}")  # Tax: $8.00
```

---

# Multiple Parameters

Order matters with positional arguments:

```python
def calculate_total_price(price, quantity, tax_rate):
    """Calculate total price including tax"""
    subtotal = price * quantity
    tax = subtotal * tax_rate
    total = subtotal + tax
    return total

# Call with different values
total1 = calculate_total_price(10.99, 3, 0.08)
print(f"Total: ${total1:.2f}")  # Total: $35.60

total2 = calculate_total_price(25.50, 2, 0.10)
print(f"Total: ${total2:.2f}")  # Total: $56.10
```

**Parameters:**
* `price = 10.99` (first argument)
* `quantity = 3` (second argument)  
* `tax_rate = 0.08` (third argument)

---

# Positional vs Keyword Arguments

```python
def create_customer_profile(name, age, city, purchases):
    """Display customer profile"""
    print(f"Customer: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
    print(f"Purchases: {purchases}")

# Positional (order matters)
create_customer_profile("Alice", 28, "Lagos", 15)

# Keyword (order doesn't matter, more readable)
create_customer_profile(city="Abuja", name="Bob", purchases=8, age=35)

# Mix positional and keyword (positional must come first!)
create_customer_profile("Charlie", 42, city="Port Harcourt", purchases=22)
```

**Tip:** Use keyword arguments for clarity with many parameters

---

# Default Parameters

Provide default values for optional parameters:

```python
def calculate_discount(price, discount_rate=0.10):
    """Calculate discounted price (default 10% discount)"""
    discount = price * discount_rate
    final_price = price - discount
    return final_price

# Use default discount (10%)
price1 = calculate_discount(100)
print(f"With default: ${price1:.2f}")  # $90.00

# Use custom discount (25%)
price2 = calculate_discount(100, 0.25)
print(f"With 25% off: ${price2:.2f}")  # $75.00
```

**Use cases:**
* Tax rates (usually constant)
* Discount percentages (standard discount)
* Optional configuration settings

---

# Returning Different Data Types

Functions can return any Python data type:

```python
# Return a number
def calculate_bmi(weight_kg, height_m):
    """Calculate Body Mass Index"""
    return weight_kg / (height_m ** 2)

# Return a string
def get_bmi_category(bmi):
    """Categorize BMI"""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Return a boolean
def is_healthy_bmi(bmi):
    """Check if BMI is healthy"""
    return 18.5 <= bmi < 25

# Use them together
bmi = calculate_bmi(70, 1.75)
category = get_bmi_category(bmi)
healthy = is_healthy_bmi(bmi)
print(f"BMI: {bmi:.1f}, Category: {category}, Healthy: {healthy}")
```

---

# Returning Multiple Values

Return multiple values as a tuple:

```python
def analyze_sales_data(sales_list):
    """Calculate multiple statistics"""
    total = sum(sales_list)
    average = total / len(sales_list)
    highest = max(sales_list)
    lowest = min(sales_list)
    
    # Return multiple values
    return total, average, highest, lowest

# Unpack multiple return values
monthly_sales = [1200, 1500, 980, 2100, 1350]
total, avg, high, low = analyze_sales_data(monthly_sales)

print(f"Total: ${total:,.2f}")
print(f"Average: ${avg:,.2f}")
print(f"Highest: ${high:,.2f}")
print(f"Lowest: ${low:,.2f}")
```

---

# Returning Dictionaries (More Organized)

Better for complex return values:

```python
def get_sales_statistics(sales_list):
    """Return organized sales statistics"""
    stats = {
        "total": sum(sales_list),
        "average": sum(sales_list) / len(sales_list),
        "count": len(sales_list),
        "highest": max(sales_list),
        "lowest": min(sales_list),
        "range": max(sales_list) - min(sales_list)
    }
    return stats

# Get and use statistics
monthly_sales = [1200, 1500, 980, 2100, 1350]
results = get_sales_statistics(monthly_sales)

print(f"Total: ${results['total']:,.2f}")
print(f"Average: ${results['average']:,.2f}")
print(f"Range: ${results['range']:,.2f}")
```

**Benefits:** Clear labels, easy to extend, self-documenting

---

# Functions for Data Analysis: Customer Segmentation

```python
def segment_customer(total_purchases, avg_order_value):
    """
    Segment customers by purchase behavior
    
    Parameters:
        total_purchases (int): Number of purchases
        avg_order_value (float): Average spending per order
    
    Returns:
        str: Customer segment (VIP, Regular, Occasional)
    """
    if total_purchases >= 10 and avg_order_value >= 100:
        return "VIP"
    elif total_purchases >= 5 or avg_order_value >= 50:
        return "Regular"
    else:
        return "Occasional"

# Analyze customers
customers = [
    ("Alice", 15, 120),
    ("Bob", 3, 45),
    ("Charlie", 8, 75),
    ("Diana", 20, 200)
]

print("CUSTOMER SEGMENTATION:")
for name, purchases, avg_value in customers:
    segment = segment_customer(purchases, avg_value)
    print(f"{name:10} {purchases:2d} orders, ${avg_value:6.2f} → {segment}")
```

---

# Data Validation Function

```python
def validate_order_data(order_id, quantity, price):
    """
    Validate order data before processing
    
    Returns:
        tuple: (is_valid, error_message)
    """
    # Check order ID
    if not order_id or len(order_id) < 5:
        return False, "Invalid Order ID"
    
    # Check quantity
    if quantity <= 0:
        return False, "Quantity must be positive"
    
    # Check price
    if price <= 0:
        return False, "Price must be positive"
    
    # All checks passed
    return True, "Valid"

# Test validation
orders = [
    ("ORD-12345", 5, 99.99),
    ("ORD-", 3, 50.00),
    ("ORD-67890", -2, 75.00)
]

for order_id, qty, price in orders:
    is_valid, message = validate_order_data(order_id, qty, price)
    status = "✓" if is_valid else "✗"
    print(f"{status} {order_id}: {message}")
```

---

# Data Cleaning Function

```python
def clean_customer_name(name):
    """
    Clean and standardize customer names
    - Remove extra spaces
    - Capitalize properly
    - Remove special characters
    """
    # Remove leading/trailing spaces
    name = name.strip()
    
    # Remove extra spaces between words
    name = " ".join(name.split())
    
    # Capitalize each word
    name = name.title()
    
    # Remove numbers and special characters
    cleaned = ""
    for char in name:
        if char.isalpha() or char == " ":
            cleaned += char
    
    return cleaned

# Test with messy names
messy_names = [
    "  alice   johnson  ",
    "BOB SMITH",
    "charlie   BROWN123"
]

print("NAME CLEANING:")
for messy in messy_names:
    clean = clean_customer_name(messy)
    print(f"'{messy}' → '{clean}'")
```

---

# Sales Metrics Calculator

```python
def calculate_sales_metrics(sales_data):
    """Calculate comprehensive sales metrics"""
    if not sales_data or len(sales_data) == 0:
        return {"error": "No data provided"}
    
    total = sum(sales_data)
    count = len(sales_data)
    average = total / count
    
    # Calculate median
    sorted_sales = sorted(sales_data)
    mid = count // 2
    if count % 2 == 0:
        median = (sorted_sales[mid-1] + sorted_sales[mid]) / 2
    else:
        median = sorted_sales[mid]
    
    # Growth rate (last vs first)
    growth = ((sales_data[-1] - sales_data[0]) / sales_data[0]) * 100
    
    return {
        "total": total,
        "count": count,
        "average": average,
        "median": median,
        "highest": max(sales_data),
        "lowest": min(sales_data),
        "growth_rate": growth
    }
```

---

# Building a Function Library

Organize related functions together:

```python
"""
sales_utils.py - Sales Analysis Function Library
"""

def calculate_total(sales_list):
    """Calculate total sales"""
    return sum(sales_list)

def calculate_average(sales_list):
    """Calculate average sale"""
    if len(sales_list) == 0:
        return 0
    return sum(sales_list) / len(sales_list)

def find_top_sales(sales_list, n=5):
    """Find top N sales"""
    return sorted(sales_list, reverse=True)[:n]

def categorize_sale(amount):
    """Categorize sale by size"""
    if amount >= 1000:
        return "Large"
    elif amount >= 500:
        return "Medium"
    else:
        return "Small"
```

---

# Using the Function Library

```python
def generate_sales_report(sales_list):
    """Generate comprehensive sales report"""
    print("=" * 50)
    print("SALES ANALYSIS REPORT")
    print("=" * 50)
    
    total = calculate_total(sales_list)
    average = calculate_average(sales_list)
    top_3 = find_top_sales(sales_list, 3)
    
    print(f"\nTotal Sales: ${total:,.2f}")
    print(f"Average: ${average:,.2f}")
    print(f"Transactions: {len(sales_list)}")
    
    print("\nTop 3 Sales:")
    for i, sale in enumerate(top_3, 1):
        category = categorize_sale(sale)
        print(f"  {i}. ${sale:,.2f} ({category})")
    
    # Distribution
    large = sum(1 for s in sales_list if categorize_sale(s) == "Large")
    medium = sum(1 for s in sales_list if categorize_sale(s) == "Medium")
    small = sum(1 for s in sales_list if categorize_sale(s) == "Small")
    
    print(f"\nDistribution: {large} Large, {medium} Medium, {small} Small")

# Use the report
sales = [450, 1200, 750, 2100, 380, 950]
generate_sales_report(sales)
```

---

# Best Practices: Function Naming

**Good Names (Use Verbs):**
```python
def calculate_tax(price):
def validate_email(email):
def get_top_customers(customers):
def format_currency(amount):
```

**Bad Names:**
```python
def do_stuff(x):      # Too vague
def process(data):    # What kind of processing?
def func1(a, b):      # Meaningless name
def x(y):             # Single letters (except in math contexts)
```

**Guidelines:**
* Use verbs for actions (`calculate`, `get`, `validate`, `format`)
* Be descriptive but concise
* Use lowercase with underscores (`snake_case`)

---

# Best Practices: Docstrings

Document what your function does:

```python
def calculate_discount(price, rate):
    """
    Calculate discount amount based on price and rate.
    
    Parameters:
        price (float): Original price in dollars
        rate (float): Discount rate (0.0 to 1.0)
    
    Returns:
        float: Discount amount in dollars
    
    Example:
        >>> calculate_discount(100, 0.20)
        20.0
    """
    return price * rate
```

**Access docstring:**
```python
help(calculate_discount)  # Shows the docstring
print(calculate_discount.__doc__)  # Prints docstring
```

---

# Best Practices: Function Design Principles

**1. Single Responsibility**
Each function should do ONE thing well:
```python
# ✓ Good - focused functions
def calculate_tax(price):
    return price * 0.08

def calculate_discount(price):
    return price * 0.10

# ✗ Bad - doing too much
def process_order(price):
    tax = price * 0.08
    discount = price * 0.10
    shipping = 10
    return price + tax - discount + shipping
```

**2. Keep Functions Short**
If function is too long (>20-30 lines), break into smaller functions

**3. Avoid Side Effects**
Functions should not modify global variables unexpectedly

**4. Use Descriptive Parameters**
`calculate_price(base, tax, discount)` not `calc(x, y, z)`

---

# Common Patterns: Early Return

Exit early when validation fails:

```python
def calculate_profit_margin(revenue, cost):
    """Calculate profit margin percentage"""
    
    # Validate inputs first (early returns)
    if revenue <= 0:
        return 0
    
    if cost < 0:
        return 0
    
    # Main calculation (only if validation passed)
    profit = revenue - cost
    margin = (profit / revenue) * 100
    return margin

# Cleaner than nested if statements!
```

**Benefits:** Reduces nesting, improves readability, validates early

---

# Common Patterns: Helper Functions

Break complex logic into smaller helper functions:

```python
def is_valid_email(email):
    """Helper: Check if email is valid"""
    return "@" in email and "." in email

def is_premium_customer(total_purchases):
    """Helper: Check if customer is premium"""
    return total_purchases >= 1000

def send_welcome_email(name, email, purchases):
    """Send welcome email based on customer status"""
    
    # Use helpers for clarity
    if not is_valid_email(email):
        return "Invalid email"
    
    if is_premium_customer(purchases):
        message = f"Welcome to VIP, {name}!"
    else:
        message = f"Welcome, {name}!"
    
    print(f"Sending to {email}: {message}")
    return "Email sent"
```

---

# Variable Scope in Functions

**Local vs Global Scope:**

```python
# GLOBAL - visible everywhere
total_sales = 0

def process_sale():
    # LOCAL - only visible in this function
    sale_amount = 100
    tax = sale_amount * 0.08
    
    print(sale_amount)  # ✓ Works
    print(total_sales)  # ✓ Can read global

process_sale()

print(total_sales)   # ✓ Works
print(sale_amount)   # ✗ ERROR! Local variable doesn't exist here
```

**Golden Rule:** What happens in the function, stays in the function (unless returned)

---

# Modifying Global Variables

Use `global` keyword to modify global variables:

```python
counter = 0  # Global

def increment():
    global counter  # Tell Python to use global counter
    counter = counter + 1
    return counter

increment()
increment()
print(counter)  # 2

# Better approach: Return instead of modifying global
def increment_better(value):
    return value + 1

counter = 0
counter = increment_better(counter)
counter = increment_better(counter)
print(counter)  # 2
```

**Recommendation:** Avoid global variables when possible; use parameters and return values

---

# HANDS-ON EXERCISE 1

## Temperature Converter

Create functions for temperature conversion:

1. `celsius_to_fahrenheit(celsius)` - Convert C to F
   * Formula: F = (C × 9/5) + 32
   
2. `fahrenheit_to_celsius(fahrenheit)` - Convert F to C
   * Formula: C = (F - 32) × 5/9
   
3. Test with:
   * 0°C, 100°C, -40°C
   * 32°F, 212°F, -40°F

---

# HANDS-ON EXERCISE 2

## Grade Calculator System

Create a grading system with these functions:

1. `calculate_letter_grade(score)` - Return letter grade
   * A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: <60

2. `calculate_gpa(letter_grade)` - Convert letter to GPA
   * A=4.0, B=3.0, C=2.0, D=1.0, F=0.0

3. `get_class_average(scores_list)` - Calculate average

4. Test with: `[92, 85, 78, 95, 67, 88]`

---

# HANDS-ON EXERCISE 3

## Shopping Cart Calculator

Build shopping cart functions:

1. `calculate_subtotal(prices_list)` - Sum all prices

2. `calculate_tax(subtotal, tax_rate=0.08)` - Calculate tax

3. `apply_discount(amount, discount_percent=0)` - Apply discount

4. `calculate_total(prices, tax_rate=0.08, discount=0)` - Full calculation
   * Should use the other three functions
   
5. Test with: `[29.99, 49.99, 15.50]`, 8% tax, 10% discount

---

# Summary

The lesson covers:

* Why functions solve the copy-paste problem
* Function syntax and components
* Parameters (positional, keyword, default)
* Return values (single, multiple, dictionaries)
* Functions for data analysis tasks
* Building function libraries
* Best practices and common patterns
* Variable scope (local vs global)
* Started Sales Analytics mini-project

**Key Takeaway:** Functions make code reusable, maintainable, and professional


---

# Additional Resources

* [Python Functions Documentation](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
* [Real Python: Defining Your Own Python Function](https://realpython.com/defining-your-own-python-function/)
* [W3Schools: Python Functions](https://www.w3schools.com/python/python_functions.asp)
* [PEP 257: Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
* [Google Python Style Guide - Functions](https://google.github.io/styleguide/pyguide.html#383-functions-and-methods)

---

# Questions?

Remember:
* Functions are your friends!
* Write once, use everywhere
* Start simple, then build complexity
* Practice makes perfect

**Office Hours:** Available after class or by appointment

**Next Class:** Introduction to Pandas - Where functions meet data!