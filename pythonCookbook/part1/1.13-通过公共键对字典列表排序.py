#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/12/6

'''
question:
我们有一个字典列表,想根据一个或多个字典中的值来对列表排序.
'''

'''
解决方案:
利用operator模块中的itemgetter函数对这类结构进行排序是非常简单的,假设通过查询数据库表项获取网站的成员列表,我们得到了如下的数据结构:
'''

rows = [
    {'fname':'Brain','lname':'Jones','uid':1003},
    {'fname':'David','lname':'Beazley','uid':1002},
    {'fname':'John','lname':'Cleese','uid':1001},
    {'fname':'Big','lname':'Jones','uid':1004},
]

'''
根据所有的字典中共有的字段来对这些记录排序是非常简单的,示例如下:
'''

from operator import itemgetter

rows_by_fname = sorted(rows,key=itemgetter('fname'))
rows_by_lname = sorted(rows,key=itemgetter('lname'))
print(rows_by_fname)
print(rows_by_lname)

'''
[{'fname': 'Big', 'lname': 'Jones', 'uid': 1004}, 
{'fname': 'Brain', 'lname': 'Jones', 'uid': 1003}, 
{'fname': 'David', 'lname': 'Beazley', 'uid': 1002}, 
{'fname': 'John', 'lname': 'Cleese', 'uid': 1001}]

[{'fname': 'David', 'lname': 'Beazley', 'uid': 1002}, 
{'fname': 'John', 'lname': 'Cleese', 'uid': 1001}, 
{'fname': 'Brain', 'lname': 'Jones', 'uid': 1003}, 
{'fname': 'Big', 'lname': 'Jones', 'uid': 1004}]
'''
'''
itemgetter()函数还可以接受多个键.例如下面这段代码:
'''
rows_by_lfname = sorted(rows,key=itemgetter('lname','fname'))
print(rows_by_lfname)

'''
[{'fname': 'David', 'lname': 'Beazley', 'uid': 1002}, 
{'fname': 'John', 'lname': 'Cleese', 'uid': 1001}, 
{'fname': 'Big', 'lname': 'Jones', 'uid': 1004}, 
{'fname': 'Brain', 'lname': 'Jones', 'uid': 1003}]
'''

'''
讨论:
在这个例子中,rows被传递给内建的sorted()函数,该函数接受一个关键字参数key.这个参数应该代表一个可调用对象(callable).该对象从rows中接受一个可调用对象(callable),该对象从rows中接受一个单独的元素作为输入并返回一个用来做排序依据的值.itemmetter()函数创建的就是这样一个可调用对象.
函数operator.itemgetter()接受参数可作为查询的标记,用来从rows的记录中提取出所需要的值.它可以是字典的键名称,用数字表示的列表元素或是任何可以传给对象的__getitem__()方法的值.如果传多个标记给itemgetter(),那么它产生的可调用对象将返回一个包含所有元素在内的元组,然后,sorted()将根据对元组的排序结果来排列输出结果.如果想同时针对多个字段做排序(比如例子中的姓和名),那么就是非常有用的.
有时候会用lambda表达式来取代itemgetter()的功能.例如:
'''
rows_by_fname = sorted(rows,key=lambda r:r['fname'])
rows_by_lname = sorted(rows,key=lambda r:r['lname'])
print(rows_by_fname)
print(rows_by_lname)
'''
[{'fname': 'Big', 'lname': 'Jones', 'uid': 1004}, {'fname': 'Brain', 'lname': 'Jones', 'uid': 1003}, {'fname': 'David', 'lname': 'Beazley', 'uid': 1002}, {'fname': 'John', 'lname': 'Cleese', 'uid': 1001}]
[{'fname': 'David', 'lname': 'Beazley', 'uid': 1002}, {'fname': 'John', 'lname': 'Cleese', 'uid': 1001}, {'fname': 'Brain', 'lname': 'Jones', 'uid': 1003}, {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}]
'''

'''
这种解决方案通常也能正常工作.但是用Itemgetter()通常会运行得更快一些.因此如果需要考虑性能问题,应该使用itemgetter().
最后不要忘记本节中所展示的技术同样适用于min()和max()这样的函数.例如:
'''

print(min(rows,key=itemgetter('fname')))
print(min(rows,key=itemgetter('lname')))
'''
{'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
{'fname': 'David', 'lname': 'Beazley', 'uid': 1002}
'''




