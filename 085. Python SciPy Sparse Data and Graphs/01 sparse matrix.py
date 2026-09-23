import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
print("CSR Matrix representation:\n", csr_matrix(arr))
