# -*- coding: utf-8 -*-
# @Time : 2020/5/21 8:39
# @Author : lzf
# @File : test.py
# @Software: PyCharm
# @Description:

import requests
from lxml import etree
import time

url = 'https://movie.douban.com/subject/30378158/comments?start=%d&limit=20&sort=new_score&status=F'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64)'
                 ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'Cookie': 'll="108169"; bid=H2Lzyg2h8rU; douban-fav-remind=1; __gads=ID=1aff6df6af19fada:T=1587958933:S=ALNI_MbkgRZlgp-KPZcfo6qbr8CtaMmCJw; _vwo_uuid_v2=DFD453C44679787CAB785201397EC8F2D|57372c8e5f59f81dc5cc26a4001ac9a7; __utma=30149280.476532630.1587958935.1588153265.1589710153.4; __utmc=30149280; __utmz=30149280.1589710153.4.2.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ap_v=0,6.0; __utmb=30149280.2.10.1589710153'
}

if __name__ == '__main__':
    fp=open('climb.csv', mode='w', encoding='utf-8')
    fp.write('author\tcomment\tvote\n')
    #  0,20,40,200ll="108169"; bid=H2Lzyg2h8rU; douban-fav-remind=1; __gads=ID=1aff6df6af19fada:T=1587958933:S=ALNI_MbkgRZlgp-KPZcfo6qbr8CtaMmCJw; _vwo_uuid_v2=DFD453C44679787CAB785201397EC8F2D|57372c8e5f59f81dc5cc26a4001ac9a7; __utma=30149280.476532630.1587958935.1588153265.1589710153.4; __utmc=30149280; __utmz=30149280.1589710153.4.2.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ap_v=0,6.0; __utmb=30149280.2.10.1589710153
    for i in range(11):
        if i ==10:   #  最后一页
            url_climb = url%(200)
        else:
            url_climb = url%(i*20)
        #print(url_climb)
        response=requests.get(url_climb,headers=headers)
        response.encoding = 'utf-8'
        text=response.text
        html=etree.HTML(text)
        comments=html.xpath('//div[@id="comments"]/div[@class="comment-item"]')
        #print(comments)
        for comment in comments:
            #  作者
            author=comment.xpath('./div[@class="avatar"]/a/@title')[0].strip()
            #  评论
            p=comment.xpath('.//span[@class="short"]/text()')[0].strip()
            #  点赞
            vote = comment.xpath('.//span[@class="votes"]/text()')[0].strip()
            #print('%s\t%s\t%s\n' % (author,p,vote))
            # name = '%s\t%s\t%s\n' % (author,p,vote)
            # with open('./climb.txt', 'a',encoding='utf-8') as f:
            #     f.write(name)
            fp.write('%s\t%s\t%s\n' % (author,p,vote))

            time.sleep(1)
            print('第%d页数据保存成功' % (i + 1))
        #fp.close()  不退出就可以运行，退出文件报错
