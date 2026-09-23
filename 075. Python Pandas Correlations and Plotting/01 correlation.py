import pandas as pd

data = {
  "Duration": [60, 60, 60, 45, 45, 60],
  "Pulse": [110, 117, 103, 109, 117, 102],
  "Calories": [409, 479, 340, 282, 406, 300]
}
df = pd.DataFrame(data)

print("Correlation Matrix:\n", df.corr())
