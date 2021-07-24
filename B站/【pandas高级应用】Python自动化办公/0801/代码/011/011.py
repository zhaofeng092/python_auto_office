import pandas as pd
import matplotlib.pyplot as plt

users = pd.read_excel('C:/Temp/Users.xlsx')
users['Total'] = users['Oct'] + users['Nov'] + users['Dec']
users.sort_values(by='Total', inplace=True, ascending=False)
print(users)

users.plot.bar(x='Name', y=['Oct', 'Nov', 'Dec'], stacked=True)
plt.tight_layout()
plt.show()
