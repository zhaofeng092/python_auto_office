# -*- coding: utf-8 -*-
# @Time : 2020/4/25 22:17
# @Author : Data
# @File : get_movie.py
# @Software: PyCharm
# @Description:
import requests
from lxml import html


def get_movie_resouce(movie):
    base_url = 'http://ifkdy.com/search?key={}'
    etree = html.etree

    url = base_url.format(movie)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
    }
    data = requests.get(url, headers=headers).text
    s = etree.HTML(data)
    print(data)
    # 通过@title获取他的title标签里面的内容
    anchors = s.xpath('//*[@class="m-info fr"]//a')
    next_line = '\n'
    res_content = '[' + movie + ']电影资源' + next_line + '(请复制到浏览器观看/下载，微信端打不开)：'
    if len(anchors) == 0:
        res_content = res_content + next_line + '抱歉，暂时没有该电影资源'
    else:
        n = 0
        for a in anchors:
            n = n + 1
            if n == 6:
                break
            hrefs = a.xpath('./@href')
            movie_url_long = hrefs[0]
            res_content = res_content + next_line + '资源' + str(n) + '：' + 'http://ifkdy.com'+movie_url_long
    return res_content

res = get_movie_resouce('超人')
print(res)
