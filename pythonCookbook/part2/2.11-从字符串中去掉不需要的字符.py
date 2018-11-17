#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/11/17

'''
question:
我们想在字符串的开始,结尾或中间去掉不需要的字符,比如说空格
'''

'''
解决问题:
strip()方法可用来从字符串的开始和结尾处去掉字符.lstrip()和rstrip(
)可分别从左或从右侧开始执行去除字符串的操作.默认情况下这些方法去除的空格符,但也可以指定其他的字符.例如:
'''

#Whitespace stripping
s = ' hello word \n'

print(s.strip())

print(s.lstrip())

print(s.rstrip())

'''
运行结果如下:
hello word
hello word 

 hello word
'''

#Character stripping

t = '-----hello===='
print(t.lstrip('-'))
print(t.rstrip('='))
print(t.strip('-='))

'''
运行结果如下:
hello====
-----hello
hello
'''

'''
讨论:
当我们读取并整理数据以待稍后的处理时常常会用到这类strip()方法.例如,可以用它们来去掉空格,移除引号等.
需要注意的是,去除字符的操作并不会对位于字符串中间的任何文本起作用.例如:
'''
s = ' hello     world      \n'

s = s.strip()

print(s)

'''
运行结果如下:

hello     world

'''
'''
如果要对里面的空格执行某些操作,应该使用其他技巧,比如使用replace()方法或者正则表达式替换.例如:
'''
print(s.replace(' ',''))

import re

print(re.sub('\s+',' ',s))

'''
运行结果如下:

helloworld
hello world

'''

'''
我们通常会遇到的情况是将去除的操作同某些迭代操作结合起来,比如,从文件中读取文本行.如果是这样的话,那就到了生成器表达式大显身手的时候了.例如:
'''

with open('2.11-从字符串中去掉不需要的字符.py',mode='r',encoding='utf-8') as f:
    lines = (line.strip() for line in f)
    for line in lines:
        print(line)

'''
运行结果如下:

略

'''

'''
这里表达式lines = (line.strip() for line in f)的作用是完成数据的转换.它很高效,
因为这里并没有先将数据读取到任何形式的临时列表中.它只是创建一个迭代器,在所有产生出的文本行上都会执行strip操作.
对于更高级的strip操作,应该使用translate()方法,请参见下一节获得进一步的细节.
'''

