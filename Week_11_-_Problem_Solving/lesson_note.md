# **Computational Thinking & Problem-Solving**

---

## **🎯 Objective**

By the end of this week, students will be able to:

✅ **Read and explain** existing code fluently  
✅ **Recognize** the 5 core programming patterns in problem descriptions  
✅ **Translate** English requirements into code structure  
✅ **Decompose** complex problems into functions  
✅ **Write** skeleton code before implementation  
✅ **Debug** systematically using manual tracing  
✅ **Solve** new problems independently using a repeatable framework  

---

## **🧠 Core Philosophy**

> **"Programming is not about memorizing syntax.  
> Programming is about recognizing patterns and transforming data step-by-step."**

Everything reduces to:

1. **What is the INPUT?**
2. **What transformation must happen?**
3. **What is the OUTPUT?**

---

## **⚠️ CRITICAL RULES**

### **FORBID:**

- ❌ Immediate coding without planning
- ❌ "I'll just try random things"
- ❌ Copying from ChatGPT/internet without understanding
- ❌ Writing 50 lines before testing

### **ENFORCE:**

- ✅ Read code before writing code
- ✅ English explanation first, then code
- ✅ Pattern identification mandatory
- ✅ Skeleton code before details
- ✅ Test after every function

---

# 📅 **DAY 1 – Pattern Recognition & Code Reading**

## **🎯 Goal**

Learn to READ code fluently and RECOGNIZE the 5 core patterns that solve 80% of problems.

---

## **The 5 Core Patterns**

### **Pattern Introduction**

**Each pattern is listed with:**

1. Pattern name
2. Keywords that signal it
3. Code template
4. 3 worked examples

---

### **PATTERN 1: FILTER**

**When to use:** "Find all...", "Get items where...", "Select customers who...", "Filter by..."

**Template:**

```python
results = []
for item in collection:
    if condition:
        results.append(item)
```

**Example 1: Find expensive products**

```python
expensive_products = []
for product in products:
    if product['price'] > 100:
        expensive_products.append(product)
```

**Example 2: Find students who passed**

```python
passed_students = []
for student in students:
    if student['grade'] >= 60:
        passed_students.append(student)
```

**Example 3: Find West region sales**

```python
west_sales = []
for sale in sales:
    if sale['region'] == 'West':
        west_sales.append(sale)
```

**Example 4: Find customers who spent over $5000 and been active for more than 2 years**

```python
premium_customers = []
for customer in customers:
    if customer['total_spent'] > 5000 and customer['years_active'] > 2:
        premium_customers.append(customer)

# Pattern: FILTER (multiple conditions)
```

**Key insight:** "Any time you see 'find all' or 'get items where', it's a FILTER pattern."

---

### **PATTERN 2: AGGREGATE**

**When to use:** "Calculate total...", "Find average...", "Count how many...", "Sum all..."

**Template:**

```python
total = 0  # or count = 0
for item in collection:
    total += item[field]  # or count += 1
result = total / count  # if calculating average
```

**Example 1: Calculate total revenue**

```python
total_revenue = 0
for sale in sales:
    total_revenue += sale['amount']

# Alternative approach using a mix of list comprehension and the sum() function
total_revenue = sum([float(sale['amount']) for sale in sales])
```

**Example 2: Count products**

```python
product_count = 0
for product in products:
    product_count += 1
# Or simply: product_count = len(products)
```

**Example 3: Calculate average score**

```python
total_score = 0
for student in students:
    total_score += student['score']
average_score = total_score / len(students)
```

**Example 4: Calculate average inventory value per product**

```python
product_count = 0
total_value = 0
for item in inventory:
    product_count += 1
    total_value += item['price'] * item['quantity']
average_value = total_value / product_count
# Pattern: AGGREGATE (multiple calculations)
```

**Key insight:** "Anytime you're combining values into one number, it's AGGREGATE."

---

### **PATTERN 3: GROUP BY**

**When to use:** "By category...", "Per customer...", "Group by region...", "Organize by..."

**Template:**

