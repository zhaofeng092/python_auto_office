import pandas as pd

students1 = pd.read_csv('C:/Temp/Students.csv', index_col='ID')
students2 = pd.read_csv('C:/Temp/Students.tsv', sep='\t', index_col='ID')
students3 = pd.read_csv('C:/Temp/Students.txt', sep='|', index_col='ID')

print(students1)
print(students2)
print(students3)
