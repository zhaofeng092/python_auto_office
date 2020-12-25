from scrapy import Spider, Request

#1、获取百度首页内容
    # scrapy框架


class TJSpider(Spider):
    name = 'baidu'
    start_urls = ['https://www.baidu.com']

    def parse(self, response):
        text = response.text
        print(text)