```python
groups = {}
for item in collection:
    key = item[field]
    if key not in groups:
        groups[key] = []  # or = 0, or = {'count': 0, 'total': 0}
    groups[key].append(item)  # or groups[key] += value
```

**Example 1: Group sales by region**

```python
sales_by_region = {}
for sale in sales:
    region = sale['region']
    if region not in sales_by_region:
        sales_by_region[region] = []
    sales_by_region[region].append(sale)
```

**Example 2: Count products by category**

```python
category_counts = {}
for product in products:
    category = product['category']
    if category not in category_counts:
        category_counts[category] = 0
    category_counts[category] += 1
```

**Example 3: Sum sales by customer**

```python
customer_totals = {}
for sale in sales:
    customer = sale['customer_id']
    if customer not in customer_totals:
        customer_totals[customer] = 0
    customer_totals[customer] += sale['amount']
```

**Example 4: Calculate total revenue for each month**

```python
monthly_revenue = {}
for order in orders:
    month = order['date'][:7]  # Extract YYYY-MM
    if month not in monthly_revenue:
        monthly_revenue[month] = 0
    monthly_revenue[month] += order['total']

# Pattern: GROUP BY + AGGREGATE
```

**Key insight:** "When organizing by categories, use dictionaries. This is GROUP BY."

---

### **PATTERN 4: FIND MAX/MIN**

**When to use:** "Find highest...", "Get best...", "Find oldest...", "Get minimum..."

**Template:**

```python
best = collection[0]  # Start with first item
for item in collection:
    if item[field] > best[field]:  # or < for minimum
        best = item
```

**Example 1: Find highest-priced product**

```python
most_expensive = products[0]
for product in products:
    if product['price'] > most_expensive['price']:
        most_expensive = product

# Alternative solution using a mix of the max() function and lambda
# most_expensive = max(products, key=lambda x: x["price"])
```

**Example 2: Find top-scoring student**

```python
top_student = students[0]
for student in students:
    if student['score'] > top_student['score']:
        top_student = student
```

**Example 3: Find oldest customer**

```python
oldest = customers[0]
for customer in customers:
    if customer['age'] > oldest['age']:
        oldest = customer
```

**Example 4: Get names of top 3 products by sales**

```python
top_3 = []
sorted_products = sorted(products, key=lambda x: x['sales'], reverse=True)
for i in range(3):
    top_3.append(sorted_products[i]['name'])

# Pattern: FIND MAX (top N)
```

**Pro tip:**

```python
# Python has built-in max()
top_student = max(students, key=lambda x: x['score'])
```

---

### **PATTERN 5: TRANSFORM**

**When to use:** "Convert each...", "Calculate X for every...", "Create a list of...", "Map to..."

**Template:**

```python
results = []
for item in collection:
    new_item = transform(item)  # Some calculation or conversion
    results.append(new_item)
```

**Example 1: Convert prices to euros**

```python
prices_in_euros = []
for product in products:
    euro_price = product['price'] * 0.85
    prices_in_euros.append(euro_price)
```

**Example 2: Extract customer names**

```python
customer_names = []
for customer in customers:
    customer_names.append(customer['name'])
```

**Example 3: Calculate discounted prices**

```python
discounted_prices = []
for product in products:
    discounted = product['price'] * 0.9  # 10% off
    discounted_prices.append(discounted)
```

**Example 4: Create list of email addresses for subscribed customers only**

```python
emails = []
for customer in customers:
    if customer['subscribed']:
        emails.append(customer['email'])

# Pattern: FILTER + TRANSFORM
```

**Example 5: Create list of product prices with 20% discount applied**

```python
discounted_prices = []
for product in products:
    new_price = product['price'] * 0.8
    discounted_prices.append(new_price)
```

---

### **Pattern Summary Table**

**Give students this reference card:**

| Pattern | Keywords | Usually Requires | Purpose |
|---------|----------|------------------|---------|
| **FILTER** | "Find all", "Get where", "Select items" | `for` + `if` + list | Get subset matching criteria |
| **AGGREGATE** | "Total", "Average", "Count", "Sum" | Variable + `for` | Combine values into one number |
| **GROUP BY** | "By category", "Per customer", "Group by" | Dictionary + `for` | Organize by categories |
| **FIND MAX/MIN** | "Highest", "Best", "Lowest", "Oldest" | Variable + `for` + comparison | Find extreme value |
| **TRANSFORM** | "Convert each", "Calculate for each" | List + `for` | Change each item |

