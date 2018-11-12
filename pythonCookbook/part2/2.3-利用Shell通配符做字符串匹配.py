#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/11/12

'''
question:
当工作在UNIX Shell 下时,我们想使用常见的通配符模式(即,*P.py,Dat[0-9]*.csv等]来对文本做匹配
'''

'''
解决方案:
fnmatch模块提供了两个函数---fnmatch()和fnmatchcase()----可用来执行这样的匹配.使用起来很简单:
'''
from fnmatch import fnmatch,fnmatchcase

print(fnmatch('foo.txt','*.txt'))

print(fnmatch('foo.txt','?oo.txt'))

print(fnmatch('Date45.csv', 'Dat[0-9]*'))

names = ['Dat1.csv','Dat2.csv','config.ini','foo.py']
print([name for name in names if fnmatch(name,'Dat*.csv')])

'''
运行结果如下:
True
True
False
['Dat1.csv', 'Dat2.csv']
'''

'''
一般来说,fnmatch()所采用的大小写区分规则和底层文件系统相同(根据操作系统的不同而不同).例如:
'''
#On OS X (Mac)
print(fnmatch('foot.txt', '*.TXT'))

#On Windows
print(fnmatch('foot.txt','*.TXT'))

'''
运行结果如下:
False
True
'''

'''
如果这个区别对我们而言很重要,就应该使用fnmatchcase().它完全根据我们提供的大小写方式来匹配:
'''
print(fnmatchcase('foo.txt', '*.TXT'))

'''
运行结果如下:
False
'''

'''
关于这些函数,一个常被忽略的特性是 它们在处理非文件名式的字符串时的潜在用途.例如,假设有一组街道地址,就像这样:
'''
addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY'
]

'''
可以像下面这样写列表推导式:
'''

print([addr for addr in addresses if fnmatchcase(addr,'* ST')])

print([addr for addr in addresses if fnmatchcase(addr,'54[0-9][0-9] *CLARK*')])

'''
运行结果如下:

['5412 N CLARK ST', '1060 W ADDISON ST', '2122 N CLARK ST']
['5412 N CLARK ST']

'''

'''
讨论:
fnmatch 所完成的匹配操作介于简单的字符串方法和全功能的正则表达式之间.如果只是试着在处理数据时提供一种简单的机制以允许使用能配符,
那么通常这都个合理的解决方案.
如果实际上是想编写匹配文件名的代码,那应该使用 glob 模块来完成,请参见 获取目录内容的列表
'''
