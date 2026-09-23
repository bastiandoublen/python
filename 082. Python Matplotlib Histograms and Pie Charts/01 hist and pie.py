import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels=mylabels, startangle=90)
plt.savefig("pie_chart.png")
print("Pie chart saved to pie_chart.png.")
