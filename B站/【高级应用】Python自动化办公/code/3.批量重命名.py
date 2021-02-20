# -*- coding: utf-8 -*-
# @Time : 2020/12/16 9:54
# @Author :liuzf 
# @File : filename.py
# @Software: PyCharm
# @Description:

import os

path = input('请输入文件路径(结尾加上\)：')
del_replace_content = input('请输入需要去掉的内容：')

# 获取该目录下所有文件，存入列表中
fileList = os.listdir(path)

for filename in fileList:

    if del_replace_content in filename:
        old_name = filename
        new_name = old_name.replace(del_replace_content, 'mp4')
        os.rename(path + os.sep + old_name, path + os.sep + new_name)

        print(filename)
