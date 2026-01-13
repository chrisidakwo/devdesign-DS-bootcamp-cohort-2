# Website Traffic Analytics

# As a Data Analyst, your job is to analyze the website traffic data for an ecommerce site.
# The marketing team needs to understand which pages users visit most frequently to optimize their
# ad spend and/or marketing strategy

# The Problem
# You have a log of page visits from 50 users. You need to:
# 1. Count how many times each page was visited
# 2. Find the most and least popular pages
# 3. Calculate what percentage of traffic each page receives
# 4. Identify pages with low traffic, that need promotion

import random
from pprint import pprint

pages = ["products", "product profile", "about", "home", "checkout", "cart", "contact"]
users = 50

log_of_pages_visited = []

for i in range(users):
    rounds = random.randint(3, 20)
    for take in range(rounds):
        index = random.randint(0, 6)
        log_of_pages_visited.append(pages[index])

# Step 1 - Count page visits
# Concept: Use dictionaries to count frequency - a fundamental data science task

page_counts = {}

for page in log_of_pages_visited:
    if page in page_counts:
        page_counts[page] = page_counts[page] + 1
    else:
        page_counts[page] = 1
    
print("\n")
print(log_of_pages_visited)
print("\n")
pprint(page_counts)

# Step 2 - Find Most Visited & Least Visited Pages
# Concept: Extract insights from the frequency data

all_counts = page_counts.values()
max_visits = max(all_counts)
min_visits = min(all_counts)

print("\nMost popular pages:")
for (key, value) in page_counts.items():
    # In this context, the key is the page name, while the value is the visit frequency - i.e. how many times the page was visited
    if value == max_visits:
        print(f"    - {key}: {value} visits")


print("\nLeast popular pages:")
for (key, value) in page_counts.items():
    if value == min_visits:
        print(f"    - {key}: {value} visits")


# Step 3 - Calculate traffic percentage
# Concept: Convert page visit count to percentages for better insight

total_visits = sum(page_counts.values())

print(f"\nTotal visits: {total_visits}")
print("\nTraffic Distribution:")

page_percentages = {}

for (key, value) in page_counts.items():
    # In this context, the key is the page name, while the value is the visit frequency - i.e. how many times the page was visited

    percentage = (value / total_visits) * 100
    page_percentages[key] = f"{percentage:.1f}"
    print(f"    {key}: {value} visits ({page_percentages[key]}%)")

# Step 4 - Identify Pages Needing Promotion
# Concept: Use conditional logic with dictionary data to genrate insight
low_traffic_threshold = 13 # percentage
low_traffic_pages = {}

print("\nPAGES NEEDING PROMOTION:")

for (key, value) in page_percentages.items():
    percentage_val = float(value)

    if percentage_val <= low_traffic_threshold:
        low_traffic_pages[key] = percentage_val

if len(low_traffic_pages) == 0:
    print(" All pages have adequate traffic")
else:
    pprint(low_traffic_pages)

