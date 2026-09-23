from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x_val):
    return slope * x_val + intercept

speed_pred = myfunc(10)
print("R-squared correlation:", r**2)
print("Predicted speed for age 10:", speed_pred)
