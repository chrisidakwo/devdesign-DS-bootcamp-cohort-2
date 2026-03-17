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

ss1_math = students_df[students_df["class_level"] == "SS1"]["Mathematics"]
ss2_math = students_df[students_df["class_level"] == "SS2"]["Mathematics"]
ss3_math = students_df[students_df["class_level"] == "SS3"]["Mathematics"]

# Create a figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Create a line representing the distribution of math scores
ax.plot(range(len(ss1_math)), sorted(ss1_math), label="SS1", color="blue")
ax.plot(range(len(ss2_math)), sorted(ss2_math), label="SS2", color="green")
ax.plot(range(len(ss3_math)), sorted(ss3_math), label="SS3", color="red")

# Add labels and title
ax.set_title("Distribution of Mathematics Scores by Class Level")
ax.set_ylabel("Mathematics")
ax.set_xlabel("Student Rank")
ax.legend()

# Display the plot
plt.show()

