import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.max_columns = 999
homes = pd.read_excel('C:/Temp/home_data.xlsx')
print(homes.head())
# print(homes.corr())
# homes.plot.scatter(x='sqft_living', y='price')
# homes.sqft_living.plot.kde()
homes.sqft_living.plot.hist(bins=100)
plt.xticks(range(0, max(homes.sqft_living), 500), fontsize=8, rotation=90)
# homes.price.plot.hist(bins=200)
# plt.xticks(range(0, max(homes.price), 100000), fontsize=8, rotation=90)
plt.show()
