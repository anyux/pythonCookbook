#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/11/10

'''
question:
我们需要在字符串的开头或结尾处按照指定的文本模式做检查,例如检查文本扩展名,URL协议类型等
'''

'''
解决方案:
有一种简单的方法来检查字符串的开头或结尾,只要使用str.startswith()或str.endswith()方法就可以了,示例如下:
'''

filename = 'spam.txt'
print(filename.endswith('.txt'))

print(filename.startswith('file:'))

url = 'http://www.python.org'

print(url.startswith('http:'))


'''
输出结果依次为:
True
False
True
'''

'''
如果需要同时针对多个选项做检查,只需给startswith()和endswith()提供包含可能选项的元组即可:
'''

import os

filenames = os.listdir('.')
print(filenames)

check_mutil_file = [name for name in filenames if name.endswith(('.c','.py')) ]
print(check_mutil_file)

is_container_file = any(name.endswith('.py') for name in filenames)
print(is_container_file)

'''
输出结果依次为:

['在字符串开头或结尾处做文本匹配.py', '针对任意多的分隔符拆分字符串.py']

['在字符串开头或结尾处做文本匹配.py', '针对任意多的分隔符拆分字符串.py']

True
'''

'''
这里有另一个例子:
'''

from urllib.request import urlopen

def read_data(name):
    if name.startswith(('http:','https:','ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()

'''
奇怪的是,这是python中需要把元组当成输入的一个地方.如果我们刚好把指定在了列表里或集合中,请确保首先用tuple()将它们转换成元组.示例如下:
'''

choice = ['http:','ftp:']
url = 'http://www.python.org'
# 注:这里使用异常处理使用文件正常运行
try:
    print(url.startswith(choice))
except Exception  as err:
    print(err)

print(url.startswith(tuple(choice)))

'''
输出结果如下:

注:这里使用异常处理使用文件正常运行
startswith first arg must be str or a tuple of str, not list


True
'''

'''
discuss:
startswith()和endswith()提供了一种非常方便的方式来对字符串的前缀和后缀做基本的检查.类似的操作也可以用切片来完成,
但是那样方案不够优雅.例如:
'''
filename = 'spam.txt'
print(filename[-4:] == '.txt')

url = 'http://www.python.org'
print(url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp:')

'''
使用切片匹配结果如下:
True
True

'''

'''
可能我们也比较倾向于使用正则表达式作为替代方案.例如:
'''

import re

url = 'http://www.python.org'
print(re.match(r'http:|https:|ftp:',url))

'''
运行结果如下:
<_sre.SRE_Match object; span=(0, 5), match='http:'>
'''

'''
这也行得通,但是通常对于简单的匹配过于重量级了.使用本节提到的技术会更简单,运行得也会更快.
最好同样重要的是,当startswith()和endswith()方法和其他操作(比如常见的数据整理操作)结合起来时效果也很好.例如,
下面的检查目录中有无出现特定的文件:
'''

if any(name.startswith(('.c','.py')) for name in os.listdir('.')):
    pass














