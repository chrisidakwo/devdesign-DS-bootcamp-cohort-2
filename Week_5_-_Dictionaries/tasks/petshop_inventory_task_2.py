petshop = {
    "animals": {
        "dogs": {"Labrador": 3, "Beagle": 2, "Poodle": 1, "Mastiff": 5},
        "cats": {"Persian": 2, "Siamese": 1, "Maine Coon": 2},
        "fish": {"Goldfish": 12, "Angelfish": 5, "Betta": 3},
        "birds": {"Parakeet": 4, "Canary": 3, "Cockatiel": 7}
    },
    "supplies": {
        "food": {"Dog Food": 20, "Cat Food": 9, "Fish Food": 25},
        "toys": {"Dog Toys": 30, "Cat Toys": 20},
        "habitats": {"Aquariums": 5, "Cat Trees": 8, "Dog Beds": 7}
    },
}

print("\n")
print("="*60)
print("PETSHOP INVENTORY")
print("="*60)

# Task 2
# Create a shopping list of supplies that are low in stock (fewer than 10)

# Approach 1
low_stock_products = []

supplies = petshop["supplies"]
for (sub_category, products) in supplies.items():
    for product, qty in products.items():
        if qty < 10:
            low_stock_products.append(product)

print(low_stock_products)

# Approach 2
shopping_list = [
    item
    for products in supplies.values()
    for item, qty in products.items()
    if qty < 10
]

print(shopping_list)
