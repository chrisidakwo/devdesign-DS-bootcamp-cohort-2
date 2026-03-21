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

#  Create a scatter plot of Mathematics vs English Language scores
ax.scatter(
    students_df[students_df["class_level"] == "SS1"].iloc[0:100]["Mathematics"],
    students_df[students_df["class_level"] == "SS1"].iloc[0:100]["English Language"],
    c=students_df[students_df["class_level"] == "SS1"].iloc[0:100]["attendance"],
    cmap="viridis" # color palette
)

# Add labels and title
ax.set_title("Mathematics vs English Language Scores (colored by attendance)")
ax.set_xlabel("Mathematics Scores")
ax.set_ylabel("English Language Scores")

# Add a color bar to show what each color represent
cbar = plt.colorbar(ax.collections[0], ax=ax)
cbar.set_label("Attendance Rate (%)")

# Display the plot
plt.show()
