#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/12/12

'''
question:
序列中含有一些数据,我们需要提取出其中的值或根据某些标准对序列做删减.
'''
'''
解决方案:
要筛选序列中的数据,通常是简单的方法是使用列表推导式(list comprehension)例如:
'''
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print([n for n in mylist if n>0])
print([n for n in mylist if n<0])
'''
[1, 4, 10, 2, 3]
[-5, -7, -1]
'''
'''
使用列表推导式的一个潜在缺点是如果原始输入非常大,这么做可能会产生一个大的结果集.此时建议使用  生成器表达式  通过 迭代方式产生筛选结果.例如:
'''
poss = (n for n in mylist if n>0)

print(poss)

for x in poss:
    print(x)
'''
<generator object <genexpr> at 0x0000028C3A5EABA0>
1
4
10
2
3
'''

'''
有时候筛选的标准没法简单地表示在列表推导式或生成器表达式中.比如,假设筛选过程涉及异常处理或者其他一些复杂的细节.基于此,可以将处理筛选逻辑的代码放到单独的函数中.然后使用内建的filter()函数处理.示例如下:
'''
values = ['1', '2', '-3', '-', '4', 'N/A', '5']

def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

values = list(filter(is_int,values))
print(values)
'''
['1', '2', '-3', '4', '5']
'''
'''
filter创建了一个迭代器,因此如果我们想要的是列表形式的结果,请确保加上了list(),就像示例中那样.
'''

'''
讨论:
列表推导式和生成器表达式通常是用来筛选数据的最简单和最直接的方式.此外,它们还具有同时对数据做转换的能力.例如:
'''

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
import math
res =(math.sqrt(n) for n in mylist if n>0)
for num in res:
    print(num)
'''
1.0
2.0
3.1622776601683795
1.4142135623730951
1.7320508075688772
'''

'''
关于筛选数据,有一种情况是用新值替换掉不满足标准的值,而不丢弃它们.例如,除了要找到正整数之外,我们也许还希望在指定的范围内将不满足要求的值替换掉.通常,这可以通过将筛选条件移到一个条件表达式中来轻松实现.就像下面这样:
'''
clip_neg = (n if n > 0 else 0 for n in mylist)
for num in clip_neg:
    print(num)
'''
1
4
0
10
0
2
3
0
'''


clip_neg = (n if n < 0 else 0 for n in mylist)
for num in clip_neg:
    print(num)

'''
0
0
-5
0
-7
0
0
-1
'''

'''
另一个值得一提的筛选工具是itertools.compress(),它接受一个可迭代对像以及一个布尔选择器序列作为输入.输出时,它会给出所有在相应的布尔选择器中为True的可迭代对象元素.如果想把一个序列的筛选结果施加到另一个相关的序列上时,这就会非常有用.例如,假设有以下两列数据:
'''

address = [
'5412 N CLARK',
'5148 N CLARK',
'5800 E 58TH',
'2122 N CLARK',
'5645 N RAVENSWOOD',
'1060 W ADDISON',
'4801 N BROADWAY',
'1039 W GRANVILLE',
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]

'''
现在我们想构建一个地址列表,其中相应的count值要在于5.下面是我们可以尝试的方法:
'''

from itertools import compress

more5 = [n>5 for n in counts]
print(more5)

print(
    list(compress(address,more5))
)
'''
[False, False, True, False, False, True, True, False]
['5800 E 58TH', '1060 W ADDISON', '4801 N BROADWAY']
'''

'''
这里的关键在于首先创建一个布尔序列,用来表示哪个元素可满足我们的条件.然后compress()函数挑选出满足布尔值为True的相应元素.
同filter()函数一样,正常情况下compress()会返回一个迭代器.因此,如果需要的话,得使用list()将结果转换为列表.
'''








