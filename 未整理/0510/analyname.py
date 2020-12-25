# -*- coding: utf-8 -*-
# @Time : 2020/5/10 16:55
# @Author : lzf
# @File : analyname.py
# @Software: PyCharm
# @Description: 解析公号介绍



# import xlwings as xw
# import pandas as pd
#
#
#
# file = 'd:\\test\\res.xlsx'
#
# df = pd.DataFrame([[0.4, 0.6], [1, 1]],
#                   columns=['1', '2'],
#                   index=['小王', '小李'])
# wb = xw.Book()
# sheet = wb.sheets['Sheet1']
# sheet.range('A1').value = df
# # sheet.range('A1').options(pd.DataFrame,expand='table').value
# wb.save(path=file)
# # 没有close，会出现最后一个文件打开未关闭的问题
# wb.close()

content = input()
if '公号名称' in content and '标签' in content:
    f = open('name.txt','a+',encoding='utf-8')
    f.write(content)
    f.write('\n')
    f.write('\n')
    f.write('\n')
    f.close()