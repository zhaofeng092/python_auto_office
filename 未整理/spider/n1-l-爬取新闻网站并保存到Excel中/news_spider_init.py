# -*- coding: utf-8 -*-
# @Time : 2020/3/20 9:28
# @Author : kanmendashu2020
# @File : news_spider_init.py
# @Software: PyCharm
# @Description:

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


#################生成词云图片#####################
import jieba
import numpy as np
from wordcloud import WordCloud, STOPWORDS
from PIL import Image


def get_ciyun(content):
    # 3. 制作词云
    wl_space_split = ' '.join(jieba.lcut(content))  # jieba返回分好的词
    # stop_words = set(STOPWORDS)
    abel_mask = np.array(Image.open('002.jpg'))  # 用于生成配色方案的图片，可以是任意图片，建议图片越清晰越好
    # 4. 生成词云
    wc = WordCloud(
        background_color='white',  # 背景颜色
        font_path='simfang.ttf',  # 字体
        max_words=3000,  # 最大词数
        max_font_size=100,  # 显示字体最大值
        random_state=42,  # 为每个词返回一个PIL颜色
        mask=abel_mask,  # 以该参数值作图绘制词云
        stopwords=STOPWORDS,  # 屏蔽词
        # stopwords= STOPWORDS.add('中国'),   # 在内置屏蔽词的基础上添加自定义屏蔽词
    ).generate(wl_space_split)  # 生成词云

    # 5. 保存生成的词云图片
    wc.to_file('词云.png')

    # 6. 展示词云
    img = Image.open('词云.png')
    img.show()


url = 'http://www.qzwb.com/gb/node/node_1467.htm'
content = get_html_data(url)
get_ciyun(content)