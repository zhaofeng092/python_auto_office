# -*- coding: utf-8 -*-
# @Time : 2020/4/29 17:08
# @Author : lzf
# @File : time_weibo_send.py
# @Software: PyCharm
# @Description:

import requests
import re
import pandas as pd
import time as tm
import random
# ------------------------
id = "2304132803301701"
timedata = []
for p in range(1,3):
    page = str(p)
    url = "https://m.weibo.cn/api/container/getIndex?containerid=" + id + "_-_WEIBO_SECOND_PROFILE_WEIBO&luicode=10000011&lfid=" + id + "&page_type=03&page=" + page
    print(url)
    data = requests.get(url)
    data_text = data.text
    data_num = re.findall(r'\"mid\"\:\"(\d{16})\"', data_text)
    num = len(data_num)
    for i in range(0,num):
        url_detail = "https://m.weibo.cn/detail/" + data_num[i]
        print(url_detail)
        html = requests.get(url_detail)
        time = re.search(r'\"created_at\"\:\s\"(\w\w\w\s\w\w\w\s\d\d\s\d\d\:\d\d\:\d\d)\s\+\d{4}\s\d{4}\"', html.text)
        timedata.append(time.group(1))
        tm.sleep(random.uniform(1,4)) #反爬间隔
        print("采集第%d页第%d条微博数据"%(p,i))
name =["time"]
data_save = pd.DataFrame(columns=name, data=timedata)
data_save.to_csv('./data.csv')
