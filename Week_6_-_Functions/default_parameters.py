
def calculate_discount(price, discount_rate = 0.10):
    """Calculate price after discount"""
    discount_amount = price * discount_rate
    net_amount = price- discount_amount

    print("What is the value of discount_rate", discount_rate)

    return net_amount

# WHen you call a function with a default parameters, it's legal/okay to not provide an argument in place of that parameter
amount1 = calculate_discount(850)
print("Amount:", amount1)

# Overriding the default parameter value for discount_rate
amount2 = calculate_discount(850, 0.25)
print("Amount:", amount2)