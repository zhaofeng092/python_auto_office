# 安装爬虫框架Scrapy,并运行测试代码：爬虫百度首页

###### 安装Scrapy之前，一定要安装好Python和PyCharm

传送门：[安装python的教程]( http://t.cn/A6Ps4pmr)
  
传送门：[安装PhCharm的教程]( http://t.cn/A6Ps4REw)

### 1、安装Scrapy

`pip install scrapy`


pip操作最好是配置一个阿里的镜像，没配置的话，用下面这句进行下载：


`pip install -i https://pypi.tuna.tsinghua.edu.cn/simple scrapy`


### 2、新建Scrapy项目scrapy_demo

`scrapy startproject scrapy_demo`

### 3、在新建的项目目录scrapy_demo/scrapy_demo/spiders下，新建baidu.py
```
#直接复制这段代码到baidu.py
from scrapy import Spider, Request

class TJSpider(Spider):
    name = 'baidu'
    start_urls = ['https://www.baidu.com']

    def parse(self, response):
        text = response.text
        print(text)

```

### 4、关闭目录scrapy_demo/scrapy_demo/settings.py下的rebot协议

```
# Obey robots.txt rules
ROBOTSTXT_OBEY = False
```

### 5、在terminal里运行baidu.py

`scrapy crawl baidu`

传送门：[爬虫入门之百度首页爬取]( https://mp.weixin.qq.com/s/Oitt09fnOYQjQZCu1HIOyw)

更多内容，请关注公众号：数据TA说
![数据TA说](https://github.com/kanmendashu2020/verify_python/blob/master/data.jpg)
