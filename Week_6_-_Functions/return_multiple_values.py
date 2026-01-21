def analyze_sales(sales_list):
    """Calculate multiple statistics from sales data"""
    total = sum(sales_list)
    average = total / len(sales_list)
    highest = max(sales_list)
    lowest = min(sales_list)

    return total, average, highest, lowest


data = [1500, 920, 1800, 1100, 2200]

(total, average, highest, lowest) = analyze_sales(data)

print("Total sales value:", total)
print("Average sales value:", average)
print("Highest sales amount:", highest)
print("Lowest sales amount:", lowest)

# TODO: Return values as dictionary