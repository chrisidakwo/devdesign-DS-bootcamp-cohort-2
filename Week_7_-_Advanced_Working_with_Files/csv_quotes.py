import csv

with open('files/house_prices.csv', 'r') as file:
    reader = csv.reader(
        file,
        quotechar="'",  # Character used for quotes
        quoting=csv.QUOTE_MINIMAL  # When to quote fields
    )

    for row in reader:
        print(row)