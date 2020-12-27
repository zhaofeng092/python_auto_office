import xlrd
import xlwt
from xlutils.copy import copy
import pymysql

database = pymysql.connect("127.0.0.1", "test", "test", "db", charset='utf8')

cursor = database.cursor()

sql = "SELECT company ,COUNT(company),SUM(weight),SUM(weight*price) FROM data  GROUP BY company"
cursor.execute(sql)
result = cursor.fetchall()
# print(result)
for i in result:
    if i[0] == '张三粮配':
        a_num = i[1]
        a_weight = i[2]
        a_total_price = i[3]
    elif i[0] == '李四粮食':
        b_num = i[1]
        b_weight = i[2]
        b_total_price = i[3]
    elif i[0] == '王五小麦':
        c_num = i[1]
        c_weight = i[2]
        c_total_price = i[3]
    elif i[0] == '赵六麦子专营':
        d_num = i[1]
        d_weight = i[2]
        d_total_price = i[3]

tem_excel = xlrd.open_workbook('D:/统计表_模板.xls', formatting_info=True)
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

new_sheet.write(2, 1, a_num, style)
new_sheet.write(2, 2, a_weight, style)
new_sheet.write(2, 3, a_total_price, style)
new_sheet.write(3, 1, b_num, style)
new_sheet.write(3, 2, b_weight, style)
new_sheet.write(3, 3, b_total_price, style)
new_sheet.write(4, 1, c_num, style)
new_sheet.write(4, 2, c_weight, style)
new_sheet.write(4, 3, c_total_price, style)
new_sheet.write(5, 1, d_num, style)
new_sheet.write(5, 2, d_weight, style)
new_sheet.write(5, 3, d_total_price, style)

new_excel.save('d:/7月下旬统计表.xls')
