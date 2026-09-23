import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)
print("Indexes where value is 4:", x[0])

arr_unsorted = np.array([3, 2, 0, 1])
print("Sorted array:", np.sort(arr_unsorted))
