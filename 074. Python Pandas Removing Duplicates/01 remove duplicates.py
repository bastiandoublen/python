import pandas as pd

data = {
  "Name": ["John", "Anna", "John", "Peter"],
  "Age": [28, 24, 28, 35]
}
df = pd.DataFrame(data)

print("Duplicates check:\n", df.duplicated())
df_cleaned = df.drop_duplicates()
print("\nAfter drop_duplicates():\n", df_cleaned)
