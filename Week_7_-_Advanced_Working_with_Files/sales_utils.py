# Define constants
TAX_RATE = 0.08
DISCOUNT_THRESHOLD = 1000

def calculate_total(sales_list):
    """Calculates total sales amount"""
    return sum(sales_list)

def calculate_average(sales_list):
    """Calculate average sales amount"""
    return sum(sales_list) / len(sales_list)

def find_top_sales(sales_list):
    """Find the highest sale"""
    return max(sales_list)
