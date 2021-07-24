import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel('C:/Temp/Students.xlsx')
students.sort_values(by='2017', inplace=True, ascending=False)
print(students)
students.plot.bar('Field', ['2016', '2017'], color=['orange', 'Red'])
plt.title('International Students by Field', fontsize=16)
plt.xlabel('Field', fontweight='bold')
plt.ylabel('Number', fontweight='bold')
# plt.tight_layout()
ax = plt.gca()
ax.set_xticklabels(students['Field'], rotation=40, ha='right')
plt.gcf().subplots_adjust(left=0.2, bottom=0.42)
plt.show()
