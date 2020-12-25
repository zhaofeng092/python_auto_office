# -*- coding: utf-8 -*-
# @Time : 2020/5/20 17:00
# @Author : lzf
# @File : xlwings读取任一个单元格.py
# @Software: PyCharm
# @Description:

# -*- coding: utf-8 -*-
# @Time : 2020/4/19 21:17
# @Author : python自动化办公社区
# @File : read.py
# @Software: PyCharm
# @Description:
#               1、读取excel中任意内容（win/mac通用）

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
        print(sht)
        v = sht.range('b1').value
        print(v)

        # 退出系统打开的excel
        wb.app.quit()
else:
    print('no related files')
