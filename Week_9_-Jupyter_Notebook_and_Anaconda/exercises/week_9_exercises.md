# Take-Home Exercises - Data Analysis Projects

## **Instructions for Both Exercises**

### **Submission Requirements:**

1. **Python file (.py)** - Your main analysis code
2. **Jupyter Notebook (.ipynb)** - Step-by-step analysis with explanations for your approach
3. **Output files** - CSV/text files with your results

---

## **EXERCISE 1: Superstore Sales Analysis System**

### **Scenario**

You're a junior data analyst at a retail company. The sales team has provided you with a CSV file containing transaction records for the past year. Your manager needs insights to make strategic decisions about inventory, regional focus, and product mix.

### **Dataset Description**

You'll work with `superstore_sales.csv` for this exercise.

---

### **Your Tasks**

#### **Part 1: Data Loading and Exploration**

**Requirements:**

1. Create a function `load_sales_data(filename)` that:
   - Reads the CSV file using csv.DictReader
   - Converts numeric fields (Sales, Quantity, Discount, Profit) to appropriate types
   - Returns a list of dictionaries
   - Includes error handling for file not found

2. Create a function `explore_data(sales_data)` that displays:
   - Total number of orders
   - Date range (earliest and latest order)
   - List of unique regions
   - List of unique categories
   - Number of unique products

**Expected Output:**

```txt
DATASET EXPLORATION
===================
Total Orders: 1,247
Date Range: 2024-01-01 to 2024-12-31
Regions: West, East, South, Central
Categories: Technology, Furniture, Office Supplies
Unique Products: 342
```

---

#### **Part 2: Sales Performance Analysis**

**Requirements:**

1. Create `calculate_revenue_metrics(sales_data)` that returns a dictionary with:
   - Total revenue
   - Total profit
   - Total quantity sold
   - Average order value
   - Overall profit margin (profit/revenue * 100)

2. Create `analyze_by_region(sales_data)` that returns a dictionary where:
   - Keys are region names
   - Values are dictionaries with: total_sales, total_profit, order_count, avg_order_value

3. Create `analyze_by_category(sales_data)` that returns similar structure for categories

**Expected Output:**

```txt
REVENUE METRICS
===============
Total Revenue: $2,456,789.50
Total Profit: $345,678.90
Units Sold: 12,450
Average Order: $1,969.15
Profit Margin: 14.07%

REGIONAL PERFORMANCE
====================
West:    $856,234.00 | Profit: $120,456.00 | Orders: 425 | Avg: $2,014.67
East:    $723,456.00 | Profit: $95,234.00  | Orders: 389 | Avg: $1,859.78
South:   $534,123.00 | Profit: $67,890.00  | Orders: 267 | Avg: $2,000.46
Central: $342,976.50 | Profit: $62,098.90  | Orders: 166 | Avg: $2,066.03
```

---

#### **Part 3: Product Analysis**

**Requirements:**

1. Create `find_top_products(sales_data, n=10, metric='Sales')` that:
   - Aggregates data by Product_Name
   - Returns top N products based on metric (Sales, Profit, or Quantity)
   - Returns list of tuples: (product_name, metric_value)

2. Create `analyze_discounts(sales_data)` that:
   - Calculates average discount by category
   - Compares profit margin for discounted vs non-discounted items
   - Returns dictionary with insights

3. Create `identify_loss_makers(sales_data)` that:
   - Finds all orders with negative profit
   - Returns count and total loss amount
   - Lists top 5 products with most losses

**Expected Output:**

```txt
TOP 10 PRODUCTS BY SALES
========================
1. iPhone 14              $45,678.90
2. Dell Laptop            $38,234.56
3. Office Desk Pro        $32,456.78
...

DISCOUNT ANALYSIS
=================
Technology:       Avg Discount: 8.5%  | Profit Margin: 15.2%
Furniture:        Avg Discount: 12.3% | Profit Margin: 11.8%
Office Supplies:  Avg Discount: 15.6% | Profit Margin: 9.4%

Discounted Items:     Profit Margin: 10.5%
Non-Discounted Items: Profit Margin: 16.2%
Insight: Heavy discounting reduces profit margin by 5.7%

LOSS-MAKING ORDERS
==================
Total Loss Orders: 45
Total Loss Amount: -$12,345.67
Top Loss Products:
1. Premium Desk Chair: -$3,456.78
2. Conference Table: -$2,890.45
...
```

