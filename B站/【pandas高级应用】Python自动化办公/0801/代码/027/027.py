import pandas as pd

page_001 = pd.read_excel('C:/Temp/Students.xlsx', sheet_name='Page_001')
page_002 = pd.read_excel('C:/Temp/Students.xlsx', sheet_name='Page_002')

# 追加已有
students = page_001.append(page_002).reset_index(drop=True)

# 追加新建
stu = pd.Series({'ID': 41, 'Name': 'Abel', 'Score': 90})
students = students.append(stu, ignore_index=True)

# 删除（可切片）
students = students.drop(index=[39, 40])

# 插入
stu = pd.Series({'ID': 100, 'Name': 'Bailey', 'Score': 100})
part1 = students[:21]  # .iloc[] is the same
part2 = students[21:]
students = part1.append(stu, ignore_index=True).append(part2).reset_index(drop=True)

# 更改
stu = pd.Series({'ID': 101, 'Name': 'Danni', 'Score': 101})
students.iloc[39] = stu

# 设置空值
for i in range(5, 15):
    students['Name'].at[i] = ''

# 去掉空值
missing = students.loc[students['Name'] == '']
students.drop(missing.index, inplace=True)

print(students)
