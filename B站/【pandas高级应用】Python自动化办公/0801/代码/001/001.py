#使用pandas，别名：pd
import pandas as pd
##################  1、没有数据的空表 ####################
# 用pd，生成一个sheet（excel里面的一张表）
#变量：一个盒子
df = pd.DataFrame()
# 保存这个文件
df.to_excel('001.xlsx')
##################  2、有数据的表 ####################
# 注释的快捷键：ctrl+/
df = pd.DataFrame({
    'id':[1,2,3],
    'name':['a','b','c']
})
df.to_excel('001-data.xlsx')
##################  3、有数据的表，取消默认的索引 ####################

df = pd.DataFrame({
    'id':[1,2,3],
    'name':['a','b','c']
})
df = df.set_index('id')
df.to_excel('001-data-index.xlsx')

#运行的快捷键：ctrl+shift+f10