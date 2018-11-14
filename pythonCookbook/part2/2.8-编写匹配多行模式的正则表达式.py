#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/11/14

'''
问题:
我们打算用正则表达式对一段文本块做匹配,但是希望在进行匹配时能够跨越多行
'''

'''
解决方案:
这个问题出现在希望使用句点(.)来匹配任意字符,但是忘记了句点并不能匹配换行符.例如,假设想匹配C语言风格的注释:
'''
import re
comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a 
              mutiline comment */

'''
print(comment.findall(text1))
print(comment.findall(text2))

'''
运行结果如下:

[' this is a comment ']
[]

'''

'''
要解决这个问题,可以添加对换行符的支持.示例如下:
'''

comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment.findall(text2))

'''
运行结果如下:

[' this is a \n              mutiline comment ']

'''

'''
在这个模块中,(?:.\n)指定一个非捕获组(即,这个组只做匹配但不捕获结果,也不分配组号)
'''
'''
讨论:
re.compile()函数可接受一个有用的标记----re.DOTALL.这使得正则表达式中的句点(.),可以匹配所有的字符,也包括换行符.例如:
'''
comment = re.compile(r'/\*(.*?)\*/',re.DOTALL)
print(comment.findall(text2))

'''
运行结果如下:

[' this is a \n              mutiline comment ']

'''

'''
对于简单的情况,使用re.DOTALL标记可以得到很好地完成工作.但是如果要处理极其复杂的模式,或者面对2.18中所描述的分词(
tokenizing)而将单独的正则表达式全并在一起的情况,如果可以选择的话,通常更好的方法是定义自己的正则表达式模式,这样它无需额外的标记也能正确工作.
'''
