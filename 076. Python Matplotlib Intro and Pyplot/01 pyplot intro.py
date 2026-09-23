import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.savefig("plot_sample.png")
print("Matplotlib Version:", matplotlib.__version__)
print("Plot generated and saved to plot_sample.png successfully.")
