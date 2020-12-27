#1、2星答案
# import xlrd,xlwt
# xlsx = xlrd.open_workbook('d:/7月下旬入库表.xlsx')
# new_workbook = xlwt.Workbook()
# worksheet = new_workbook.add_sheet('new_test')
# table = xlsx.sheet_by_index(0)
# for i in range(0,table.nrows):
#     for j in range(0,table.ncols):
#         print(table.cell_value(i, j))
#         worksheet.write(i, j, table.cell_value(i, j))
# new_workbook.save('d:/test.xls')

#3星答案
import xlrd,xlsxwriter
xlsx = xlrd.open_workbook('d:/7月下旬入库表.xlsx')
new_workbook = xlsxwriter.Workbook('d:/test.xlsx')
worksheet = new_workbook.add_worksheet()
table = xlsx.sheet_by_index(0)
for i in range(0,table.nrows):
    for j in range(0,table.ncols):
        print(table.cell_value(i, j))
        worksheet.write(i, j, table.cell_value(i, j))
new_workbook.close()
