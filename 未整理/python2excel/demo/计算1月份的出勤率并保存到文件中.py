# -*- coding: utf-8 -*-
# @Time : 2020/4/25 23:39
# @Author : 添加微信:hdylw1024
# @File : 计算1月份的出勤率并保存到文件中.py
# @Software: PyCharm
# @Description:


import glob
import xlwings as xw

# 读取文件夹下所有的excel文档
x = glob.glob(r'D:\test\*.xls*')
# 是否有excel文档
if len(x):
    print(x)
    # 遍历excel文档
    for y in x:
        # 生成文件对象
        wb = xw.Book(y)
        # 读取指定的sheet
        sht = wb.sheets[0]
        # 读取小王当月的所有数据
        day_list = []
        flag_list = ['b','c','d','e','f','g','h','i','j','k']
        for f in flag_list:
            # 读取指定的单元格
            flag_i = '{}2'.format(f)
            day_list.append(sht.range(flag_i).value)
        # 打印数据到控制台
        print(day_list)
        num = day_list.count(200.0)
        come_rate = num/len(day_list)

        import pandas as pd

        file = 'd:\\test\\res.xlsx'

        df = pd.DataFrame([[come_rate, 0.6], [1, 1]],
                          columns=['1', '2'],
                          index=['小王', '小李'])
        wb_write = xw.Book()
        sheet = wb_write.sheets['Sheet1']
        sheet.range('A1').value = df
        # sheet.range('A1').options(pd.DataFrame,expand='table').value
        wb_write.save(path=file)
        # 没有close，会出现最后一个文件打开未关闭的问题
        wb_write.close()


        # 退出系统打开的excel
        wb.app.quit()
else:
    print('no related files')