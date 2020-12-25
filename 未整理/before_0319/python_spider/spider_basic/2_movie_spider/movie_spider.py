from lxml import html
import requests


def get_movie_resouce(movie):
    # 目标网站
    base_url = 'http://ifkdy.com/?q={}'
    # 格式网站代码的工具
    etree = html.etree
    # 获取电影名称
    url = base_url.format(movie)
    # 获取网站信息
    data = requests.get(url).text
    # 格式化获取的网站代码
    s = etree.HTML(data)
    # 通过@title获取他的title标签里面的内容
    anchors = s.xpath('//*[@class="statistical result-detail10993hhh"]//a')
    # 输出结构的换行符
    next_line = '\n'
    # 输出结果的格式
    res_content = '[' + movie + ']电影资源' + next_line + '(请复制到浏览器观看/下载，微信端打不开)：'
    # 没有该标签，说明没有查询结果
    if len(anchors) == 0:
        res_content = res_content + next_line + '抱歉，暂时没有该电影资源'
    # 否则，循环a标签，取出结果
    else:
        n = 0
        for a in anchors:
            n = n + 1
            # 只要前5个结果，这里可以自己修改
            if n == 6:
                break
            # 拿到资源的网址
            hrefs = a.xpath('./@href')
            movie_url_long = hrefs[0]
            # 将资源按照格式拼接起来
            res_content = res_content + next_line + '资源' + str(n) + '：' + movie_url_long
    return res_content


# 运行这段代码
movie = input('movie name：')
resouce = get_movie_resouce(movie)
print(resouce)
