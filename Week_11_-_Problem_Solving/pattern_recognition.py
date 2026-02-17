# Pattern 1: Filter
# Output of a filter operation is always an iterable (preferably a list)

# Template:

# results = []
# for item in []:
#     if condition:
#         results.append(item)

# Example Set: Find expensive transactions
import csv

expensive_transactions = []
__transactions = None

with open("customer_transactions.csv") as file:
    __transactions = csv.DictReader(file)

    for transaction in __transactions:
        transaction["Purchase_Amount"] = float(transaction["Purchase_Amount"])

        if transaction["Purchase_Amount"] > 100:
            expensive_transactions.append(transaction)

print(expensive_transactions)


# Pattern 2: Aggregate
# Output of an aggregate operation is always numeric - either an integer or a float

# Template:

# total = 0
# for item in collection:
#     total = item.get("field") + total

# result = total / count # if calculating average


# Example Set: Calculate total revenue
total_revenue = 0
for transaction in __transactions:
    total_revenue = total_revenue + float(transaction["Purchase_Amount"])

# Alternative approach using a mix of list comprehension and the sum() function
total_revenue = sum([float(transaction["Purchase_Amount"]) for transaction in __transactions])

average = total_revenue / len(list(__transactions))


# Pattern 3: Group By
# Output of a "group by" operation is always a dictionary - where the group name is the key and the group aggregate dataset is the value

# Template:

# groups = {}
# for item in collection:
#     key = item[field]
#     if key not in groups:
#         groups[key] = [] # = 0, = {}

#     groups[key].append(item)


# Example Set: Group transactions by category
transactions_by_categories = {
    "Jewelry": [{}, {}],
    "Food & Grocery": [{}],
    "Automotive": [{}, {}],
}

for transaction in __transactions:
    category = transaction["Product_Category"]

    if category in transactions_by_categories:
        transactions_by_categories[category].append(transaction)
    else:
        transactions_by_categories[category] = [transaction]


# Pattern 4: Min/Max

# Example Set: Find the most-valuable transaction
most_valuable_transaction = list(__transactions)[0]

for transaction in list(__transactions)[1:]:
    if transaction["Purchase_Amount"] > most_valuable_transaction["Purchase_Amount"]:
        most_valuable_transaction = transaction

# Alternative solution using a mix of the max() function and lambda
# most_valuable_transaction = max(__transactions, key=lambda x: x["Purchase_Amount"])


# Pattern 5: Transform

# Example Case: Create a list of email addresses for vip customers only (assuming there's a customer category column in the dataset)
# Filter + Transform operation
emails = []
for transaction in __transactions:
    if transaction["Group"] is "VIP":
        if transaction["Email"] not in emails:
            emails.append(transaction["Email"])

emails = set()
for transaction in __transactions:
    if transaction["Group"] is "VIP":
        emails.add(transaction["Email"])

# Example case: Extract customer names
customer_names = set()
for transaction in __transactions:
    customer_names.add(transaction["Customer_Name"])

