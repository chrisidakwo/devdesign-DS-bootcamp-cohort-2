total = 0
for order in orders:
    total += order["amount"]
print(total)


# Snippet 2
high_scorers = []
for student in students:
    if student["score"] >= 90:
        high_scorers.append(student["name"])

print(high_scorers)


# Snippet 3
product_categories = {}
for product in products:
    category = product["category"]
    if category not in product_categories:
        product_categories[category] = []
    
    product_categories[category].eppend(product)


# Snippet 4
most_expensive = products[0]
for product in products:
    if product["price"] > most_expensive["price"]:
        most_expensive = product

print(most_expensive["name"])


# Snippet 5
ages = []
for person in people:
    ages.append(person["age"])

x = sum(ages) / len(ages)
print(x)

# Snippet 6
region_totals = {}

for sale in sales:
    region = sale["region"]

    # if region in region_totals:
    #     region_totals[region] += sale["amount"]
    # else:
    #     region_totals[region] = sale["amount"]

    if region not in region_totals:
        region_totals[region] = 0
    
    region_totals[region] += sale["amount"]

# Snippet 7
discounted_prices = []
for product in products:
    new_price = product["price"] * 0.8
    discounted_prices.append(new_price)

print(discounted_prices)

# Snippet 8
youngest = people[0]
for person in people:
    if person["age"] < youngest["age"]:
        youngest = person

print(youngest["name"])

# print(min(people, key=lambda x: x["age"])["name"])


