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

## Hands-on Exercise 1: Data Selection Challenge

**Real-world Context:**

As a data scientist working for an educational consulting firm, you've been tasked with identifying students for special academic programs based on specific criteria. This exercise simulates the kind of targeted filtering data scientists perform when creating audience segments or identifying candidates for special interventions.

**Tasks:**

1. Find all students who are in SS1 and have an attendance rate above 92%
2. Identify students who are excelling in humanities (those with both English Language and Literature in English scores above 85)
3. Find students who might need academic support (those with at least two STEM subjects below 70)
4. Create a list of potential math tutors (students with Mathematics scores above 90 in SS3)
5. Sort the dataset by average score across all subjects they've taken (you'll need to calculate this first)

**Why This Matters**:
In data analytics, the ability to precisely select subsets of data based on complex criteria is essential. School counselors might use these techniques to identify students for advanced placement courses or academic intervention programs. Marketing analysts use similar approaches to segment customers for targeted campaigns. These filtering operations are among the most commonly used tools in a data scientist's daily workflow.

## Part 2: Grouping and Aggregation

### Understanding the GroupBy Operation

The `groupby()` method in Pandas is one of its most powerful features, allowing you to split data into groups based on some criteria, apply a function to each group independently, and then combine the results.

**Real-life Analogy**:
"Think of `groupby()` like sorting a deck of playing cards by suit. You first separate all the hearts, diamonds, clubs, and spades into different piles (the grouping step). Then, you can count how many cards are in each pile, find the highest card in each pile, or calculate the average card value for each suit (the aggregation step). Finally, you can put your results together in a new, summarized format that tells you about each suit rather than each individual card."

```python
# Basic groupby with a single column
gender_groups = students_df.groupby('gender')

# Calculate mean scores for each gender
gender_performance = gender_groups[['Mathematics', 'English Language', 'Physics', 'Chemistry']].mean()
print("Average scores by gender:")
print(gender_performance)

# Multiple aggregations at once
gender_stats = gender_groups['Mathematics'].agg(['mean', 'min', 'max', 'count'])
print("\nMath statistics by gender:")
print(gender_stats)

# Group by multiple columns
level_gender_groups = students_df.groupby(['class_level', 'gender'])
level_gender_performance = level_gender_groups['Mathematics'].mean()
print("\nAverage math score by class level and gender:")
print(level_gender_performance)
```

### Common Aggregation Functions

```python
# Group by class level
class_groups = students_df.groupby('class_level')

# Count of students in each class level
print("Number of students per class level:")
print(class_groups.size())

# Mean of all numeric columns by class level
print("\nAverage values by class level:")
print(class_groups.mean())

# Custom aggregations per column
custom_agg = {
    'attendance': ['min', 'max', 'mean'],
    'Mathematics': ['mean', 'median', 'std'],
    'English Language': ['mean', 'median', 'std'],
}
class_analysis = class_groups.agg(custom_agg)
print("\nCustom aggregations by class level:")
print(class_analysis)
```

### The Split-Apply-Combine Pattern

The GroupBy operation follows what's called the "split-apply-combine" pattern:

1. **Split**: The data is split into groups based on one or more keys
2. **Apply**: A function is applied to each group independently
3. **Combine**: The results are combined into a new data structure

This pattern is extremely powerful for data analysis and is used extensively in real-world data science.

### Grouped Filtering with .filter()

```python
# Find class levels with average Mathematics scores above 80
high_math_classes = students_df.groupby('class_level').filter(
    lambda x: x['Mathematics'].mean() > 80
)
print("Class levels with math average above 80:")
print(high_math_classes['class_level'].unique())

# Find students in classes where average attendance is above 90%
good_attendance_classes = students_df.groupby('class_level').filter(
    lambda x: x['attendance'].mean() > 90
)
print("\nStudents in classes with good average attendance:")
print(good_attendance_classes[['first_name', 'last_name', 'class_level', 'attendance']].head())
```

## Hands-on Exercise 2: School Performance Analysis

**Real-world Context**:
You're working as a data analyst for a school, and the principal has requested a comprehensive analysis of student performance patterns. This analysis will inform resource allocation, curriculum development, and teacher professional development for the coming year. This exercise simulates a typical data aggregation task that data scientists perform when preparing reports for stakeholders.

**Tasks**:

1. Group the student data by class level and calculate:
   - The average score for each subject
   - The number of students in each class level
   - The minimum and maximum scores in each subject
2. Identify which class level has the:
   - Highest average attendance
   - Best overall academic performance (across all subjects)
   - Largest gender performance gap in Mathematics
3. Find out if there's a correlation between attendance and academic performance (hint: use groupby with multiple conditions)
4. Create a summary report showing the performance metrics for each class level

**Why This Matters**:
Educational administrators regularly need summary statistics to make data-driven decisions. School leaders might use these analyses to allocate resources for remedial programs, identify successful teaching practices, or spot trends that require intervention. The ability to group and aggregate data is essential for transforming detailed student records into actionable insights that can guide policy decisions.
