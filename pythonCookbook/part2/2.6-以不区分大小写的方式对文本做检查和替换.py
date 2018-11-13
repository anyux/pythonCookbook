#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/11/13

'''
question:
我们需要以不区分大小写的形式对文本进行查找和替换
'''

'''
解决方案:
要进行不区分大小写的文本操作,我们需要使用re模块并且对各种操作都要加上re.IGNORECASE标记.例如:
'''
import re

text = 'UPPER PYTHON, lower python, Mixed Python'
print(re.findall('python',text,flags=re.IGNORECASE))

print(re.sub('python','snake',text,flags=re.IGNORECASE))

'''
运行结果如下:

['PYTHON', 'python', 'Python']
UPPER snake, lower snake, Mixed snake

'''

'''
上面这个例子提示了一种局限,那就是待替换的文本与匹配的文本大小写并不吻合.如果想修正这个问题,需要用到一个支撑函数(support function),示例如下:
'''
def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace

# 下面使用这个函数的例子:

print(re.sub('python',matchcase('snake'),text,flags=re.IGNORECASE))

'''
运行结果如下:

UPPER SNAKE, lower snake, Mixed Snake

'''

'''
讨论:
对于简单的情况,只需要加上re.IGNORECASE标记就足以进行不区分大小写的匹配操作了.但请注意的是这对于某些涉及大写转换(case folding)的Unicode匹配来说可能是不够的.细节参见2.10-用正则表达式处理Unicode字符
    '''








''
