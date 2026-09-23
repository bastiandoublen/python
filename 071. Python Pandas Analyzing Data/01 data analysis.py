import pandas as pd

data = {
  "Pulse": [110, 117, 103, 109, 117, 102, 110, 104],
  "Calories": [409.1, 479.0, 340.0, 282.4, 406.0, 300.0, 374.0, 253.3]
}
df = pd.DataFrame(data)

print("Statistical Summary:\n", df.describe())
print("\nInfo Summary:")
df.info()