---

#### **Part 4: Report Generation**

**Requirements:**

1. Create `generate_executive_summary(sales_data, output_file)` that:
   - Calls all analysis functions
   - Writes a formatted text report to file
   - Includes all key metrics and insights

2. Create `export_regional_summary(regional_data, output_file)` that:
   - Exports regional analysis to CSV
   - Columns: Region, Total_Sales, Total_Profit, Order_Count, Avg_Order_Value, Profit_Margin

3. Create `export_top_products(sales_data, output_file, n=20)` that:
   - Exports top 20 products by sales to CSV
   - Columns: Product_Name, Category, Total_Sales, Total_Profit, Units_Sold

**Expected Files:**

- `executive_summary.txt` - Complete analysis report
- `regional_performance.csv` - Regional metrics
- `top_products.csv` - Top 20 products

---

### **Starter Code Template**

```python
"""
Superstore Sales Analysis System
Name: [Your Name]
Date: [Date]
"""

import csv
from datetime import datetime

# Part 1: Data Loading
def load_sales_data(filename):
    """Load sales data from CSV file"""
    sales_data = []
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                # Convert numeric fields
                row['Sales'] = float(row['Sales'])
                row['Quantity'] = int(row['Quantity'])
                row['Discount'] = float(row['Discount'])
                row['Profit'] = float(row['Profit'])
                
                sales_data.append(row)
        
        return sales_data
    
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return []
    except Exception as e:
        print(f"Error loading data: {e}")
        return []

def explore_data(sales_data):
    """Display dataset exploration statistics"""
    # TODO: Implement this function
    pass

# Part 2: Sales Performance
def calculate_revenue_metrics(sales_data):
    """Calculate overall revenue metrics"""
    # TODO: Implement this function
    pass

def analyze_by_region(sales_data):
    """Analyze sales performance by region"""
    # TODO: Implement this function
    pass

# Part 3: Product Analysis
def find_top_products(sales_data, n=10, metric='Sales'):
    """Find top N products by specified metric"""
    # TODO: Implement this function
    pass

# Part 4: Report Generation
def generate_executive_summary(sales_data, output_file):
    """Generate comprehensive executive summary"""
    # TODO: Implement this function
    pass

# Main execution
if __name__ == "__main__":
    # Load data
    sales_data = load_sales_data('superstore_sales.csv')
    
    if sales_data:
        print(f"Loaded {len(sales_data)} orders successfully!")
        
        # Run analyses
        explore_data(sales_data)

        # Add more function calls below
    else:
        print("Failed to load data")
```

---

## **EXERCISE 2: E-Commerce Customer Behavior Analysis**

### **Scenario**

You work as a data analyst for an e-commerce platform. The marketing team wants to understand customer purchase behavior to improve retention and increase sales. They've provided you with customer transaction data spanning 6 months.

### **Dataset**

You'll work with the `customer_transactions.csv` for this exercise

---

### **Your Tasks**

#### **Part 1: Customer Database Setup**

**Requirements:**

1. Create `load_transaction_data(filename)` that:
   - Loads CSV using csv.DictReader
   - Converts Purchase_Amount to float
   - Handles missing or invalid data
   - Returns list of transaction dictionaries

2. Create `build_customer_profiles(transactions)` that:
   - Groups transactions by Customer_ID
   - Returns dictionary: {customer_id: {...profile_data}}
   - Profile data includes: name, email, signup_date, total_transactions, total_spent

3. Create `display_customer_summary(customer_profiles)` that shows:
   - Total unique customers
   - Average transactions per customer
   - Average spend per customer
   - Customer with most transactions
   - Customer with highest total spend

**Expected Output:**

```txt
CUSTOMER DATABASE SUMMARY
=========================
Total Customers: 1,523
Average Transactions per Customer: 4.2
Average Customer Lifetime Value: $487.65
Most Active Customer: CUST-0456 (23 transactions)
Highest Spending Customer: CUST-0892 ($3,456.78)
```

---

#### **Part 2: Purchase Behavior Analysis**

**Requirements:**

1. Create `analyze_purchase_frequency(customer_profiles)` that:
   - Categorizes customers by purchase frequency:
     - One-time: 1 transaction
     - Occasional: 2-3 transactions
     - Regular: 4-6 transactions
     - Frequent: 7+ transactions
   - Returns count and percentage for each category

