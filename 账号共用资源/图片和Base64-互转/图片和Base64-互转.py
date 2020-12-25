import base64
def img_2_base64(path):
    f=open(path,'rb') #二进制方式打开图文件
    ls_f=base64.b64encode(f.read()) #读取文件内容，转换为base64编码
    f.close()
    return (r'data:image/png;base64,{}'.format(ls_f))


# base64字符串转化为图片
def base64_2_img(base64_code):
    # bs='iVBORw0KGgoAAAANSUhEUg....' # 太长了省略
    imgdata=base64.b64decode(base64_code)
    file=open('res.jpg','wb')
    file.write(imgdata)
    file.close()

path = r'../image/resource_资料库.jpg'
base64_code = img_2_base64(path)
print(base64_code)