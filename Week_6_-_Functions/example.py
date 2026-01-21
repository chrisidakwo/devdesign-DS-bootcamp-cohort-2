



# --------------------------------------------------------------
# Refactor (Option 1)
# --------------------------------------------------------------
def calculate_average(sales_data):
    """Calcuate average of sales values"""
    total_sales_value = 0
    total_sales_count = 0

    for sale in sales_data:
        total_sales_value += sale
        total_sales_count += 1

    average = total_sales_value / total_sales_count
    return average


north_sales = [1200, 850, 2100, 1450, 980]
south_sales = [1500, 920, 1800, 1100, 2200]
east_sales = [1100, 1300, 950, 1700, 1200]

print(f"North Average: ${calculate_average(north_sales)}")
print(f"South Average: ${calculate_average(south_sales)}")
print(f"East Average: ${calculate_average(east_sales)}")


# --------------------------------------------------------------
# Refactor (Option 2)
# --------------------------------------------------------------

def calculate_average_alt(sales_data, region):
    """Calcuate average of sales values"""
    total_sales_value = 0
    total_sales_count = 0

    for sale in sales_data:
        total_sales_value += sale
        total_sales_count += 1

    average = total_sales_value / total_sales_count

    print(f"{region} Average: ${average}")
    
sales = {
    "North": [1200, 850, 2100, 1450, 980],
    "South": [1500, 920, 1800, 1100, 2200],
    "East": [1100, 1300, 950, 1700, 1200],
}

for region, sales_data in sales.items():
    calculate_average_alt(sales_data, region)
