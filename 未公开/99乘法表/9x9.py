# -*- coding: UTF-8 -*-
# 公众号  ：  技术TA说
# 代码作者  ：  看门大叔
# 创建时间  ：  2020/3/12  20:58
# 文件名称  :  9x9.py
# 开发工具  :  PyCharm


# 方式1：
print('方式1：')
result = 0
# 列
for i in range(1, 10):
    # 行
    for j in range(1, i + 1):
        result = i * j
        print('%d*%d=%d' % (i, j, result), end=' ')
    print()

# 方式2：
print('\n方式2：')
print('\n'.join([' '.join(['%s*%s=%-2s' % (j, i, i * j) for j in range(1, i + 1)]) for i in range(1, 10)]))

# 方式3：
print('\n方式3：')
for x in range(1, 10):
    for y in range(1, 1 + x):
        print(str(y), '*', str(x), '=', str(x * y), sep='', end='\t')
    print()