2. Create `calculate_customer_lifetime_value(transactions)` that:
   - Calculates CLV (Customer Life-Time Value) for each customer (total money spent)
   - Returns dictionary sorted by CLV (highest amount first)

3. Create `analyze_category_preferences(transactions)` that:
   - Finds most popular product categories (sort using the transaction_count in descending order)
   - Returns: {category: {transaction_count, total_revenue, avg_purchase}}

**Expected Output:**

```txt
PURCHASE FREQUENCY DISTRIBUTION
================================
One-time Buyers:    456 (29.9%) | Avg Spend: $156.78
Occasional Buyers:  523 (34.3%) | Avg Spend: $312.45
Regular Buyers:     389 (25.5%) | Avg Spend: $567.89
Frequent Buyers:    155 (10.2%) | Avg Spend: $1,234.56

CATEGORY PERFORMANCE
====================
Electronics:  1,234 transactions | Revenue: $456,789.00 | Avg: $370.15
Clothing:       987 transactions | Revenue: $123,456.78 | Avg: $125.08
Books:          756 transactions | Revenue: $34,567.89  | Avg: $45.72
Home & Garden:  543 transactions | Revenue: $89,012.34  | Avg: $163.95
```

---

#### **Part 3: Customer Segmentation**

**Requirements:**

1. Create `segment_customers_by_value(customer_profiles)` that segments customers by their total spend:
   - VIP: Total spend > $1000
   - High Value: Between $500 and $1000
   - Medium Value: Between $200 and $500
   - Low Value: Less than $200

2. Create `identify_at_risk_customers(transactions, days_threshold=90)` that:
   - Finds customers who haven't purchased in 90+ days
   - Calculates their previous CLV
   - Returns list of at-risk customers with potential revenue loss

3. Create `find_loyal_customers(customer_profiles, min_transactions=5)` that:
   - Identifies customers with 5+ transactions
   - Calculates their average order value
   - Returns sorted list of loyal customers (by the average order value in descending order)

**Expected Output:**

```txt
CUSTOMER VALUE SEGMENTATION
============================
VIP Customers:         87 (5.7%)  | Total Value: $123,456.78 (42.3% of revenue)
High Value:           234 (15.4%) | Total Value: $89,234.56  (30.6% of revenue)
Medium Value:         567 (37.2%) | Total Value: $56,789.01  (19.5% of revenue)
Low Value:            635 (41.7%) | Total Value: $22,345.67  (7.6% of revenue)

AT-RISK CUSTOMERS (No purchase in 90+ days)
============================================
Found 234 at-risk customers
Potential Revenue at Risk: $67,890.45
Top 5 At-Risk VIP Customers:
  1. CUST-0234: Last purchase 120 days ago | Historic CLV: $2,345.67
  2. CUST-0567: Last purchase 98 days ago  | Historic CLV: $1,890.23
  ...

LOYAL CUSTOMER BASE
===================
Total Loyal Customers: 544 (35.7%)
Average Orders per Loyal Customer: 7.8
Average Order Value: $156.78
Loyal Customer Contribution: 68.9% of total revenue
```

---

#### **Part 4: Payment and Device Analytics**

**Requirements:**

1. Create `analyze_payment_methods(transactions)` that:
   - Counts transactions by payment method
   - Calculates average purchase value by payment method
   - Returns insights on preferred payment types

2. Create `analyze_device_usage(transactions)` that:
   - Analyzes purchases by device type (Mobile, Desktop, Tablet)
   - Compares average order values across devices
   - Identifies trends

**Expected Output:**

```txt
PAYMENT METHOD ANALYSIS
========================
Credit Card:  1,234 transactions (45.6%) | Avg: $234.56
Debit Card:     890 transactions (32.9%) | Avg: $178.90
PayPal:         456 transactions (16.8%) | Avg: $156.34
Apple Pay:      123 transactions (4.5%)  | Avg: $298.12

Insight: Apple Pay users have highest average order value

DEVICE USAGE PATTERNS
======================
Mobile:   1,789 transactions (66.1%) | Avg Order: $156.78
Desktop:    756 transactions (27.9%) | Avg Order: $289.45
Tablet:     158 transactions (5.8%)  | Avg Order: $198.23

Insight: Desktop users spend 84.6% more per order than mobile users
```

---

#### **Part 5: Time-Based Patterns**

**Requirements:**

1. Create `analyze_purchase_timing(transactions)` that:
   - Groups transactions by month
   - Identifies busiest shopping months
   - Calculates month-over-month growth

