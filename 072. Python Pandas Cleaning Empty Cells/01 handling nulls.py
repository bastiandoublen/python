import pandas as pd
import numpy as np

data = {
  "Name": ["John", "Anna", "Peter", "Linda"],
  "Age": [28, np.nan, 35, 32],
  "Salary": [50000, 60000, np.nan, 75000]
}
df = pd.DataFrame(data)

print("Original with NaNs:\n", df)

df_filled = df.copy()
df_filled["Age"] = df_filled["Age"].fillna(df_filled["Age"].mean())
print("\nAfter filling Age NaN:\n", df_filled)
