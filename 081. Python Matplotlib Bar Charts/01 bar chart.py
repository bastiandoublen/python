import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color="#4CAF50")
plt.savefig("bar_chart.png")
print("Bar chart saved to bar_chart.png.")
