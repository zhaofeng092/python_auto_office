import xlrd

xlsx = xlrd.open_workbook('d:/7月下旬入库表.xlsx')

table = xlsx.sheet_by_index(0)
# 通过sheet名查找：xlsx.sheet_by_name("7月下旬入库表")
# 通过索引查找：xlsx.sheet_by_index(3)
print(table.cell_value(0, 0))

# table.cell_value(1, 2)
# print(table.cell(1, 2).value)
# print(table.row(1)[2].value)



for i in range(0, xlsx.nsheets):
    table = xlsx.sheet_by_index(i)
    print(table.cell_value(0, 0))

# 获取所有sheet名字：xlsx.sheet_names()
# 获取sheet数量：xlsx.nsheets

for i in xlsx.sheet_names():
    table = xlsx.sheet_by_name(i)
    print(table.cell_value(3, 3))
