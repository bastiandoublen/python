import numpy as np

X = np.array([[1, 2], [1, 4], [1, 0], [10, 2], [10, 4], [10, 0]])
centroids = np.array([[1, 1], [10, 1]])

distances = np.linalg.norm(X[:, np.newaxis] - centroids, axis=2)
labels = np.argmin(distances, axis=1)

print("Data Points:\n", X)
print("Cluster assignments for K=2:", labels)
