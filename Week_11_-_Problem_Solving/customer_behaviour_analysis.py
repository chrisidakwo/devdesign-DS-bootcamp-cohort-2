import csv

def load_transaction_data(filename):
    """Load transaction data from CSV"""
    transactions = []
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                # Convert Purchase_Amount to float
                row['Purchase_Amount'] = float(row['Purchase_Amount'])
                transactions.append(row)
        
        return transactions
    
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []
    
def build_customer_profiles(transactions):
    """
    Pattern: Group By Pattern
    """
    customer_profiles = {}
    
    for tx in transactions:
        customer_id = tx["Customer_ID"]

        if customer_id not in customer_profiles:
            customer_profiles[customer_id] = {
                "id": tx["Customer_ID"],
                "name": tx["Customer_Name"],
                "email": tx["Email"],
                "signup_date": tx["Signup_Date"],
                "transactions": [],
                "total_transactions": 0,
                "total_spent": 0,
            }

        customer_profiles["transactions"].append(tx)
        customer_profiles["total_spent"] += tx["Purchase_Amount"]

    return customer_profiles

def display_customer_summary(customer_profiles):
    """
    - Total unique customers
    - Average transactions per customer
    - Average spend per customer
    - Customer with most transactions
    - Customer with highest total spend
    """

    # 1. Total unique customers
    total_unique_customers = len(customer_profiles.keys())

    # 2. Average transactions (count) per customer
    customer_transactions = []
    for profile in customer_profiles.values():
        customer_transactions.append(len(profile["transactions"]))
    
    avg_transactions = sum(customer_transactions) / total_unique_customers
    
    # Alternative method for implementing the preceeding code for calculating average transactions per customer
    # total_transactions = sum([len(p["transactions"]) for p in customer_profiles.values()])
    # avg_transactions = total_transactions / total_unique_customers

    # 3. Average spend per customer
    customer_total_spend = []
    for profile in customer_profiles.values():
        customer_total_spend.append(profile["total_spent"])

    avg_clv = sum(customer_total_spend) / total_unique_customers

    # Alternative method for implementing the preceeding code for calculating average life-time value of a customer (i.e. average spend per customer)
    # total_spent = sum([p["total_spent"] for p in customer_profiles.values()])
    # avg_clv = total_spent / total_unique_customers

    # 4. TODO: Most Active Customer (Customer with the most number of transactions)

    # 5. Most-Valuable Customer (Highest Spending Customer)
    mvp_customer = max(customer_profiles.values(), key=lambda x: x["total_spent"])

    return {
        "total_customers": total_unique_customers,
        "avg_tx_count_per_customer": avg_transactions,
        "avg_spend_per_customer": avg_clv,
        "mvp_customer": mvp_customer,
    }

def main():
    transactions = load_transaction_data("files/customer_transactions.csv")
    customer_profiles = build_customer_profiles(transactions)
    customer_summary = display_customer_summary(customer_profiles)

    # TODO: Use the main function to display to the terminal
    # ```txt
    #     CUSTOMER DATABASE SUMMARY
    #     =========================
    #     Total Customers: 1,523
    #     Average Transactions per Customer: 4.2
    #     Average Customer Lifetime Value: $487.65
    #     Most Active Customer: CUST-0456 (23 transactions)
    #     Highest Spending Customer: CUST-0892 ($3,456.78)
    # ```

if __name__ == "__main__":
    main()