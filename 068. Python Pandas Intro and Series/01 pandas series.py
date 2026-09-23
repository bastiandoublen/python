import pandas as pd

a = [1, 7, 2]
myvar = pd.Series(a, index=["x", "y", "z"])

print("Pandas Series:\n", myvar)
print("Value at index y:", myvar["y"])
