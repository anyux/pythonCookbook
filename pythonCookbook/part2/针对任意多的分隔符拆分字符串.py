#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/11/10

'''
question:
我们需要将字符串拆分为不同的字段，但分隔符(以及分隔符之间的空格)在整个字符串中并不一致

'''

'''
解决方案
字符串对象split()方法只能处理简单的情况，而且不支持多个分隔符，对分隔符周围可能存在的空格也无能为力.当需要更为灵活的功能时，需要使用re
.split()方法:
'''
import re

line = 'asdf fjdk; afed, fjek,asdf,    foo'

res = re.split(r'[;,\s]\s*',line)
print(res)
'''
执行结果:
['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
'''

'''
discuss:
re.split()是很有用的，因为可以为分隔符设置多个模式。例如，上面解决方案中，分隔符可以设置为逗号、分号，或者空格(
后面可跟任意数量的额外空格).只要找到对应的模式,无论匹配的两端是什么字段,整个匹配的结果就成为那个分隔符.最终得到的结果是字段列表,
同str.split()得到的结果一样.

当使用re.split()时,需要小心正则表达表达式模式中的捕获组(capture group)是否包含在括号中.如果用到了捕获组,
那么匹配的文本也会包含在最终的结果中.比如下面的情况:

'''
field = re.split(r'(;|,|\s)\s*',line)
print(field)

'''
运行结果:
['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']
'''

'''
特定的上下文获取到分隔字符也可能是有用的.例如,使用分隔符改进字符串的输出
'''

value = field[::2]

delimiters = field[1::2] + ['']

print(value)

print(delimiters)

print(''.join(v+d for v,d in zip(value,delimiters)))


'''
输出结果依次为:
['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
[' ', ';', ',', ',', ',', '']
asdf fjdk;afed,fjek,asdf,foo

'''

'''
如果不想是结果中看到分隔符,但仍然想用括号来对正则表达式模式匹配进行分组,请确保用的是非捕获组,以(?:...)的形式指定.示例如下:
'''

not_include_patterns = re.split(r'(?:,|;|\s)\s*',line)

print(not_include_patterns)

'''
输出结果为:
['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
'''















