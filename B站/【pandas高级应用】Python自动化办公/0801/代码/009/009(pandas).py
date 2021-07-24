import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel('C:/Temp/Students.xlsx')
students.sort_values('Number', inplace=True, ascending=False)
print(students)
students.plot.bar(x='Field', y='Number', color='blue', title='International Students by Field')
plt.tight_layout()
plt.show()
