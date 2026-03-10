import pandas as pd

df = pd.read_csv("../data/students.csv")

# print(df.isnull().sum())

df["Geography"] = df["Geography"].fillna(df["Geography"].mean())

grouped_means = df.groupby('class_level')['Physics'].transform('mean')
df['Physics'] = df['Physics'].fillna(grouped_means)

print(grouped_means)
