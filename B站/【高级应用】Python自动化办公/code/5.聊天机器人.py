'''
微信机器人
'''
import hashlib
import time
import random
import string
from urllib.parse import quote
import requests

import hashlib
import time
import random
import string
from urllib.parse import quote


def curlmd5(src):
    m = hashlib.md5(src.encode('UTF-8'))

    # 将得到的MD5值所有字符转换成大写
    return m.hexdigest().upper()


app_id = '2125174629'
app_key = 'vSW4Z5ZnXOCnXxGc'

def get_params(plus_item):
    # 请求时间戳（秒级），用于防止请求重放（保证签名5分钟有效）  
    t = time.time()
    time_stamp = str(int(t))
    # 请求随机字符串，用于保证签名不可预测  
    nonce_str = ''.join(random.sample(string.ascii_letters + string.digits, 10))
    # 应用标志，这里修改成自己的id和key  

    params = {'app_id': app_id,
              'question': plus_item,
              'time_stamp': time_stamp,
              'nonce_str': nonce_str,
              'session': '10000'
              }
    sign_before = ''
    # 要对key排序再拼接  
    for key in sorted(params):
        # 键值拼接过程value部分需要URL编码，URL编码算法用大写字母，例如%E8。quote默认大写。  
        sign_before += '{}={}&'.format(key, quote(params[key], safe=''))
    # 将应用密钥以app_key为键名，拼接到字符串sign_before末尾  
    sign_before += 'app_key={}'.format(app_key)
    # 对字符串sign_before进行MD5运算，得到接口请求签名  
    sign = curlmd5(sign_before)
    params['sign'] = sign
    return params


def get_content(plus_item):
    # 聊天的API地址
    url = "https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat"
    # 获取请求参数
    plus_item = plus_item.encode('utf-8')
    payload = get_params(plus_item)
    r = requests.post(url, data=payload)
    return r.json()["data"]["answer"]


if __name__ == '__main__':
    if app_id != '戳我获取：https://mp.weixin.qq.com/s/mA-GG69kQwxk8CFuMY6NQg':

        while True:
            comment = input('我：')
            if comment == 'q':
                break
            answer = get_content(comment)
            print('机器人：' + answer)
    else:
        attention = '''-----
您还没有填写账号密码哦~
可以自己在腾讯AI平台免费申请,
也可以使用兆锋私人的，戳我获取：https://mp.weixin.qq.com/s/mA-GG69kQwxk8CFuMY6NQg
-----'''
        print(attention)
