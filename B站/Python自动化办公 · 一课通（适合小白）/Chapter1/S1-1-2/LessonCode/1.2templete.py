from xlutils.copy import copy
import xlrd
import xlwt

tem_excel = xlrd.open_workbook('D:/日统计.xls', formatting_info=True)
tem_sheet = tem_excel.sheet_by_index(0)

new_excel = copy(tem_excel)
new_sheet = new_excel.get_sheet(0)

style = xlwt.XFStyle()

font = xlwt.Font()
font.name = '微软雅黑'
font.bold = True
font.height = 360
style.font = font

borders = xlwt.Borders()
borders.top = xlwt.Borders.THIN
borders.bottom = xlwt.Borders.THIN
borders.left = xlwt.Borders.THIN
borders.right = xlwt.Borders.THIN
style.borders = borders

alignment = xlwt.Alignment()
alignment.horz = xlwt.Alignment.HORZ_CENTER
alignment.vert = xlwt.Alignment.VERT_CENTER
style.alignment = alignment

"""
new_sheet.write(2, 1, 12)
new_sheet.write(3, 1, 18)
new_sheet.write(4, 1, 19)
new_sheet.write(5, 1, 15)
"""

new_sheet.write(2, 1, 12, style)
new_sheet.write(3, 1, 18, style)
new_sheet.write(4, 1, 19, style)
new_sheet.write(5, 1, 15, style)


new_excel.save('D:/填写.xls')
