# -*- coding: utf-8 -*-
# @Time : 2020/4/21 17:16
# @Author : Python自动化办公社区
# @File : local_code.py
# @Software: PyCharm
# @Description:


import codecs
import csv
import random
import threading
import time

import requests
import os
import json


class eastmoneyspider_new():
    page_num = 1
    page_size = 1000
    type = "YJBB21_YJBB"
    filter = "(securitytypecode in ('058001001','058001002'))(reportdate=^datetime^)"

    url = "http://dcfm.eastmoney.com/em_mutisvcexpandinterface/api/js"
    param = {
        "type": type,
        "token": "70f12f2f4f091e459a279469fe49eca5",
        # "st":"latestnoticedate",
        # "sr":"-1",
        "p": page_num,
        "ps": page_size,
        "js": "var yWBvWaEi={pages:(tp),data: (x),font:(font)}",
        "filter": filter,
        # "rt":"52834634"
    }
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Connection": "keep-alive",
        "Cookie": "em_hq_fls=js; HAList=f-0-000001-%u4E0A%u8BC1%u6307%u6570%2Ca-sz-300033-%u540C%u82B1%u987A%2Cd-hk-03978; cowCookie=true; st_si=04286436098362; qgqp_b_id=26c5686b4561e994f18e813ffccd233d; st_pvi=78119759712311; st_sp=2020-03-13%2009%3A23%3A47; st_inirUrl=https%3A%2F%2Fwww.baidu.com%2Fs; st_sn=28; st_psi=20200324163709596-113300301066-1761262920; st_asi=delete; intellpositionL=1215.35px; intellpositionT=2246.2px",
        "Host": "dcfm.eastmoney.com",
        "Referer": "http://data.eastmoney.com/bbsj/201903/yjbb.html",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3141.8 Safari/537.36}"
    }

    # 写入文件
    def write_to_file(this, df_table, category):
        # 设置文件保存在D盘eastmoney文件夹下
        file_path = 'D:\\eastmoney'
        if not os.path.exists(file_path):
            os.mkdir(file_path)
        os.chdir(file_path)
        df_table.to_csv('{}.csv'.format(category), mode='a', encoding='utf_8_sig', index=0, header=0)

    def start(self, date):
        time.sleep(random.randint(1, 5))
        self.param['filter'] = self.filter.replace('datetime', date)
        r = requests.post(url=self.url, headers=self.headers, data=self.param, timeout=30)
        r.encoding = r.apparent_encoding
        # print(r.text)

        org_data = r.text[r.text.index("{"):]
        json_str = org_data.replace('data:', '"data":').replace('pages:', '"pages":').replace('font:', '"font":')
        json_data = json.loads(json_str)
        # print(json_data)

        # 字体文件
        font_url = json_data['font']['WoffUrl']
        # print(font_url)
        font = requests.get(font_url, headers=self.headers, timeout=30)
        font_name = font_url.split("/")[-1]
        # print("font_name:" + font_name)
        with codecs.open(font_name, 'wb') as f:
            f.write(font.content)
        # font_map = TTFont(font_name).getBestCmap()
        # font_index = [hex(key).upper().replace('0X', '&#x') + ';' for key in font_map.keys()]

        font_mapping = json_data['font']['FontMapping']
        # print(font_mapping)
        replace_dict = {i['code']: str(i['value']) for i in font_mapping}
        # print(replace_dict)

        for k, v in replace_dict.items():
            json_str = json_str.replace(k, v)

        final_data = json.loads(json_str)
        # print(final_data)

        rows = final_data['data']
        # print(rows)
        title_list = []
        for title in rows[0]:
            title_list.append(title)
        # print(title_list)

        save_file = 'D:\\eastmoney\\{}.csv'.format(date + "_" + self.param['type'])
        with open(save_file, 'a', newline='') as f:
            f_csv = csv.DictWriter(f, title_list)
            f_csv.writeheader()  # 写入头
            f_csv.writerows(rows)  # 一次性写入多行

    def run(self):
        date_list = ['2019-03-31', '2019-06-30', '2019-09-30', '2019-12-31']
        for date in date_list:
            self.param['filter'] = self.filter.replace('datetime', date)
            type_list = ['YJBB21_YJBB', 'CWBB_ZCFZB20', 'CWBB_LRB20', 'CWBB_XJLLB20']
            for type in type_list:
                self.param["type"] = type
                r = requests.post(url=self.url, headers=self.headers, data=self.param)
                r.encoding = r.apparent_encoding
                org_data = r.text[r.text.index("{"):]
                json_str = org_data.replace('data:', '"data":').replace('pages:', '"pages":').replace('font:',
                                                                                                      '"font":')
                json_data = json.loads(json_str)
                pages = json_data['pages']

                for i in range(1, pages + 1):
                    self.param['p'] = i
                    print('正在爬取{param1}报表类型为{param2}的第{param3}页'.format(param1=date,
                                                                        param2=type,
                                                                        param3=str(i)))
                    # self.start(date)
                    # 创建线程
                    threads = []
                    t = threading.Thread(target=self.start(date), args=date)
                    threads.append(t)
                    # 启动线程
                    for y in range(len(threads)):
                        threads[y].start()
                    for y in range(len(threads)):
                        threads[y].join()


if __name__ == '__main__':
    esastmoneyspider = eastmoneyspider_new()
    esastmoneyspider.run()
    # esastmoneyspider.start('2019-03-31')

# https://blog.csdn.net/qq_29622761/article/details/105090403
# -*- coding: utf-8 -*-
# @Time : 2020/5/18 10:33
# @Author : lzf
# @File : test.py
# @Software: PyCharm
# @Description: 