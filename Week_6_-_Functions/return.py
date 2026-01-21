# "return" helps us send out
# The "return" keyword can be used only within a function

sales = [261.96, 731.94, 14.62, 957.5, 1706.18, 95, 43, 17, 48, 71, 54, 63]

def calculate_average(values):
    sales_count = len(values)
    total_sales = sum(values)

    average = total_sales / sales_count

    print("\nWhat is average?", average)

    return average


result = calculate_average(sales)
print(f"The average value of sales for the month of December 2025 was {result}")

# --------------------------------------------------------------
# MULTIPLE RETURNS
# A function can have multiple return statements 
# --------------------------------------------------------------

def calculate_bmi(weight_kg, height_m):
    """Calculates Body Mass Index (BMI)"""
    bmi = weight_kg / (height_m ** 2)
    return bmi

def get_bmi_category(bmi):
    """Get BMI category as a string"""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

height = 1.75
weight = 70

bmi_value = calculate_bmi(weight, height)
category = get_bmi_category(bmi_value)

print(f"\nHeight: {height}")
print(f"Weight: {weight}")
print(f"BMI: {bmi_value:.1f}")
print(f"Category: {category}")
