# 1. Understand 
# 2. Input 
# 3. Output 
# 4. Pattern 
# 5. Skeleton 
# 6. Implement

# Problem: Find the top 3 customers for the business
def find_top_3_customers(transactions):
    # Step 1: Group by customer and sum spending
    customer_totals = {}

    for transaction in transactions:
        # Extract customer ID and purchase amount
        customer_id = transaction["Customer_Name"]
        purchase_amt = float(transaction["Purchase_Amount"])

        # Recursively increment the purchase amount for each customer (identified by the customer ID)
        if customer_id not in customer_totals:
            customer_totals[customer_id] = purchase_amt
        else:
            customer_totals[customer_id] += purchase_amt


    # Step 2: Convert to list and sort
    # Create a list of (ID, total) tuples
    # Sort by total (in descending order)

    top_customers = []
    
    for (customer_id, total_spent) in customer_totals.items():
        top_customers.append((customer_id, total_spent))

    top_customers.sort(key=lambda x: x[1], reverse=True)
    top_customers = top_customers[:3]

    result = ", ".join([f"{cust[0]} - ${cust[1]:.1f}" for cust in top_customers])

    print(result)


def main():
    import csv

    with open("files/customer_transactions.csv") as file:
        reader = csv.DictReader(file)

        transactions = []

        for item in reader:
            item["Purchase_Amount"] = float(item["Purchase_Amount"])
            transactions.append(item)

        find_top_3_customers(transactions)


main()
