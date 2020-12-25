# -*- coding: utf-8 -*-
# # @Time : 2020/4/26 20:45
# # @Author :公众号：Python自动化办公社区
# # @File : baidu_trans.py
# # @Software: PyCharm
# # @Description:

import urllib.parse, urllib.request,hashlib,urllib,random,json
# from translate import Translator

appid = 'app_id'
secretKey = 'app_key'
url_baidu = 'http://api.fanyi.baidu.com/api/trans/vip/translate'


def baidu_zh2jp(text, f='zh', t='jp'):
    salt = random.randint(32768, 65536)
    sign = appid + text + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    url = url_baidu + '?appid=' + appid + '&q=' + urllib.parse.quote(text) + '&from=' + f + '&to=' + t + \
    '&salt=' + str(salt) + '&sign=' + sign
    response = urllib.request.urlopen(url)
    content = response.read().decode('utf-8')
    data = json.loads(content)
    result = str(data['trans_result'][0]['dst'])
    print(result)
    return result
