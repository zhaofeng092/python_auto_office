# -*- coding: utf-8 -*-
# @Time : 2020/5/6 20:30
# @Author : lzf
# @File : test.py
# @Software: PyCharm
# @Description:


import sys,webbrowser,bs4,requests,re,os

response = requests.get('https://wallhaven.cc/w/q6ekyd')

print(response.request.headers)
#访问头文件，默认有可能会反扒

html = response.text
#创建文件夹
dir_name = re.findall('<div class="(.*?)">',html)
print(dir_name)

if not os.path.exists(dir_name):
    os.mkdir(dir_name)

pattern = re.findall(r'<img id="wallpaper" src="(.*?)" alt="Anime 2952x2456 BanG Dream! group of women anime" data-wallpaper-id="q6ekyd" data-wallpaper-width="2952" data-wallpaper-height="2456" crossorigin="anonymous" class="fill-vertical">',re.S)
urls = re.findall(pattern,html)
print(urls)

#保存图片
for url in urls:
    time.sleep(1)
    file_name = url.split('/')[-1]
    response = requests.get('https://wallhaven.cc/w/q6ekyd')
    with open(dir_name + '/' + file_name,'wb') as f:
        f.write(response.content)