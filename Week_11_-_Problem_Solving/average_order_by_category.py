# 1. Understand 
# 2. Input 
# 3. Output 
# 4. Pattern 
# 5. Skeleton 
# 6. Implement


# Problem: Calculate the average order value by product categories

# 1. Understading the problem set
# average order value = total sales amount / total number of orders

def average_order_by_category(orders):
    # Step 1: Group by category, track the sum and count values for each category

    # NOTE: You can use one dictionary (rather than two as done below) to keep track of the
    # total order value and count (number of occurrences) for each category

    category_totals = {}
    category_counts = {}

    for order in orders:
        # Get the category name and purchase amount
        category_name = order["Product_Category"]
        purchase_amt = order["Purchase_Amount"]

        #region Recursively increment to total amount, and increment the count (by 1)

        # - For the `category_totals` variable
        if category_name not in category_totals:
            category_totals[category_name] = purchase_amt
        else:
            category_totals[category_name] += purchase_amt

        #- For the `category_counts` variable
        if category_name not in category_counts:
            category_counts[category_name] = 1
        else:
            category_counts[category_name] += 1
        #endregion
    
    # Step 2: Calculate averages
    # Introduce a new variable to keep track of average values
    category_averages = {}

    # Loop through the category_totals, get the category name, the total order value
    #   Use the category name to retrieve the count/occurrences
    for (category, total) in category_totals.items():
        count = category_counts[category]

        # Calculate average using the total order value and the count
        category_averages[category] = total / count
    
    # Neatly display the result (categories and their respective average order values)
    print("")
    print(f"{'Product Category':<24} {'Avg Order Value (USD)':<8}")
    print("-"*50)
    for (cat, avg) in category_averages.items():
        print(f"{cat:<24} ${avg:>8,.2f}")
    print("")

def main():
    import csv

    with open("files/customer_transactions.csv") as file:
        reader = csv.DictReader(file)

        transactions = []

        for item in reader:
            item["Purchase_Amount"] = float(item["Purchase_Amount"])
            transactions.append(item)

        average_order_by_category(transactions)

main()