2. Create `calculate_customer_retention(transactions)` that:
   - Calculates how many customers return for a second purchase
   - Tracks retention by cohort (signup month)
   - Returns retention rate

**Expected Output:**

```txt
MONTHLY PURCHASE PATTERNS
==========================
January:   234 transactions | Revenue: $45,678.90
February:  289 transactions | Revenue: $56,789.01 (23.9% growth)
March:     312 transactions | Revenue: $67,890.12 (19.5% growth)
...

CUSTOMER RETENTION ANALYSIS
============================
Overall Retention Rate: 58.7%
  - Customers who made 2nd purchase: 894 of 1,523

Cohort Retention:
  January Signups:  123 customers | 67.5% retained
  February Signups: 145 customers | 62.1% retained
  March Signups:    167 customers | 55.7% retained
```

---

#### **Part 6: Report Generation and Exports**

**Requirements:**

1. Create `generate_marketing_report(transactions, output_file)` that:
   - Compiles all insights into text report
   - Includes recommendations for marketing team
   - Saves to file

2. Create `export_customer_segments(customer_profiles, output_file)` that:
   - Exports customer segmentation to CSV
   - Columns: Customer_ID, Name, Email, Segment, Total_Spent, Transaction_Count

3. Create `export_at_risk_customers(at_risk_list, output_file)` that:
   - Creates CSV of at-risk customers for retention campaign
   - Columns: Customer_ID, Name, Email, Days_Since_Last_Purchase, Historic_CLV

**Expected Files:**

- `marketing_insights.txt` - Complete analysis with recommendations
- `customer_segments.csv` - Segmented customer list
- `retention_campaign_targets.csv` - At-risk customers for outreach

---

### **Starter Code Template**

```python
"""
E-Commerce Customer Behavior Analysis
Name: [Your Name]
Date: [Date]
"""

import csv
from datetime import datetime, timedelta

# Part 1: Data Loading
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
    """Build customer profiles from transactions"""
    # TODO: Implement this
    pass

# Part 2: Purchase Behavior
def analyze_purchase_frequency(customer_profiles):
    """Analyze how frequently customers purchase"""
    # TODO: Implement this
    pass

# Part 3: Segmentation
def segment_customers_by_value(customer_profiles):
    """Segment customers by spending level"""
    # TODO: Implement this
    pass

# Part 4: Payment Analytics
def analyze_payment_methods(transactions):
    """Analyze payment method preferences"""
    # TODO: Implement this
    pass

# Part 5: Time Analysis
def analyze_purchase_timing(transactions):
    """Analyze purchase timing patterns"""
    # TODO: Implement this
    pass

# Part 6: Report Generation
def generate_marketing_report(transactions, output_file):
    """Generate marketing insights report"""
    # TODO: Implement this
    pass

# Main execution
if __name__ == "__main__":
    transactions = load_transaction_data('customer_transactions.csv')
    
    if transactions:
        print(f"Loaded {len(transactions)} transactions!")
        
        # Build customer profiles
        profiles = build_customer_profiles(transactions)
        
        # Run analyses
        # Add your function calls here
    else:
        print("Failed to load data")
```

---

## **Getting Help:**

- Review lecture notes and in-class exercises
- Check Python documentation for functions
- Ask questions in class or office hours
- Collaborate on concepts, but write your own code

---

## **Submission Checklist**

Before submitting, ensure you have:

**Exercise 1 (Superstore):**

- [ ] `superstore_analysis.py` - Main Python file
- [ ] `Superstore_Analysis.ipynb` - Jupyter notebook
- [ ] `executive_summary.txt` - Generated report
- [ ] `regional_performance.csv` - Regional data export
- [ ] `top_products.csv` - Top products export
- [ ] `README.txt` - Brief explanation of your approach

**Exercise 2 (E-Commerce):**

- [ ] `customer_analysis.py` - Main Python file
- [ ] `Customer_Behavior_Analysis.ipynb` - Jupyter notebook
- [ ] `marketing_insights.txt` - Generated report
- [ ] `customer_segments.csv` - Segmented customers
- [ ] `retention_campaign_targets.csv` - At-risk customers
- [ ] `README.txt` - Brief explanation

---

**Good luck with your analysis! Remember, these exercises are designed to reinforce what you've learned and prepare you for working with pandas next week. Take your time, be thorough, and don't hesitate to ask questions!** 🚀📊
