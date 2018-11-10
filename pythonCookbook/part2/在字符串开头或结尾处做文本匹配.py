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




