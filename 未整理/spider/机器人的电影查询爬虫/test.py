import requests
from lxml import html

def get_movie_resouce():
    base_url = 'https://mp.weixin.qq.com/s/xAxcJJivyGdmqiNT-AvWFw'
    etree = html.etree

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
    }
    data = requests.get(base_url, headers=headers).text
    s = etree.HTML(data)
    print(data)

print(get_movie_resouce())