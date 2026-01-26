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

def get_category(stock_categories):
    category = input(f"\nEnter the category ({", ".join(stock_categories)}): ")

    # Validate the category entered by the user. If not valid, display the input again
    while not (category in stock_categories):
        print("")
        category = input(f"\nInvalid category. Choose from the options - {", ".join(stock_categories)}: ")

    return category

def get_sub_category(stock_sub_categories):
    # Ask the user to select from the available sub-categories in our inventory stock
    # TODO: Take-home. Introduce validation just like the `get_category()` function
    return input(f"\nSelect from the available sub-categories ({", ".join(stock_sub_categories)}): ")

def get_selected_product(stock_products):
    # Ask the user to select the product they want buy from our inventory stock
    return input(f"\nWhat product do you want? ({", ".join(stock_products.keys())}): ")

def get_requested_qty(stock_qty):
    # Ask the user to provide the quantity they want to buy, while also displaying the available quantity
    requested_qty = int(input(f"\nHow many do you want? (Available Qty: {stock_qty})? "))

    # Ensure that the quantity requested by the user is not more than what is available in stock
    while requested_qty > stock_qty:
        requested_qty = int(input(f"\nSorry, we only have {stock_qty} in stock: "))

    return requested_qty

def get_low_stock_supplies(supplies):
    """Returns a list of products that are low in stock (< 10 in qty).
    Each product entry is a dictionary.
    """
    # Task 2
    # Create a shopping list of supplies that are low in stock (fewer than 10)

    # Approach 1
    low_stock_products = []

    for (sub_category, products) in supplies.items():
        for product, qty in products.items():
            if qty < 10:
                low_stock_products.append(product)

    return low_stock_products

    # Approach 2
    shopping_list = [
        item
        for products in supplies.values()
        for item, qty in products.items()
        if qty < 10
    ]

    print(shopping_list)

def get_most_varied_product(animals):
    """
    Find which animal type has the most variety.
    """
    # Task 3
    # Find which animal type has the most variety.
    # Variety in this case means the animal with the most headcount and number of breeds.

    max_variety = 0
    most_varied_animal = None

    for sub_category, breeds in animals.items():
        num_of_breeds = len(breeds.keys())
        headcount = sum(breeds.values())

        variety = num_of_breeds + headcount

        if variety > max_variety:
            max_variety = variety
            most_varied_animal = sub_category

    return {
        "product": most_varied_animal,
        "variety_count": max_variety
    }

def main():
    """Entrypoint into the application"""
    print("\n")
    print("="*60)
    print("PETSHOP INVENTORY")
    print("="*60)

    stock_categories = petshop.keys()
    category = get_category(stock_categories)

    stock_sub_categories = petshop[category].keys()
    sub_category = get_sub_category(stock_sub_categories)

    # Get the products and their quantity for the selected sub-category
    stock_products = petshop[category][sub_category]

    selected_product = get_selected_product(stock_products)

    # Get the inventory stock quantity for the product selected by the user
    stock_qty = petshop[category][sub_category][selected_product]

    requested_qty = get_requested_qty(stock_qty)

    # Reduce the requested quantity from what is available in stock
    petshop[category][sub_category][selected_product] = stock_qty - requested_qty

    print("")
    print("="*60)
    print("************** UPDATED INVENTORY **************")
    pprint(petshop[category])
    print("="*60)
    print("")

    print("\n")
    low_stock_supplies = get_low_stock_supplies(petshop["supplies"])
    
    print("="*30)
    print("Low-Stock Products")
    print("="*30)
    print(low_stock_supplies)

    print("\n")
    most_varied_product = get_most_varied_product(petshop["animals"])
    print("="*30)
    print("Most-Varied Product")
    print("="*30)
    pprint(most_varied_product)

# Execute the main function
main()
