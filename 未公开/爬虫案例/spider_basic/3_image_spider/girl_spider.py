# -*- coding: utf-8 -*-
# @Time : 2020/3/6 9:19
# @Author : 技术TA说
# @File : girl_spider.py
# @Software: PyCharm

import requests
import re
import os
from urllib import error


def main():
    # 图片存储路径
    dirPath = "girl-images"
    # 目标网页
    # https: // www.buxiuse.com /?page = 9
    base_url = "https://www.buxiuse.com/?page={}"
    # 页数从2开始
    page = 2
    # 图片名称序号
    image_id = 0
    for page in range(2, 12):
        url = base_url.format(page)
        try:
            result = requests.get(url, timeout=10)
        except error.HTTPError as e:
            page += 1
            continue
        else:
            text = result.text
            list = re.findall('src="(.*?.jpg)"', text, re.S)
            if len(list) == 0:
                page += 1
                continue
            else:
                for enum in list:
                    image = requests.get(enum, timeout=7)
                    filePath = os.path.join(dirPath, "girl_image_" + str(image_id) + ".jpg")
                    print_str = '这是第 {} 位小姐姐'
                    print(print_str.format(image_id))
                    f = open(filePath, 'wb')
                    f.write(image.content)
                    f.close()
                    image_id += 1
                page += 1


if __name__ == '__main__':
    main()
