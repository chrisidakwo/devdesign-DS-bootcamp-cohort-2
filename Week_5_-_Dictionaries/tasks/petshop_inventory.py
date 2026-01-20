from pprint import pprint

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

# - animal (dogs, cats, fish, birds)
# - supplies (foods, toys, habitats)

stock_categories = petshop.keys()

print("")
pprint(petshop)

print("\n")
print("="*60)
print("PETSHOP INVENTORY")
print("="*60)

# Task 1
# Your task is to dynamically update the quantity of a supply item after a sale.
# Request as much information from the user in order to know what product is to be sold.
# Print out your inventory after each sale.
category = input(f"\nEnter the category ({", ".join(stock_categories)}): ")

# Validate the category entered by the user. If not valid, display the input again
while not (category in stock_categories):
    print("")
    category = input(f"\nInvalid category. Choose from the options - {", ".join(stock_categories)}: ")

# Get the sub categories using the selected category (as provided from the input() function)
stock_sub_categories = petshop[category].keys()

# Ask the user to select from the available sub-categories in our inventory stock
sub_category = input(f"\nSelect from the available sub-categories ({", ".join(stock_sub_categories)}): ")

# Get the products and their quantity for the selected sub-category
stock_products = petshop[category][sub_category]

# Ask the user to select the product they want buy from our inventory stock
product = input(f"\nWhat product do you want? ({", ".join(stock_products.keys())}): ")

# Get the inventory stock quantity for the product selected by the user
stock_qty = petshop[category][sub_category][product]

# Ask the user to provide the quantity they want to buy, while also displaying the available quantity
requested_qty = int(input(f"\nHow many do you want? (Available Qty: {stock_qty})? "))

# Ensure that the quantity requested by the user is not more than what is available in stock
while requested_qty > stock_qty:
    requested_qty = int(input(f"\nSorry, we only have {stock_qty} in stock: "))

# Reduce the requested quantity from what is available in stock
petshop[category][sub_category][product] = stock_qty - requested_qty

print("")
print("="*60)
print("************** UPDATED INVENTORY **************")
pprint(petshop[category])
print("="*60)
print("")






