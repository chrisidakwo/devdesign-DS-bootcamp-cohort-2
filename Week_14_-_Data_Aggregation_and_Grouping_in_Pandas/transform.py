import pandas as pd

df = pd.read_csv("../data/students.csv")

result_a = df.groupby("class_level")["Mathematics"].mean()
print("\n")
print(result_a)
print("\n" + "="*50 + "\n")

df["maths_mean"] = df.groupby("class_level")["Mathematics"].transform("mean").round(2)

df["distance_from_class_avg"] = (df["Mathematics"] - df["maths_mean"]).round(2)

print(df[["student_id", "class_level", "Mathematics", "maths_mean", "distance_from_class_avg"]])

print("\n")

# Using custom functions wuth the transform()
def percentile_rank(x):
    return x.rank(pct=True) * 100

df['math_percentile'] = df.groupby('class_level')['Mathematics'].transform(percentile_rank).round(0)

print(df[["student_id", "class_level", "Mathematics", "math_percentile"]].head(40))