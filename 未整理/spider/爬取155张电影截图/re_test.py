# -*- coding: utf-8 -*-
# @Time : 2020/5/3 11:24
# @Author : lzf
# @File : re_test.py
# @Software: PyCharm
# @Description:

#
# !/usr/bin/python3
import re
def get_num(content):
    phone = content #我是测试你好啊2004-959-559abc # 这是一个电话号码
    # 删除注释
    # num = re.sub(r'#.*$', "", phone)
    # print("电话号码 : ", num)

    # 移除非数字的内容
    num = re.sub(r'\D', "", phone)
    print("数字 : ", num)
#
# get_num('我是李佳琪999')
# get_num('我是测试你好啊2004-959-559abc # 这是一个电话号码')
#
# phone = '我是李佳琪999'  # 我是测试你好啊2004-959-559abc # 这是一个电话号码
# num = re.sub(r'\D', "", phone)
# print("数字 : ", num)
#
# phone = '我是测试你好啊2004-959-559abc # 这是一个电话号码'  # 我是测试你好啊2004-959-559abc # 这是一个电话号码
# num = re.sub(r'\D', "", phone)
# print("数字 : ", num)
#

# for i in range(1,6):
#     print(i)

html = 'class=fd '
pattern = re.compile(
    r'.*?class=.*?',
    re.S)
image_url = re.findall(r'.*?class=.*?', html)
print(image_url)