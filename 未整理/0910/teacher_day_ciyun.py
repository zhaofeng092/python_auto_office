# -*- coding: utf-8 -*-
# @Time : 2020/8/20 18:10
# @公众号 :Python自动化办公社区 
# @File : write_doc.py
# @Software: PyCharm
# @Description:
# 代码中所需的素材获取，请关注公众号：Python自动化办公社区 ，发送：0816，加入微信群获取

#加载需要使用的类库
from PIL import Image
import numpy as np
from wordcloud import WordCloud, ImageColorGenerator
from matplotlib import pyplot as plt
import jieba
# 分词
def trans_CN(text):
    # 接收分词的字符串
    word_list = jieba.cut(text)
    # 分词后在单独个体之间加上空格
    result = " ".join(word_list)
    return result


with open("ciyun.txt", encoding='utf8') as fp:
    text = fp.read()
    # print(text)
    # 将读取的中文文档进行分词
    cloud_text = trans_CN(text)

    #加载背景图片
    cloud_mask = np.array(Image.open("003.jpg"))
    #忽略显示的词
    st=set(["东西","这是"])
    #生成wordcloud对象
    wc = WordCloud(background_color="white",
        mask=cloud_mask,
        max_words=200,
        font_path="simkai.ttf",
        min_font_size=15,
        max_font_size=50,
        width=400,
        stopwords=st)
    wc.generate(cloud_text)
    wc.to_file("pic.png")