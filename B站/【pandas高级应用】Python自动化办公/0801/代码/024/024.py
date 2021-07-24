import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

sales = pd.read_excel('C:/Temp/Sales.xlsx', dtype={'Month': str, 'Revenue': float})
print(sales)

slope, intercept, r_value, p_value, std_err = linregress(sales.index, sales.Revenue)
exp = sales.index * slope + intercept

plt.scatter(sales.index, sales.Revenue)
plt.plot(sales.index, exp, color='red')
plt.xticks(sales.index, sales.Month, rotation=90)
plt.show()
