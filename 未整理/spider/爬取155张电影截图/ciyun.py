# -*- coding: utf-8 -*-
# @Time : 2020/3/20 14:06
# 公众号：Python自动化办公社区
# @File : ciyun.py
# @Software: PyCharm
# @Description:

import jieba
import numpy as np
from wordcloud import WordCloud, STOPWORDS
from PIL import Image


# 制作词云
def get_ciyun(content):


    wl_space_split = ' '.join(jieba.lcut(content))  # jieba返回分好的词
    # stop_words = set(STOPWORDS)
    abel_mask = np.array(Image.open('001.jpg'))  # 用于生成配色方案的图片，可以是任意图片，建议图片越清晰越好
    # 4. 生成词云
    wc = WordCloud(
        background_color='black',  # 背景颜色
        font_path='simfang.ttf',  # 字体
        max_words=3000,  # 最大词数
        max_font_size=100,  # 显示字体最大值
        random_state=42,  # 为每个词返回一个PIL颜色
        mask=abel_mask,  # 以该参数值作图绘制词云
        stopwords=STOPWORDS,  # 屏蔽词
        # stopwords= STOPWORDS.add('中国'),   # 在内置屏蔽词的基础上添加自定义屏蔽词
    ).generate(wl_space_split)  # 生成词云

    # 5. 保存生成的词云图片
    wc.to_file('res.png')

    # 6. 展示词云
    img = Image.open('res.png')
    img.show()


get_ciyun('''正则表达式是一个特殊的字符序列，它能帮助你方便的检查一个字符串是否与某种模式匹配。

Python 自1.5版本起增加了re 模块，它提供 Perl 风格的正则表达式模式。

re 模块使 Python 语言拥有全部的正则表达式功能。

compile 函数根据一个模式字符串和可选的标志参数生成一个正则表达式对象。该对象拥有一系列方法用于正则表达式匹配和替换。

re 模块也提供了与这些方法功能完全一致的函数，这些函数使用一个模式字符串做为它们的第一个参数。

本章节主要介绍 Python 中常用的正则表达式处理函数，如果你对正则表达式不了解，可以查看我们的 正则表达式 - 教程。''')

# 1、改内容
# 2、改图片
# 3、改背景色
# 4、改结果图片名字
