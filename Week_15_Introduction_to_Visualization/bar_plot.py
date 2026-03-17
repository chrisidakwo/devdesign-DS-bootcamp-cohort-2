import pandas as pd
import matplotlib.pyplot as plt

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

# Caculate average scrores by class level for core subjects
class_level_means = students_df.groupby("class_level")[["Mathematics", "English Language"]].mean()

fig, ax = plt.subplots(figsize=(10, 6))

class_level_means.plot(kind="bar", ax=ax)

ax.set_title("Average Score by Class Level")
ax.set_xlabel("Class Level")
ax.set_ylabel("Average Score")
ax.legend(title="Subjects")

# Add value labels on top of the bars
for container in ax.containers:
    ax.bar_label(container, fmt="%.1f", padding=3)

plt.show()
