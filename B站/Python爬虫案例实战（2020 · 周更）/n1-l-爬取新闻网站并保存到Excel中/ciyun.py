# -*- coding: utf-8 -*-
# @Time : 2020/3/20 14:06
# @Author : lzf
# @File : ciyun.py
# @Software: PyCharm
# @Description:

import jieba
import numpy as np
from wordcloud import WordCloud, STOPWORDS
from PIL import Image



def get_ciyun(content):

    # 3. 制作词云
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
    wc.to_file('词云.png')

    # 6. 展示词云
    img = Image.open('词云.png')
    img.show()


get_ciyun('''文艺，电台，情感

coding，技术极客
有韧性、做事认真、随心
声音好听、性格温柔、211研究生
矮呆萌 
闹腾，幽默，心中有正义
爱折腾，爱成分表，爱美妆
平凡 执着 奋进
爱折腾，爱买买买，爱囤货
慢性子，话不多，爱思考
汉服  文学  绘画
幽默，靠谱，三次传销经历[偷笑]
乐观主义，有点努力，女博士
乐观、务实、动力十足
爱学习，肯努力，向上''')