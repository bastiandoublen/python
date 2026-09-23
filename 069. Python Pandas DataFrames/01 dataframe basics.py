import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data)
print("DataFrame:\n", df)
print("\nRow at index 0:\n", df.loc[0])
