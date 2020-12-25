import requests
from lxml import etree

base_url = 'https://movie.douban.com/subject/30413052/comments?start=%d&limit=20&sort=new_score&status=P'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': 'bid=vmha0OqlJSM; douban-fav-remind=1; douban-profile-remind=1; _vwo_uuid_v2=D98EF73F4BD358407A273142E5A7E0758|d087fea288436004fdb28039e77ff9f4; __utmv=30149280.16407; ll="118286"; viewed="24715620"; gr_user_id=f2a5d685-acfe-4240-8052-bdbbf59aee4c; __utma=30149280.2029930968.1576484937.1587307870.1589966153.14; __utmc=30149280; __utmz=30149280.1589966153.14.12.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.1032421601.1579171885.1579171885.1589966153.2; __utmb=223695111.0.10.1589966153; __utmc=223695111; __utmz=223695111.1589966153.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ap_v=0,6.0; UM_distinctid=172315e28293cd-07262eb238936-7373e61-1fa400-172315e282a4b4; CNZZDATA1272964020=834086444-1579171566-https%253A%252F%252Fwww.baidu.com%252F%7C1589963960; __utmb=30149280.1.10.1589966153; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1589966169%2C%22https%3A%2F%2Fsearch.douban.com%2Fmovie%2Fsubject_search%3Fsearch_text%3D%25E6%2594%2580%25E7%2599%25BB%25E8%2580%2585%26cat%3D1002%22%5D; _pk_ses.100001.4cf6=*; dbcl2="164071570:aL/ee5gMmAM"; ck=4cGg; _pk_id.100001.4cf6=41fbe3f6d3e5305e.1579171889.2.1589968266.1579171920.; push_noty_num=0; push_doumail_num=0',
    'Host': 'movie.douban.com',
    'Pragma': 'no-cache',
    'Referer': 'https://movie.douban.com/subject/30413052/',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
}
if __name__ == '__main__':
    for i in range(1):
        if i == 25:
            url_climb = base_url % (490)
        else:
            url_climb = base_url % (i * 20)
        response = requests.get(url_climb,headers)
        print(url_climb)
        print(response.status_code)
        response.encoding = 'utf-8'
        text = response.text
        print(text)
