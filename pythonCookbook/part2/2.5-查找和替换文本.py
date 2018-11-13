#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/11/13

'''
question:
我们想到字符串的文本做查找和替换
'''

'''
解决方案:
对于简单的文本模式，使用str.replace()即可.例如:
'''
text = 'yeah, but no, but yeah, but no, but yeah'

print(text.replace('yeah','yep'))

'''
运行结果如下:

yep, but no, but yep, but no, but yep
'''

'''
针对更为复杂的模式,可以使用re模块中的sub()函数/方法.为了说明如何使用,假设我们想把日期格式从"11/27/2012"改写为 "2012-11-27".示例如下:
'''

text = 'Today is 11/27/2017. PyCon starts 3/13/2013.'
import re
print(re.sub(r'(\d+)/(\d+)/(\d+)',r'\3-\2-\1',text))

'''
运行结果如下:

Today is 2017-27-11. PyCon starts 2013-13-3.
'''
'''
sub()的第1个参数是要匹配的模式,第2个参数是要替换上的模式.类似"\3"这样的反斜线加数字的符号代表着模式中捕获组的数量.
如果打算用相同的械执行重复替换,可以将模式编译以获得好的性能.示例如下:
'''
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(r'\3-\2-\1',text))

'''
运行结果如下:

Today is 2017-27-11. PyCon starts 2013-13-3.

'''

'''
对于更复杂的情况,可以指定一个替换回调函数.示例如下:
'''
from calendar import month_abbr

def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2),mon_name,m.group(3))

datepat.sub(change_date,text)

'''
运行结果如下:

Today is 2017-27-11. PyCon starts 2013-13-3.

'''

'''
运行结果如下:

替换回调函数的输入参数是一个匹配对象,由match()或find()返回.用.group()方法来来提取匹配中特定的部分.这个函数应该返回替换后的文本.
除了得到替换后的文本外,如果还想知道一共完成了多少次替换,可以使用re.subn().例如:
'''
newtext,n = datepat.subn(change_date,text)
print(newtext)
print(n)

'''
运行结果如下:

Today is 27 Nov 2017. PyCon starts 13 Mar 2013.
2
'''

'''
讨论:
除了以上展示的sub()调用之外,关于正则表达式的查找和替换并没有什么更多可说的.最有技巧的地方在于指定正则表达式模式----这个最好的还是自己去练
'''























''
