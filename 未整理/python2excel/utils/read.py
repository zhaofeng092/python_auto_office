# -*- coding: utf-8 -*-
# @Time : 2020/4/19 21:17
# @Author : python自动化办公社区
# @File : read.py
# @Software: PyCharm
# @Description:
#               1、读取excel中的所有内容
#               2、单个文件、文件夹下所有文件

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
        name = sht.range('a2').value
        print('{}-1月的出勤率是{}'.format(name,come_rate))

        # 退出系统打开的excel
        wb.app.quit()
else:
    print('no related files')
