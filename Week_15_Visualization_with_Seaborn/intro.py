import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.set_style("whitegrid")

ALL_SUBJECTS = [
    "Agriculture", "Geography", "French", "Economics", "Biology", "Igbo", "History", "Physics", "Chemistry",
    "Further Mathematics", "Civic Education", "Computer Science", "Hausa", "English Language", "Government", "Mathematics",
    "Yoruba", "Literature in English"
]

def load_students(filename: str) -> pd.DataFrame:
    df = pd.read_csv(filename)

    class_level_map = {
        10: "SS1",
        11: "SS2",
        12: "SS3"
    }

    #  Replaces all values. Any value for the column that's not mapped in the dictionary key, is replace with NaN (meaning an empty value)
    # df["class_level"] = df["class_level"].map(class_level_map)

    # Only replaces matched values. Does not attempt to replace values not provided in the dictionary key.
    df["class_level"] = df["class_level"].replace(class_level_map)

    df["total_score"] = df[ALL_SUBJECTS].mean(axis=1).round(1)

    return df


students_df = load_students("../data/students.csv")



# ====================================================
# ========== HISTOGRAM PLOT
# ====================================================

# plt.figure(figsize=(12, 6))
#
# sns.histplot(students_df["Mathematics"], kde=True, color="skyblue")
#
# plt.title("Distribution of Mathematics Scores", fontsize=16)
# plt.xlabel("Mathematics Score", fontsize=12)
# plt.ylabel("No. of Students", fontsize=12)
#
# plt.show()


# ====================================================
# ========== BOX PLOT
# ====================================================

# plt.figure(figsize=(12, 6))

# Create a box plot for core subjects by class level
# sns.boxplot(x='class_level', y='value', hue='variable',
#             data=pd.melt(students_df,
#                          id_vars=['student_id', 'class_level'],
#                          value_vars=['Mathematics', 'English Language', 'Physics', 'Chemistry', 'Biology'],
#                          var_name='variable'))
#
# # Add labels and title
# plt.title('Score Distribution by Subject and Class Level', fontsize=15)
# plt.xlabel('Class Level', fontsize=12)
# plt.ylabel('Score', fontsize=12)
# plt.legend(title='Subject')
#
# # Display the plot
# plt.show()

# ====================================================
# ========== VIOLIN PLOT
# ====================================================
# plt.figure(figsize=(14, 7))
#
# # Create a violin plot for Mathematics scores by gender and class level
# sns.violinplot(x='class_level', y='Mathematics', hue='gender',
#                data=students_df, split=True, inner='quart', palette='Set2')
#
# # Add labels and title
# plt.title('Mathematics Score Distribution by Class Level and Gender', fontsize=15)
# plt.xlabel('Class Level', fontsize=12)
# plt.ylabel('Mathematics Score', fontsize=12)
# plt.legend(title='Gender')
#
# # Display the plot
# plt.show()


# ====================================================
# ========== COUNT PLOT
# ====================================================
# plt.figure(figsize=(12, 6))
#
# # Create a count plot for class level by gender
# sns.countplot(x='class_level', hue='gender', data=students_df, palette='Set1')
#
# # Add labels and title
# plt.title('Number of Students by Class Level and Gender', fontsize=15)
# plt.xlabel('Class Level', fontsize=12)
# plt.ylabel('Count', fontsize=12)
# plt.legend(title='Gender')
#
# # Add count labels on top of bars
# for p in plt.gca().patches:
#     plt.gca().annotate(f'{int(p.get_height())}',
#                       (p.get_x() + p.get_width() / 2., p.get_height()),
#                       ha='center', va='bottom', fontsize=11)
#
# # Display the plot
# plt.show()


corr_columns = ['Mathematics', 'English Language', 'Physics', 'Chemistry',
                'Biology', 'attendance', 'disciplinary_count']
corr_matrix = students_df[corr_columns].corr()

# Create a figure
plt.figure(figsize=(12, 10))

# Create a heatmap
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f',
            linewidths=0.5, vmin=-1, vmax=1)

# Add a title
plt.title('Correlation Matrix of Academic Performance Variables', fontsize=15, pad=20)

# Display the plot
plt.tight_layout()
plt.show()