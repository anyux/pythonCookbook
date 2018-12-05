#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/11/30

'''
question:
我们想在字典上对数据执行各种计算(比如求最大值,最小值,排序等)
'''

'''
解决方案:
假设有一个字典在股票名称和对应的价格间做了映射:
'''

prices = {
    'ACME' : 45.23,
    'AAPL' : 612.78,
    'IBM'  : 205.55,
    'HPQ'  : 37.20,
    'FB'   : 10.75,
}

'''
为了能对字典的内容做一些有用的计算,通常会使用zip()将字典的键和值反转过来.例如,下面的代码会告诉我们如何找出价格最低和最高的股票:
'''
min_price = min(zip(prices.values(),prices.keys()))
print(min_price)
'''
(10.75, 'FB')
'''
min_price = max(zip(prices.values(),prices.keys()))
print(min_price)
'''
(612.78, 'AAPL')
'''
'''
同样,要对数据排序只要使用zip()再配合sorted()就可以了,比如:
'''
prices_sorted = sorted(zip(prices.values(),prices.keys()))
print(prices_sorted)
'''
[(10.75, 'FB'), (37.2, 'HPQ'), (45.23, 'ACME'), (205.55, 'IBM'), (612.78, 'AAPL')]
'''

'''
当进行这些计算时,请注意zip()创建了一个迭代器,它的内容只能被消费一次.例如下面的代码就是错误的:
'''
prices_and_names = zip(prices.values(),prices.keys())
print(min(prices_and_names))
# print(max(prices_and_names)) #max() arg is an empty sequence

'''
(10.75, 'FB')
Traceback (most recent call last):
  File "E:/pythonCookbook/pythonCookbook/part1/1.8-与字典有关的计算问题.py", line 51, in <module>
ValueError: max() arg is an empty sequence
'''
'''
讨论:
如果尝试在字典上执行常见的数据操作,将会发现它们只会处理键,而不是值.例如:
'''
print(min(prices))
print(max(prices))
'''
AAPL
IBM
'''
'''
这很可能不是我们期望的,实际上我们是尝试对字典的值做计算.可以利用字典的values()方法来解决这个问题:
'''

print(min(prices.values()))
print(max(prices.values()))

'''
10.75
612.78
'''
'''
不幸的是,这通常也不是我们期望的.比如,我们可能想知道相应的键所关联的信息是什么?(通常是哪支股票的价格最低?)
如果提供一个key参数传递给min()和max(),就能得到最大值和最小值所对应的键是什么.例如:
'''
print(min(prices, key=lambda k: prices[k]))
print(max(prices, key=lambda k: prices[k]))
'''
FB
AAPL
'''
'''
但是,要得到最小值的话,还需要额外执行一次查找.例如:
'''

print(prices[min(prices, key=lambda k: prices[k])])
print(prices[max(prices, key=lambda k: prices[k])])

'''
利用了zip()的解决方案是将字典的键-值对 reverse 为 值-键对序列化来解决这个问题的.
当在这样的元组上比较操作时,值会先进行比较,然后才是键.这完全符合我们的期望,允许我们用一条单独的语句轻松的对字典的内容做整理和排序.
应该要注意的是,当涉及(value,key)的比较时,如果碰巧多个条目拥有相同的value,那么此时key将用来判定结果的依据.例如,在计算min(
)和max()时,如果碰巧value的值相同,则将返回拥有最小或最大key值的那个条目.示例如下:
'''
prices = {
    'AAA' : 45.23,
    'ZZZ' : 45.23,
}
print(min(zip(prices.values(),prices.keys())))
print(max(zip(prices.values(),prices.keys())))

'''
(45.23, 'AAA')
(45.23, 'ZZZ')
'''

