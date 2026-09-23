import numpy as np

X = np.array([
    [1, 1000, 1.0],
    [1, 1200, 1.2],
    [1, 1500, 1.4],
    [1, 1800, 1.6]
])
y = np.array([90, 105, 120, 140])

beta = np.linalg.inv(X.T @ X) @ X.T @ y
print("Coefficients [Intercept, Weight, Volume]:", beta)
