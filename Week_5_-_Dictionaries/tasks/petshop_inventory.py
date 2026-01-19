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

inventory_categories = petshop.keys()

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
print("")
category = input(f"Enter the category ({", ".join(inventory_categories)}): ")

while not (category in inventory_categories):
    print("")
    category = input(f"Invalid category. Choose from the options - {", ".join(inventory_categories)}: ")

print("")

#  Get the sub categories using the selected category (as provided from the input() function)
inventory_sub_categories = petshop[category].keys()

sub_category = input(f"Select from the available sub-categories ({", ".join(inventory_sub_categories)}): ")

# Get the products and their quantity for the selected sub-category
inventory_products = petshop[category][sub_category]

product = input(f"What product do you want? ({", ".join(inventory_products.keys())}): ")

stock_qty = petshop[category][sub_category][product]

requested_qty = int(input(f"How many do you want? ({stock_qty})? "))

while requested_qty > stock_qty:
    requested_qty = int(input(f"Sorry, we only have {stock_qty} in stock: "))

petshop[category][sub_category][product] = stock_qty - requested_qty


print("")
print("="*60)
print("************** UPDATED INVENTORY **************")
pprint(petshop[category])
print("="*60)
print("")






