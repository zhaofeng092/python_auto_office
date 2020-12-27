from xlutils.copy import copy
import xlrd
import xlwt

tem_excel = xlrd.open_workbook('D:/日统计.xls', formatting_info=True)
tem_sheet = tem_excel.sheet_by_index(0)

new_excel = copy(tem_excel)
new_sheet = new_excel.get_sheet(0)

style = xlwt.XFStyle()

font = xlwt.Font()
font.name = '宋体'
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
alignment.horz = xlwt.Alignment.HORZ_LEFT
alignment.vert = xlwt.Alignment.VERT_TOP
style.alignment = alignment

style_red = xlwt.XFStyle()

font_red = xlwt.Font()
font_red.name = '宋体'
font_red.bold = True
font_red.height = 360
font_red.colour_index = 2
style_red.font = font_red

borders_red = xlwt.Borders()
borders_red.top = xlwt.Borders.THIN
borders_red.bottom = xlwt.Borders.THIN
borders_red.left = xlwt.Borders.THIN
borders_red.right = xlwt.Borders.THIN
style_red.borders = borders_red

alignment_red = xlwt.Alignment()
alignment_red.horz = xlwt.Alignment.HORZ_LEFT
alignment_red.vert = xlwt.Alignment.VERT_TOP
style_red.alignment = alignment_red

style_lishu18 = xlwt.XFStyle()

font_lishu18 = xlwt.Font()
font_lishu18.name = '隶书'
font_lishu18.bold = True
font_lishu18.height = 360
style_lishu18.font = font_lishu18

borders_lishu18 = xlwt.Borders()
borders_lishu18.top = xlwt.Borders.THIN
borders_lishu18.bottom = xlwt.Borders.THIN
borders_lishu18.left = xlwt.Borders.THIN
borders_lishu18.right = xlwt.Borders.THIN
style_lishu18.borders = borders_lishu18

alignment_lishu18 = xlwt.Alignment()
alignment_lishu18.horz = xlwt.Alignment.HORZ_CENTER
alignment_lishu18.vert = xlwt.Alignment.VERT_CENTER
style_lishu18.alignment = alignment_lishu18

style_lishu22 = xlwt.XFStyle()

font_lishu22 = xlwt.Font()
font_lishu22.name = '隶书'
font_lishu22.bold = True
font_lishu22.height = 440
style_lishu22.font = font_lishu22

borders_lishu22 = xlwt.Borders()
borders_lishu22.top = xlwt.Borders.THIN
borders_lishu22.bottom = xlwt.Borders.THIN
borders_lishu22.left = xlwt.Borders.THIN
borders_lishu22.right = xlwt.Borders.THIN
style_lishu22.borders = borders_lishu22

alignment_lishu22 = xlwt.Alignment()
alignment_lishu22.horz = xlwt.Alignment.HORZ_CENTER
alignment_lishu22.vert = xlwt.Alignment.VERT_CENTER
style_lishu22.alignment = alignment_lishu22

zhangsan_num = int(input('请输入张三粮配入库量：'))
lisi_num = int(input('请输入李四粮食入库量：'))
wangwu_num = int(input('请输入王五小麦入库量：'))
zhaoliu_num = int(input('请输入赵六麦子专营入库量：'))


stylex = lambda x: style_red if x > 10 else style


new_sheet.write(0, 0, tem_sheet.cell_value(0, 0), style_lishu22)
new_sheet.write(1, 0, tem_sheet.cell_value(1, 0), style_lishu18)
new_sheet.write(1, 1, tem_sheet.cell_value(1, 1), style_lishu18)
new_sheet.write(2, 0, tem_sheet.cell_value(2, 0), style_lishu18)
new_sheet.write(3, 0, tem_sheet.cell_value(3, 0), style_lishu18)
new_sheet.write(4, 0, tem_sheet.cell_value(4, 0), style_lishu18)
new_sheet.write(5, 0, tem_sheet.cell_value(5, 0), style_lishu18)





new_sheet.write(2, 1, zhangsan_num, stylex(zhangsan_num))
new_sheet.write(3, 1, lisi_num, stylex(lisi_num))
new_sheet.write(4, 1, wangwu_num, stylex(wangwu_num))
new_sheet.write(5, 1, zhaoliu_num, stylex(zhaoliu_num))


new_excel.save('D:/填写.xls')
