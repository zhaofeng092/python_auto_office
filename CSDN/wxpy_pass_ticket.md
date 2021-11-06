<div align="center">
    <a href="https://github.com/zhaofeng092/python_auto_office"> <img src="https://badgen.net/badge/Github/%E7%A8%8B%E5%BA%8F%E5%91%98?icon=github&color=red"></a>
    <a href="https://mp.weixin.qq.com/s/xkZSp3606rTPN_JbLT3hSQ"> <img src="https://badgen.net/badge/follow/%E5%85%AC%E4%BC%97%E5%8F%B7?icon=rss&color=green"></a>
    <a href="https://space.bilibili.com/259649365"> <img src="https://badgen.net/badge/pick/B%E7%AB%99?icon=dependabot&color=blue"></a>
    <a href="https://mp.weixin.qq.com/s/wx-JkgOUoJhb-7ZESxl93w"> <img src="https://badgen.net/badge/join/%E4%BA%A4%E6%B5%81%E7%BE%A4?icon=atom&color=yellow"></a>
</div>

使用wxpy开发微信聊天机器人，结果扫码登录后，提示：

```python
KeyError: 'pass_ticket'
```

> 解决方法：wxpy是根据网页版微信的接口封装的库。用wxpy，得去试试网页版微信（[https://wx.qq.com/](https://wx.qq.com/)）看能否正常登录。


如果出现下面的提示内容，则该微信号也无法使用wxpy进行登录了！目前没有任何办法~

```python
<error><ret>1203</ret><message>为了你的帐号安全，此微信号已不允许登录网页微信。
你可以使用Windows微信或Mac微信在电脑端登录。
Windows微信下载地址：https://pc.weixin.qq.com 
Mac微信下载地址：https://mac.weixin.qq.com</message></error>
```

 ![图片](https://img-blog.csdnimg.cn/img_convert/9f9ea5e5338cbbfda46b8230d5fcf21e.png)