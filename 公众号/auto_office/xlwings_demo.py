# -*- coding: utf-8 -*-
# @公众号 :Python自动化办公社区
# @Software: PyCharm
# @Description: xlwings演示代码


import xlwings as xw
# wb = xw.Book()  # 新建一个文档
wb = xw.Book('test.xls')  # 打开一个已有的文档
sht = wb.sheets['Sheet1'] # 找到指定sheet
print(sht.range('A1').value) # 读取指定单元格的数据，这里读的是A1