---

## **Code Reading Practice**

Most beginners try to write code before they can read code. That's backwards! You need to read fluently before you can write fluently. Today we'll practice reading.

---

### **Exercise 1: Code Explanation**

**Instructions:** "For each code snippet, write in plain English what it does. Don't say 'it loops through' - say what the PURPOSE is."

Give students worksheet with 15 snippets:

```python
# Snippet 1
total = 0
for order in orders:
    total += order['amount']
print(total)

# Student writes: "Calculates total of all order amounts"
```

```python
# Snippet 2
high_scorers = []
for student in students:
    if student['score'] >= 90:
        high_scorers.append(student['name'])

# Student writes: "Creates list of students who scored 90 or above"
```

```python
# Snippet 3
product_categories = {}
for product in products:
    category = product['category']
    if category not in product_categories:
        product_categories[category] = []
    product_categories[category].append(product)

# Student writes: "Groups products by their category"
```

```python
# Snippet 4
most_expensive = products[0]
for product in products:
    if product['price'] > most_expensive['price']:
        most_expensive = product
print(most_expensive['name'])

# Student writes: "Finds the most expensive product"
```

```python
# Snippet 5
ages = []
for person in people:
    ages.append(person['age'])
average_age = sum(ages) / len(ages)

# Student writes: "Calculates average age of all people"
```

```python
# Snippet 6
region_totals = {}
for sale in sales:
    region = sale['region']
    if region not in region_totals:
        region_totals[region] = 0
    region_totals[region] += sale['amount']

# Student writes: "Calculates total sales amount for each region"
# Pattern: GROUP BY + AGGREGATE
```

**Continue with 10 more snippets of varying complexity.**

---

### **Exercise 2: Pattern Identification**

**Instructions:** "For each problem description, identify which pattern you'd use. Don't write code yet!"

**Problems:**

1. "Calculate the average customer spending" → **AGGREGATE**
2. "List all orders over $500" → **FILTER**
3. "Group sales by month" → **GROUP BY**
4. "Find the oldest customer" → **FIND MAX/MIN**
5. "Convert temperatures from Celsius to Fahrenheit" → **TRANSFORM**
6. "Count how many products are out of stock" → **AGGREGATE (count)**
7. "Find customers who made more than 5 purchases" → **FILTER**
8. "Calculate total revenue by region" → **GROUP BY + AGGREGATE**
9. "Get the top 3 best-selling products" → **FIND MAX/MIN**
10. "Create a list of customer emails" → **TRANSFORM**
11. "Find students who failed (grade < 60)" → **FILTER**
12. "Group employees by department" → **GROUP BY**
13. "Find the cheapest item in inventory" → **FIND MAX/MIN**
14. "Calculate the sum of all invoice amounts" → **AGGREGATE**
15. "Get product names and prices (from product objects)" → **TRANSFORM**

---

### **Exercise 3: Reverse Engineering**

**Instructions:** "This code solves a problem. What was the problem?"

```python
# Mystery Code 1
eligible = []
for applicant in applicants:
    if applicant['age'] >= 18 and applicant['has_license']:
        eligible.append(applicant)

# Answer: "Find all applicants who are 18+ and have a license"
# Pattern: FILTER (with multiple conditions)
```

```python
# Mystery Code 2
regional_sales = {}
for sale in sales:
    region = sale['region']
    if region not in regional_sales:
        regional_sales[region] = 0
    regional_sales[region] += sale['amount']

# Answer: "Calculate total sales by region"
# Pattern: GROUP BY + AGGREGATE
```

```python
# Mystery Code 3
newest = orders[0]
for order in orders:
    if order['date'] > newest['date']:
        newest = order

# Answer: "Find the most recent order"
# Pattern: FIND MAX
```

---

# 📅 **DAY 2 – Systematic Problem-Solving & Decomposition **

