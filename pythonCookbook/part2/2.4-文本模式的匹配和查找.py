#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/11/12

'''
question:
我们想要按特定的文本模式进行匹配或查找
'''

'''
解决方案:
如果想要匹配的只是简单的文字,那么只需要用基本的字符串方法可以了,比如 str.find(),str.endswith(),str.startswith( )或类似的函数.示例如下:
'''
text = 'yeah, but no,but yeah, but no, but yeah'

print(text == 'yeah')

print(text.startswith('yeah'))

print(text.endswith('no'))

print(text.find('no'))

'''
运行结果如下:

False
True
False
10

'''

'''
对于更为复杂的匹配规则需要使用正则表达式以及re模块.为了说明使用正则表达式的基本流程,假设我们想匹配以数字形式构成的日期,比如"11/27/2012".示例如下:
'''
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'


import re

# simple matching: \d+ means match one or more digits

if re.match(r'\d+/\d+/\d+',text1):
    print('yes')
else:
    print('no')


if re.match(r'\d+/\d+/\d+',text2):
    print('yes')
else:
    print('no')

'''
运行结果如下:

yes
no

'''

'''
如果打算针对同一种模式做多次匹配,那么通常会先正则表达式模式预编译成一个模式对象.例如:
'''
depart = re.compile(r'\d+/\d+/\d+')

if depart.match(text1):
    print('yes')
else:
    print('no')

if depart.match(text2):
    print('yes')
else:
    print('no')

'''
运行结果如下:

yes
no

'''

'''
match()方法总是尝试在字符串的开头找到匹配项.如果想针对文本搜索出所有的匹配项,那么就应该使用findall()方法.例如:
'''
text = 'Today is 11/27/2012. PyCon start3 3/13/2013.'

print(depart.findall(text))

'''
运行结果如下:

['11/27/2012', '3/13/2013']

'''

'''
当定义正则表达式时,我们常会将部分模式用括号包起来方式引入捕获组.例如:
'''
depart = re.compile(r'(\d+)/(\d+)/(\d+)')

'''
捕获组通常能简化后续对匹配文本的处理,因为每个组的内容都可以单独提取出来.例如:
'''
m = depart.match('11/27/2012')
print(m)

#Extract the contents of each group

print(m.group(0))

print(m.group(1))

print(m.group(2))

print(m.group(3))

month, day, year = m.groups()
print(month,day,year)

'''
运行结果如下:
<_sre.SRE_Match object; span=(0, 10), match='11/27/2012'>
11/27/2012
11
27
2012
11 27 2012
'''

#Find all matches (notice spliting into tupes)

print(text)

print(depart.findall(text))

for month,day,year in depart.findall(text):
    print('{}-{}-{}'.format(year,month,day))

'''
运行结果如下:

Today is 11/27/2012. PyCon start3 3/13/2013.
[('11', '27', '2012'), ('3', '13', '2013')]
2012-11-27
2013-3-13

'''

'''
findall()方法搜索整个文本并找出所有的匹配项然后将它们以列表的形式返回.如果想以迭代的方式找出匹配项,可使用finditer()方法.示例如下:
'''
for m in depart.finditer(text):
    print(m.groups())

'''
运行结果如下:

('11', '27', '2012')
('3', '13', '2013')

'''

'''
当前展示了利用re模块来对文本做匹配搜索的基础.基本功能是首先用re.compile()对模式进行编译,然后使用像match(),findall()或finditer()这样的方法做匹配和搜索.
当指定模式时我们通常会使用原始字符串,比如r'(\d+)/(\d+)/(\d+)'.这样的字符串不会对反斜线字符转义,
这在正则表达式上下文中会很有用.否则,我们需要使用双反斜线来表示一个单独的"\",例如'(\\d+)/(\\d+)/(\\d+)'.
请注意,match()方法只会检查字符串的开头.有可能出现匹配的结果并不是你想要的情况.例如:
'''
m = depart.match('11/27/2012abcdef')
print(m)
print(m.group())

'''
运行结果如下:

<_sre.SRE_Match object; span=(0, 10), match='11/27/2012'>
11/27/2012

'''

'''
如果想要精确匹配,请确保在模式中包含一个结束标记($),示例如下:
'''
depart = re.compile(r'(\d+)/(\d+)/(\d+)$')
print(depart.match('11/27/2012abcdef'))
print(depart.match('11/27/2012'))

'''
运行结果如下:

None
<_sre.SRE_Match object; span=(0, 10), match='11/27/2012'>

'''
'''
最后,如果只是想执行简单的文本匹配和搜索操作,通常可以省略编译步骤,直接使用re模块中的函数即可.例如:
'''
print(re.findall(r'(\d+)/(\d+)/(\d+)',text))

'''
运行结果如下:

[('11', '27', '2012'), ('3', '13', '2013')]

'''
'''
请注意,如果打算执行很多匹配或查找操作,
通常需要先将模式编译然后重复使用.模块级的函数会对最近编译过的模式做缓存处理因此这里并不会有巨大的性能差异.但是使用自己编译过的模式会省下一些查找步骤和额外的处理.
'''
