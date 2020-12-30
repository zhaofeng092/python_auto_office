import requests

# 目标网址
url = 'https://www.baidu.com'

# 输入网址，按下回车
# <Response [200]> 成功
# <Response [404]> 失败
# 404例子
html = requests.get(url)
#变成汉语
html.encoding = 'utf-8'
#把变成汉语的html代码
text = html.text

# 输出到屏幕上
# print(text)
file = open('baidu.html', 'a+', encoding='utf-8')

file.write(text)
file.close()

