import numpy as np

actual = np.array([1, 0, 0, 1, 0, 0, 1, 0, 0, 1])
predicted = np.array([1, 0, 0, 1, 0, 0, 0, 1, 0, 0])

tp = np.sum((actual == 1) & (predicted == 1))
tn = np.sum((actual == 0) & (predicted == 0))
fp = np.sum((actual == 0) & (predicted == 1))
fn = np.sum((actual == 1) & (predicted == 0))

accuracy = (tp + tn) / len(actual)
print(f"Confusion Matrix -> TP: {tp}, TN: {tn}, FP: {fp}, FN: {fn}")
print("Accuracy:", accuracy)
