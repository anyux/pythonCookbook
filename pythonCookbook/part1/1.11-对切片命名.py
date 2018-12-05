#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/12/5

'''
question:
我们的代码已经变得无法阅读,到处都是硬编码的切片索引,我们想将它们清理干净.
'''

'''
假设有一些代码用来从字符串的固定位置中取出具体的数据(比如从一个平面文件或类似的格式):
'''

record = '..........100........513.25......'

cost = int(record[10:13]) * float(record[22:27])
print(cost)
'''
1325.0
'''
'''
与其这样为什么不对切片做命名呢?
'''

SHARES = slice(10,13)
PRICE = slice(22,27)

cost = int(record[SHARES]) * float(record[PRICE])

'''
在后一种版本中,由于避免了使用许多神秘难懂的编码索引,我们的代码就变得清晰了许多.
'''

'''
讨论:
作为一条基本准则,代码中如果有很多硬编码的索引值,将导致可读性和维护性都不佳.例如,如果一年以后再回过头来看代码,
你会发现自己很想知道当初编写这些代码时自己想些什么.前面展示的方法可以让我们对代码的功能有着清晰的认识.
一般来说,内置的slice()函数会创建一个切片对象,可以用在任何允许切片操作的地方.例如:
'''


items = [0, 1, 2, 3, 4, 5, 6]

a = slice(2,4)
print(items[a])
print(items[2:4])
'''
[2, 3]
[2, 3]
'''
items[a] = [10,11]
print(items)
'''
[0, 1, 10, 11, 4, 5, 6]
'''

del items[a]

print(items)

'''
[0, 1, 4, 5, 6]
'''

'''
如果有一个slice对象的实例s,可以分别通过,s.start,s.stop,以及s.step属性来得到关于该对象的信息.例如:

此示例,未完成
'''

'''
此外,通过使用indices(size)方法将切片映射到特定大小的序列上,这会返回一个(start,stop,step)元组,
所有的值都已经恰当地限制在边界以内(当做索引操作进可避免出现IndexError异常).例如:
start 表示开始的位置
stop 表示停几次
step表示每次移动多少个位置
'''

a = slice(5,10,2)

s = "HelloWorld"

print(a.indices(len(s)))
'''
(2, 4, 1)
'''

for i in range(*a.indices(len(s))):
    print(s[i])

'''

W
r
d
'''


















