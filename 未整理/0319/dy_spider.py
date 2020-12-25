# -*- coding: UTF-8 -*-
# 公众号  ：  技术TA说
# 代码作者  ：  看门大叔
# 创建时间  ：  2020/3/19  20:29
# 文件名称  :  dy_spider.py
# 开发工具  :  PyCharm

import requests

url = 'https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg'
commentid = ''
for x in range(1):

    params = {
        'g_tk': '5381',
        'loginUin': '0',
        'hostUin': '0',
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'GB2312',
        'notice': '0',
        'platform': 'yqq.json',
        'needNewCode': '0',
        'cid': '205360772',
        'reqtype': '2',
        'biztype': '1',
        'topid': '102065756',
        'cmd': '8',
        'needcommentcrit': '0',
        'pagenum': str(x),
        'pagesize': '25',
        'lasthotcommentid': commentid,
        'domain': 'qq.com',
        'ct': '24',
        'cv': '101010  '
    }
    res_comment = requests.get(url, params=params)
    json_comment = res_comment.json()
    # print(json_comment)

    list_comment = json_comment['comment']['commentlist']
    # print(list_comment)
    for comment in list_comment:
        print(comment['rootcommentcontent'])
    print(len(list_comment))
    commentid = list_comment[9]['commentid']




