import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("Shape:", arr.shape)

arr1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr1d.reshape(4, 3)
print("Reshaped (4, 3):\n", newarr)
