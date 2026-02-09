import csv
from datetime import datetime
from pprint import pprint

transactions = []

with open("exercises/customer_transactions.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        transactions.append(row)

transactions.sort(key=lambda x: datetime.strptime(x["Transaction_Date"], "%Y-%m-%d"))

headers = ["Customer_ID", "Customer_Name", "Email", "Signup_Date", "Transaction_Date", "Product_Category", "Purchase_Amount", "Payment_Method", "Device"]

with open("exercises/customer_transactions.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(transactions)
    