from scipy.stats import ttest_ind
import numpy as np

v1 = np.random.normal(size=100)
v2 = np.random.normal(size=100)

res = ttest_ind(v1, v2)
print("Two-sample T-test p-value:", res.pvalue)
