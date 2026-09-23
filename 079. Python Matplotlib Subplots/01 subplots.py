import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.subplot(1, 2, 1)
plt.plot(np.array([0, 1, 2, 3]), np.array([3, 8, 1, 10]))
plt.title("SALES")

plt.subplot(1, 2, 2)
plt.plot(np.array([0, 1, 2, 3]), np.array([10, 20, 30, 40]))
plt.title("INCOME")

plt.suptitle("MY SHOP")
plt.savefig("subplots.png")
print("Subplots saved to subplots.png.")
