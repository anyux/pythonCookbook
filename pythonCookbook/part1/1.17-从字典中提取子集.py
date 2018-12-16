#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/12/16

'''
question:
创建一个字典,其本身是另一个字典的子集.
'''

'''
解决方案:
利用字典推导式(dictionary comprehension)可轻松解决.例如:
'''
prices = {
    'ACME' : 45.23,
    'AAPL' : 612.78,
    'IBM'  : 205.55,
    'HPQ'  : 37.20,
    'FB'   : 10.75,
}

# Make a dictionary of all prices over 200

p1 = {    key:value for key, value in prices.items() if value > 200 }
print(p1)

# Make a dictionary of tech stocks

tech_names = {
    'AAPL' , 'IBM', 'HPQ', 'MSFT'
}

p2 = {key:value for key,value in prices.items() if key in tech_names}
print(p2)

'''
讨论:
大部分可以用字典推导式解决也可以通过创建元组序列然后将它们传给dict()函数来完成.例如:
'''
p1 = dict((key,value) for key, value in prices.items() if value > 200 )

print(p1)
'''
但是字典推导式的方案更加清晰,而且实际运行起来也要快很多(以本例中的字典prices来测试,效率要高2倍多).
有时候会有多种方法来完成同一件事情.例如,第二个例子还可以重写成:
'''
# Make a dictionary of tech stocks

tech_names = {
    'AAPL','IBM','HPQ','MSFT'
}

p2 = {key:prices[key] for key in prices.keys() & tech_names}
print(p2)

'''
但是,计时测试表明这种解决方案几乎要比延续一种慢上1.6倍.如果需要考虑性能因素,那么通常都需要一点时间来研究它.有关计时和性能分析方面的信息.参见14.13节
'''



