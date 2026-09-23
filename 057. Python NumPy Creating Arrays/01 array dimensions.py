import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print("0-D dimension:", a.ndim)
print("1-D dimension:", b.ndim)
print("2-D dimension:", c.ndim)
print("3-D dimension:", d.ndim)
