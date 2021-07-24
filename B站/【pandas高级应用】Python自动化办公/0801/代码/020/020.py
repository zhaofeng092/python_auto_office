import pandas as pd

students = pd.read_excel('C:/Temp/Students_Duplicates.xlsx')
dupe = students.duplicated(subset='Name')
dupe = dupe[dupe == True]  # dupe = dupe[dupe]
print(students.iloc[dupe.index])
print("=========")
students.drop_duplicates(subset='Name', inplace=True, keep='last')
print(students)
