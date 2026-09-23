import numpy as np

x = np.random.uniform(0.0, 5.0, 250)
print("Mean of uniform distribution:", np.mean(x))

y = np.random.normal(5.0, 1.0, 1000)
print("Mean of normal distribution:", np.mean(y))
