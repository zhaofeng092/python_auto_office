#!/usr/bin/env python
# -*- coding=utf-8 -*-
import smtplib
from email.mime.text import MIMEText
import threading
import time, datetime

mailto_list = ["3@qq.com"]  # 里面是对方的邮箱
# -----------QQ邮箱发送设置----------------------
mail_server = "smtp.qq.com"  # 以qq邮箱为例子，里面是QQ邮箱的服务，换成其他邮箱需要更改服务
mail_user = "2167@qq.com"  # 这是QQ邮箱的账号
mail_pass = "dffhsafgea"  # 如果是其他的可以直接填上密码，如果用qq之类的，或者邮箱未开服务，会提醒你打开下面的链接


# QQ邮箱需要去官方打开服务：http://service.mail.qq.com/cgi-bin/help?subtype=1&&id=28&&no=1001256
def send_mail(to_list, sub, content):
    msg = MIMEText(content, 'plain', 'utf-8')
    msg["Accept-Language"] = "zh-CN"
    msg["Accept-Charset"] = "ISO-8859-1,utf-8"
    msg['Subject'] = sub
    msg['From'] = mail_user
    msg['To'] = ";".join(to_list)
    try:
        server = smtplib.SMTP()
        server.connect(mail_server)
        server.starttls()
        server.login(mail_user, mail_pass)
        server.sendmail(mail_user, to_list, msg.as_string())
        server.close()
        return True
    except Exception as e:
        print(str(e))
        return False


def get_date():
    return str(datetime.datetime.utcfromtimestamp(time.time()) + datetime.timedelta(hours=8))


def send_warning_mail(title, info):
    now_time = get_date()
    try:
        t = threading.Thread(target=send_mail, args=(mailto_list, title, str(now_time) + " | " + str(info)))
        t.start()
    except:
        pass


if __name__ == '__main__':
    send_warning_mail("this is title", "\nthis is content")

