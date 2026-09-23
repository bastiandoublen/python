import numpy as np

np.random.seed(2)
x = np.random.normal(3, 1, 100)
y = np.random.normal(150, 40, 100) / x

train_x, test_x = x[:80], x[80:]
train_y, test_y = y[:80], y[80:]

print("Training set size:", len(train_x))
print("Testing set size:", len(test_x))
