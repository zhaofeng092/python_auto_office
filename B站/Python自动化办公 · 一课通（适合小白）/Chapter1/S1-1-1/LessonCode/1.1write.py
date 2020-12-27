import xlwt
new_workbook = xlwt.Workbook()
worksheet = new_workbook.add_sheet('new_test')
worksheet.write(0, 0, 'test')
new_workbook.save('d:/test.xls')