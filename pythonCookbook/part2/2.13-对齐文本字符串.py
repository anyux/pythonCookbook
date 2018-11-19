#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/11/19

'''
question:
我们需要以某种对齐方式将文本做格式化处理
'''
'''
解决方案:
对于基本的字符串要求,可以使用字符串的ljust(),rjust(),center()方法,基本示例如下:
'''
text = 'hello world'
print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))

'''
运行结果如下:
hello world         
         hello world
    hello world     
'''
'''
所有这些方法都可接受一个可选的填充字符:
'''
print(text.rjust(20,'='))
print(text.center(20,'*'))

'''
=========hello world
****hello world*****
'''

'''
format()函数也可以轻松完成对齐任务.需要做的就是合理利用'<','>',或'^'字符以及一个期望的宽度值.例如:
注解:
    '>' 表示右对齐
    '<' 表示左对齐
    '^' 表示剧中对齐
    这些字符称为对齐字符
'''

print(format(text,'>20'))

print(format(text,'<20'))

print(format(text,'^20'))

'''
运行结果如下:

         hello world
hello world         
    hello world     
'''
'''
如果想包含空格之外的填充字符,可以在对齐字符之前指定:
'''
print(format(text,'=>20'))

print(format(text,'=<20'))

print(format(text,'*^20'))

'''
运行结果如下:
=========hello world
hello world=========
****hello world*****
'''

'''
当格式化多个值时,这些格式化代码也可以用在format()方法中.例如:
'''

print('{:>10s} {:>10s}'.format('Hello','word'))

'''
     Hello       word
'''
'''
format()好处之一是它并不是特定于字符串的.它能作用于任何值,这使得它更加通用.例如,可以对数字做格式化处理.
'''

x = 1.2345

print(format(x,'>10'))

print(format(x,'^10.2f'))

'''
运行结果如下:

    1.2345
   1.23   
'''

'''
讨论:
在比较老的代码中,通常会发现%操作符用来格式化文本.例如:
'''
print('%-20s' % text)

print('%20s' % text)

'''
hello world         
         hello world
'''
'''
但是在新的代码中,我们应该会更钟情于使用format()函数或方法.format()比%操作符提供的功能要强大多了.此外,format(
)可作用于任意类型的对象,比字符串的ljust(),rjust()及center()方法要更加通用.想了解format()函数的所有功能,
请参考Python的在线手册http://docs.python.org/3/library/string.html/#formatspec
'''