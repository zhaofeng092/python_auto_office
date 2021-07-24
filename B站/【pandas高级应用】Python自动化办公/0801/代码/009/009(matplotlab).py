import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel('C:/Temp/Students.xlsx')
students.sort_values(by='Number', inplace=True, ascending=False)
students.index = range(0, len(students))
print(students)

plt.bar(students['Field'], students['Number'], color='orange', width=0.7)
plt.xticks(students['Field'], rotation='90')
plt.title('International Student by Field', fontsize=16)
plt.xlabel('Field')
plt.ylabel('Number')
plt.tight_layout()
plt.show()
