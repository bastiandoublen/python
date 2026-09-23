import pandas as pd

data = {
  "Duration": [60, 60, 60, 45, 45],
  "Pulse": [110, 117, 103, 109, 117],
  "Maxpulse": [130, 145, 135, 175, 148],
  "Calories": [409.1, 479.0, 340.0, 282.4, 406.0]
}
df = pd.DataFrame(data)
df.to_csv("sample_data.csv", index=False)

loaded_df = pd.read_csv("sample_data.csv")
print("Loaded CSV Head:\n", loaded_df.head(3))
