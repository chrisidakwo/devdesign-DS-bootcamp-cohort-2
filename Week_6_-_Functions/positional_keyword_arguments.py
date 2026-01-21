# Positional vs Keyword Arguments

def create_customer_profile(name, age, city, purchases):
    """Create a customer profile summary"""
    print(f"\nCustomer: {name}")
    print(f"Age: {age}")
    print(f"Location: {city}")
    print(f"Total Purchases: {purchases}")

# In positional arguments, order matters
create_customer_profile("Alice", 28, "Abuja", 15)

create_customer_profile(28, "Alice", "Abuja", 15)

# However, in keyword arguments, order doesn't matter
create_customer_profile(city="Lagos", name="Bob", purchases=8, age=35)

# You can mix positional and keyword arguments. However, when you do so, positional arguments must come first
create_customer_profile("Chris", 20, city="Owerri", purchases=10)

