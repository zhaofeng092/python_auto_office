# -*- coding: UTF-8 -*-
# 公众号  ：  技术TA说
# 代码作者  ：  看门大叔
# 创建时间  ：  2020/3/15  16:06
# 文件名称  :  9x9_live.py
# 开发工具  :  PyCharm

# 方式3：
# print('\n方式3：')
# for x in range(1, 10):
#     for y in range(1, 1 + x):
#         print(str(y), '*', str(x), '=', str(x * y), sep='', end='\t')
#     print()

second_hang = 1
first_1_hang = 1
for second_hang in range(1,10):
    for first_1_hang in range(1,second_hang+1):
        print(str(first_1_hang),'*',str(second_hang),'=',first_1_hang*second_hang,sep='',end='\t')
    print()



