import numpy as np

arr = np.array([41, 42, 43, 44])

filter_arr = arr > 42
newarr = arr[filter_arr]

print("Filter condition (> 42):", filter_arr)
print("Filtered array:", newarr)
