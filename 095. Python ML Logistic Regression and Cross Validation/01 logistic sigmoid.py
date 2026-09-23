import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

z_values = np.array([-2.0, -1.0, 0.0, 1.0, 2.0])
probabilities = sigmoid(z_values)

for z, p in zip(z_values, probabilities):
    print(f"z = {z:4.1f} -> P(y=1) = {p:.4f}")
