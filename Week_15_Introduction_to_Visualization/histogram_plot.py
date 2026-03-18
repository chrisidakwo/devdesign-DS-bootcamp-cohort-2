import matplotlib.pyplot as plt
import pandas as pd

def load_students(filename: str) -> pd.DataFrame:
    df = pd.read_csv(filename)

    class_level_map = {
        10: "SS1",
        11: "SS2",
        12: "SS3"
    }

    df["English Language"] = pd.to_numeric(df["English Language"], errors="coerce")
    df["Literature in English"] = pd.to_numeric(df["Literature in English"], errors="coerce")

    #  Replaces all values. Any value for the column that's not mapped in the dictionary key, is replace with NaN (meaning an empty value)
    # df["class_level"] = df["class_level"].map(class_level_map)

    # Only replaces matched values. Does not attempt to replace values not provided in the dictionary key.
    df["class_level"] = df["class_level"].replace(class_level_map)

    return df

students_df = load_students("../data/students.csv")

# Create the figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Create a histogram of Mathematics scores
ax.hist(students_df["Mathematics"], bins=10, color="skyblue", alpha=0.7, edgecolor="black")

ax.set_title("Distribution of Mathematics Scores")
ax.set_xlabel("Score")
ax.set_ylabel("Number of Students")

ax.grid(axis="y", linestyle="--", alpha=0.7)

plt.show()