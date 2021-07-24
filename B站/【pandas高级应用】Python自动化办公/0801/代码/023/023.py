import pandas as pd
from datetime import date

orders = pd.read_excel('C:/Temp/Orders.xlsx', dtype={'Date': date})
orders['Year'] = pd.DatetimeIndex(orders.Date).year
groups = orders.groupby(['Category', 'Year'])
s = groups['Total'].sum()
c = groups['ID'].count()
pt1 = pd.DataFrame({'Sum': s, 'Count': c})
pt2 = orders.pivot_table(index='Category', columns='Year', values='Total', aggfunc=np.sum)

print(pt1)
print(pt2)
