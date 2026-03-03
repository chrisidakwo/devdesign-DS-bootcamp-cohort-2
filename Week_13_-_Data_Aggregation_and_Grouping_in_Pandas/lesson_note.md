# Week 13: Data Aggregation and Grouping in Pandas

## Learning Objectives

By the end of this lesson, you will be able to:

1. Master essential data manipulation techniques in Pandas (sorting, filtering, selecting)
2. Understand and apply grouping and aggregation methods to analyze data by categories
3. Apply functions to transform and clean data efficiently
4. Handle missing data appropriately
5. Create informative summaries of grouped data
6. Extract valuable insights from (educational performance) data

## Introduction

In our previous lesson, we introduced Pandas and the basics of Pandas. Today, we'll dive deeper into Pandas' powerful data manipulation capabilities, focusing on techniques that allow us to summarize, group, and analyze data in meaningful ways.

Real data scientists spend a significant portion of their time preparing, cleaning, and transforming data. The skills you'll learn today are essential for turning raw data into actionable insights, which is at the core of any data science project.

## Part 1: Advanced Data Selection and Filtering

### Before we start

- Setup virtual environment

### Recap: Basic Data Access in Pandas

```python
import pandas as pd
import numpy as np

# Load the Nigerian students dataset
students_df = pd.read_csv('students.csv')
# Hint: See the data folder for the students.csv file

# Basic selection methods
print("First 5 rows:")
print(students_df.head())

# Selecting specific columns
scores = students_df[['English Language', 'Mathematics', 'Physics', 'Chemistry', 'Biology']]
print("\nScore columns only:")
print(scores.head())
```

### Sorting Data

```python
# Sort by a single column (Mathematics scores from highest to lowest)
sorted_by_math = students_df.sort_values('Mathematics', ascending=False)
print("Top math students:")
print(sorted_by_math[['first_name', 'last_name', 'Mathematics']].head())

# Sort by multiple columns (class level, then Mathematics score)
sorted_multi = students_df.sort_values(['class_level', 'Mathematics'], ascending=[True, False])
print("\nSorted by class level, then Mathematics score:")
print(sorted_multi[['class_level', 'first_name', 'last_name', 'Mathematics']].head())
```

### Advanced Filtering with Multiple Conditions

```python
# Filter with multiple conditions using logical operators
high_performers = students_df[(students_df['Mathematics'] > 85) & (students_df['Physics'] > 75)]
print("Students with 85+ in Mathematics and 75+ in Physics:")
print(high_performers[['first_name', 'last_name', 'Mathematics', 'Physics']].head())

# Students who excel in either Mathematics OR English Language
maths_or_english = students_df[(students_df['Mathematics'] > 90) | (students_df['English Language'] > 90)]
print("\nStudents with 90+ in either Mathematics or English Language:")
print(maths_or_english[['first_name', 'last_name', 'Mathematics', 'English Language']].head())

# Using query() method for more readable filtering
science_experts = students_df.query('Chemistry >= 85 and class_level == "SS2"')
print("\nSS2 students with 85+ in Chemistry:")
print(science_experts[['first_name', 'last_name', 'Chemistry']].head())
```

### Using .loc and .iloc for Precise Data Selection

```python
# .loc - Label-based indexing
# Select rows with index labels 0, 1, 2 and columns 'first_name', 'last_name'
print(students_df.loc[0:2, ['first_name', 'last_name']])

# .iloc - Integer-based indexing
# Select rows 0, 1, 2 and columns 0, 1
print(students_df.iloc[0:3, 0:2])

# Combining .loc with conditions
girls_ss2 = students_df.loc[(students_df['gender'] == 'F') & 
                            (students_df['class_level'] == 11)]
print("\nGirls in SS2:")
print(girls_ss2[['first_name', 'last_name']].head())
```
