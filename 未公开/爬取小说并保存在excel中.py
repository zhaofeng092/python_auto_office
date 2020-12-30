import requests
from lxml import etree
from openpyxl import Workbook


class Book():
    def __init__(p):
        p.url = 'https://www.qidian.com/rank/hotsales?page={页数}'
        p.wb = Workbook()  # class实例化
        p.ws = p.wb.active  # 激活工具表
        p.ws.append(['书名', '作者', '类型', '连载状态'])  # 添加对应的表头

    def geturl(p):
        url = [p.url.format(页数=i) for i in range(1, 15)]
        return url

    def parse_url(p, url):
        response = requests.get(url, timeout=5)
        return response.content.decode('utf-8', 'ignore')

    def get_list(p, html_str):
        html = etree.HTML(html_str)
        connect_list = []
        lists = html.xpath("//div[@class='book-img-text']/ul/li//div[@class='book-mid-info']")
        for list in lists:
            item = {}
            item['书名'] = ''.join(list.xpath("./h4/a/text()"))
            item['作者'] = ''.join(list.xpath("./p[@class='author']/a[1]/text()"))
            item['类型'] = ''.join(list.xpath("./p[@class='author']/a[2]/text()"))
            item['连载状态'] = ''.join(list.xpath("./p[@class='author']/span/text()"))
            connect_list.append(item)
        return connect_list

    def save_list(p, connects):
        for connect in connects:
            p.ws.append([connect['书名'], connect['作者'], connect['类型'], connect['连载状态']])
        print('保存小说信息成功')

    def run(p):
        url_list = p.geturl()
        for url in url_list:
            html_url = p.parse_url(url)
            connects = p.get_list(html_url)
            p.save_list(connects[:])
        p.wb.save('book.xlsx')


if __name__ == '__main__':
    spider = Book()
    spider.run()
