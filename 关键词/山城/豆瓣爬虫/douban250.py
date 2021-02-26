# -*- coding: utf-8 -*-
# @Time : 2021/2/26 8:24
# @File : 0226豆瓣爬虫.py
# @Software: PyCharm
# @Description: 豆瓣250爬虫

# 导入爬虫需要的库
import requests
from bs4 import BeautifulSoup
# 设置翻页的初始变量
start=0
for n in range(0,10):
    # 伪装请求头
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
    }
    # 获取页面信息
    html=requests.get('https://movie.douban.com/top250?start='+str(start),headers = headers).content
    start+=25
    # 转换为bs4格式
    soup = BeautifulSoup(html, 'html.parser')
    # 循环取出bs4中的目标数据
    for item in soup.find_all('div',"info"):
        title=item.div.a.span.string #获取标题
        yearline=item.find('div','bd').p.contents[2].string #获取年份那一行
        yearline=yearline.replace(' ','') #去掉这一行的空格
        yearline=yearline.replace('\n','') #去掉这一行的回车换行
        year=yearline[0:4] #只取年份前四个字符
        # 打印结果
        print(title,'\t',year)