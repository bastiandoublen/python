import numpy as np

arr_int = np.array([1, 2, 3, 4])
arr_str = np.array(['apple', 'banana', 'cherry'])

print("Integer dtype:", arr_int.dtype)
print("String dtype:", arr_str.dtype)

arr_float = arr_int.astype('f')
print("Converted to float:", arr_float.dtype)
