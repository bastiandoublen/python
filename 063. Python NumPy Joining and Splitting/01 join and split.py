import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))
print("Joined array:", arr)

arr_split = np.array_split(arr, 3)
print("Split into 3 parts:", arr_split)
