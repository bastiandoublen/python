import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker='o', linestyle='dashed', color='r')
plt.savefig("markers_line.png")
print("Line & marker plot saved to markers_line.png.")
