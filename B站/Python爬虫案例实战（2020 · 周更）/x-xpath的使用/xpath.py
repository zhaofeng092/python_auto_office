# -*- coding: utf-8 -*-
# @Time : 2020/5/29 22:01
# 公众号：Python自动化办公社区
# @File : xpath.py
# @Software: PyCharm
# @Description: 怎么定位网页中的数据？XPath的基本使用。


import requests
from lxml import html


# 获取网页数据
def get_html_data(url):
    html_code = requests.get(url)
    html_code.encoding = 'utf-8'
    html_code = html_code.text

    # 格式网站代码的工具
    etree_tools = html.etree
    # 格式化获取的网站代码
    format_html = etree_tools.HTML(html_code)
    # 通过@title获取他的title标签里面的内容
    li_anchors = format_html.xpath('//*[@class="qzw_articlelist"]//li')
    titles = ''
    for li in li_anchors:
        title = str(li.xpath('./a/text()')[0])
        titles += title
    return titles