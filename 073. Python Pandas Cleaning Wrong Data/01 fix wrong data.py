import pandas as pd

data = {
  "Duration": [60, 60, 450, 45],
  "Calories": [409.1, 479.0, 340.0, 282.4]
}
df = pd.DataFrame(data)

for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.loc[x, "Duration"] = 120

print("Cleaned DataFrame:\n", df)
