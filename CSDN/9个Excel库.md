<div align="center">
    <a href="https://github.com/zhaofeng092/python_auto_office"> <img src="https://badgen.net/badge/Github/%E7%A8%8B%E5%BA%8F%E5%91%98?icon=github&color=red"></a>
    <a href="http://t.cn/A6Gkrbzw"> <img src="https://badgen.net/badge/follow/%E5%85%AC%E4%BC%97%E5%8F%B7?icon=rss&color=green"></a>
    <a href="https://space.bilibili.com/259649365"> <img src="https://badgen.net/badge/pick/B%E7%AB%99?icon=dependabot&color=blue"></a>
    <a href="https://mp.weixin.qq.com/s/CadAaJUTUlXmTxJAjFUfPQ"> <img src="https://badgen.net/badge/join/%E4%BA%A4%E6%B5%81%E7%BE%A4?icon=atom&color=yellow"></a>
</div>


往日回顾：[内幕 | 报价上万的大屏数据可视化，成本只有10分钟？（附18套可视化模板）](http://mp.weixin.qq.com/s?__biz=MzI2Nzg5MjgyNg==&mid=2247487795&idx=1&sn=2c5c03e79779e5c3771c6907fb86ef75&chksm=eaf6b006dd81391003d372e4d73447b01e296655222564d8e262ee36c5b7a146c02ed2d8ea0e&scene=21#wechat_redirect)



**环境配置及可实现操作**

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/SAHDhZ6pPOibuS0xkxf1HGCtV1KxmOy2ic2qcAEQxDSsa1icC6on0bibkxBRHPxgqZ3rVuI4UnwGcscibcpO3Ifwzjg/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

# 1、xlrd

xlrd是一个从Excel文件读取数据和格式化信息的库，支持.xls以及.xlsx文件。

http://xlrd.readthedocs.io/en/latest/

1、xlrd支持.xls，.xlsx文件的读

2、通过设置on_demand变量使open_workbook()函数只加载那些需要的sheet，从而节省时间和内存（该方法对.xlsx文件无效）。

3、xlrd.Book对象有一个unload_sheet方法，它将从内存中卸载工作表，由工作表索引或工作表名称指定（该方法对.xlsx文件无效）

# 2、xlwt

xlwt是一个用于将数据和格式化信息写入旧Excel文件的库（如.xls）。

https://xlwt.readthedocs.io/en/latest/

1、xlwt支持.xls文件写。

3、xlutils

xlutils是一个处理Excel文件的库，依赖于xlrd和xlwt。

http://xlutils.readthedocs.io/en/latest/

1、xlutils支持.xls文件。

2、支持Excel操作。



![图片](https://mmbiz.qpic.cn/mmbiz_png/SAHDhZ6pPOibuS0xkxf1HGCtV1KxmOy2ic7hAUiaeuib4VamYHtHFXO988QXwK0QicQxTK1MqDOsMwiamT9xBlBhcG4g/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

免费加入知识星球，专注、高效、共赢

# 4、xlwings

xlwings是一个可以实现从Excel调用Python，也可在python中调用Excel的库。

http://docs.xlwings.org/en/stable/index.html

1、xlwings支持.xls读，支持.xlsx文件读写。

2、支持Excel操作。

3、支持VBA。

4、强大的转换器可以处理大部分数据类型，包括在两个方向上的numpy array和pandas DataFrame。

5、都看到这里了，还不点个赞？

# 5、openpyxl

openpyxl是一个用于读取和编写Excel 2010 xlsx/xlsm/xltx/xltm文件的库。

https://openpyxl.readthedocs.io/en/stable/

1、openpyxl支持.xlsx文件的读写。

2、支持Excel操作。

3、加载大.xlsx文件可以使用read_only模式。

4、写入大.xlsx文件可以使用write_only模式。

# 6、xlsxwriter

xlsxwriter是一个用于创建Excel .xlsx文件的库。

https://xlsxwriter.readthedocs.io/

1、xlswriter支持.xlsx文件的写。

2、支持VBA。

3、写入大.xlsx文件时使用内存优化模式。

# 7、win32com

win32com库存在于pywin32中，是一个读写和处理Excel文件的库。

http://pythonexcels.com/python-excel-mini-cookbook/

1、win32com支持.xls，.xlsx文件的读写，支持.xlsx文件的写。

2、支持Excel操作。

# 8、DataNitro

DataNitro是一个内嵌在Excel中的插件。

https://datanitro.com/docs/

1、DataNitro支持.xls，.xlsx文件的读写。

2、支持Excel操作。

3、支持VBA。

4、收费。注：DataNitro作为插件使用需依托软件本身。



# 9、pandas

pandas通过对Excel文件的读写实现数据输入输出

http://pandas.pydata.org/

1、pandas支持.xls，.xlsx文件的读写。

2、支持只加载每个表的单一工作页。

3、点我：[**如何用Python处理Excel？Pandas视频教程&官方文档来啦~**](http://mp.weixin.qq.com/s?__biz=MzI2Nzg5MjgyNg==&mid=2247487280&idx=1&sn=504f948be74ae8a2fa9f3419ef8fbc5d&chksm=eaf6ae05dd812713b99e1164589d17333173ac0c60c2bfcf1942c84f8fcbac225664ec248923&scene=21#wechat_redirect)



————————————————

> 参考：https://zhuanlan.zhihu.com/p/23998083

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/SAHDhZ6pPOibgo7Ze5JAPiaYYmteOo95fwpiacvSnibzVmNVCEN6fbfgaDKGHNlMZ6aFiaGjuCfr4ekng7mlfUaCWyg/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)