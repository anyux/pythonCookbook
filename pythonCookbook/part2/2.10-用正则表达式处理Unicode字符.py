#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/11/16

'''
question:
我们正在用正则表达式处理文本,但是需要考虑处理Unicode字符.
'''
'''
解决问题:
默认情况下re模块已经对某些Unicode字符类型有了基本的认识.例如,\d已经可以匹配任意Unicode数字字符了:
'''
import re

num = re.compile('\d+')

#ASCII digits

print(num.match('123'))

#Arabic digits
print(num.match('\u0661\u0662\u0663'))

'''
运行结果如下:

<_sre.SRE_Match object; span=(0, 3), match='123'>
<_sre.SRE_Match object; span=(0, 3), match='١٢٣'>

'''
'''
如果需要在在模式字符串中包含指定的Unicode字符,可以针对Unicode字符使用转义字符(例如\uFFFF或'''#\UFFFFFF   ).比如,
'''这里有一个正则表达式能在多个不同的阿拉伯代码页中匹配所有的字符:
'''

arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')
print(arabic)

'''
re.compile('[\u0600-ۿݐ-ݿࢠ-ࣿ]+')
'''
'''
当执行匹配和搜索操作时,一个好主意是首先将所有的文本都统一表示为标准形式(见2.9).但是,同样重要的是需要注意一些情况.例如,
当不区分大小写的匹配和大写转换(case folding)匹配联合起来时,考虑会出现什么行为:
'''
pat = re.compile('stra\u00dfe',re.IGNORECASE)
s = 'straße'
print(pat.match(s))

print(pat.match(s.upper())) #没有匹配到内容

print(s.upper())
'''
运行结果如下:
<_sre.SRE_Match object; span=(0, 6), match='straße'>
None
STRASSE
'''

'''
讨论:
把Unicode和正则表达式混在一起使用绝对是让人头痛欲裂的办法.如果真的要这么做,应该考虑安装第三方的正则表达式库(
http://pypi.python.org/pypi/regex),这些第三方正则库针对Unicode大写转换提供了完整的支持,
还包含其他各种有趣的特性,包括近似匹配
'''