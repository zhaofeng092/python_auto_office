# -*- coding: utf-8 -*-
# @Time : 2020/4/19 21:17
# @Author : python自动化办公社区
# @File : read.py
# @Software: PyCharm
# @Description:
#               1、生成excel表格
#               2、生成指定名称的sheet

import xlwings


# 创建excel表格
def createExcel(excel_name):
    excelApp = xlwings.App(False, False)
    excelFile = excelApp.books.add()
    excelFile.save(excel_name)
    excelFile.close()
    excelApp.quit()


# 给excel表格增加sheet
def addSheet(excel_name):
    excelApp = xlwings.App(False, False)
    excelFile = excelApp.books.add()
    excelFile.sheets.add("test")
    excelFile.save("1.xlsx")


if __name__ == '__main__':
    # 生成100个excel文件
    from _datetime import  datetime
    start = datetime.now()
    for i in range(1, 13):
        excel_name = "d:\\test\\{}.xlsx".format(i)
        createExcel(excel_name)
    end = datetime.now()  # 获取当前时间
    res = (end - start).seconds  # 两个时间差，并以秒显示出来
    print(res)

    # addSheet(excel_name)
