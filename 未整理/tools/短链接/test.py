import requests


# 短链接
def long2short(long_url):
    try:
        base_url = 'https://www.98api.cn/api/sinaDwz.php?url='
        short_url = requests.get(base_url + str(long_url)).json()['short_url']
        if 'http://t.cn/Ai3sAGR7' in short_url or '.jd.com' in long_url:
            mail_api = "http://api.ft12.com/api.php?url={}&apikey=gZWbWTUDXcPkaxyP3X@ddd"
            init = mail_api.format(long_url)
            short_url = requests.get(init).text
    except:
        mail_api = "http://api.ft12.com/api.php?url={}&apikey=gZWbWTUDXcPkaxyP3X@ddd"
        init = mail_api.format(long_url)
        short_url = requests.get(init).text
    return short_url

short_url = long2short('https://mp.weixin.qq.com/s?__biz=MzUzNTc5NjA4NQ==&amp;mid=2247483737&amp;idx=1&amp;sn=a990d0f34585c15df160eeb3bcfa11c2&amp;chksm=fa814143cdf6c855ad87fa9e2376c526ab15f5b6d302874b8ffae2ab4a10eac8cae81011a9e5&amp;token=575479880&amp;lang=zh_CN&rd2werd=1#wechat_redirect')
print(short_url)


