#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/11/19

'''
question:
我们想创建一个字符串,其中嵌入的变量名称会以变量的字符串值形式替换掉.
'''
'''
解决方案:
Python并不直接支持在字符串中对变量做简单的值替换.但是,这个功能可以通过字符串的format()方法近似模拟出来.示例如下:
'''
s = '{name} has {n} messages.'
print(s.format(name='Guido',n = 37))
'''
Guido has 37 messages.
'''
'''
另一种方法是,如果要被替换的值确实能在变量中找到,则可以将format_map()和vars()联合起来使用,示例如下:
'''
name = 'Guido'
n = 37

print(s.format_map(vars()))

'''
Guido has 37 messages.
'''
'''
有关vars()的一个微妙的特性是它也能作用于类实例上.比如:
'''
class Info:
    def __init__(self,name,n):
        self.name = name
        self.n = n

a = Info('Guido',37)
print(s.format_map(vars(a)))

'''
Guido has 37 messages.
'''

'''
而format()和format_map()的一个缺点是没法优雅地处理缺少某个值的情况,例如:
'''
# s.format(name='Guido')
'''
raceback (most recent call last):
File "E:/xxx/part2/2.15-给字符串中的变量名做插值处理.py", line 48, in <module>
    s.format(name='Guido')
KeyError: 'n'
'''
'''
避免这种情况出现的一种方法是单独定义一个带有__missing__()方法的字典类,示例如下:
'''
class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'

'''
现在用这个类来包装传给format_map()输入参数:
'''
del n #Make sure n is undefined

print(s.format_map(safesub(vars())))
'''
Guido has {n} messages.
'''
'''
如果发现自己在代码中常常需要执行这些步骤,则可以将替换变量的过程隐藏在一个小型的功能函数内,这里需要采用一种称之为"frame hack"的技巧.示例如下:
frame hack:
    即需要同函数的栈帧打交道.sys._getframe这个特殊的函数可以让我们获得调用函数的栈信息.
'''
import sys

def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))

'''
现在我们可以这样编写代码了:
'''
name = 'Guido'
n = 37

print(sub('Hello {name}'))

print(sub('You have {n} messages.'))

print(sub('Your favrite color is {color}'))

'''
运行结果如下:

Hello Guido
You have 37 messages.
Your favrite color is {color}

'''
'''
讨论:
多年来,由于python缺乏真正的变量插值功能,由此产生了各种解决方案.作为本节中已给出的解决方案的替代,有时候我们会看到类似下面代码中的字符串格式化操作:
'''
name = 'Guido'
n = 37

print("%(name)s has %(n)s message." % vars())

'''
Guido has 37 message.
'''

'''
我们可能还会看到模板字符串(template string)的使用:
'''
import string

s = string.Template('$name has $n message.')
print(s.substitute(vars()))
'''
Guido has 37 message.
'''
'''
但是,format()和format_map()方法比上面这些替代方案都要更加现代化,我们应该将其作为首选.使用format(
)的一个好处是可以同时得到所有关于字符串格式化方面的能力(对齐,填充,数值格式化等),而这些功能在字符串模板对象上是不可能做到的.
在李的部分内容中还提到了一些有趣的高级特性.字典类中鲜为人知的__missing__()方法可用来处理缺少值时的行为.在safesub类中,
我们将该方法定义为将缺失的值以占位符的形式返回,因此这里不会抛出KeyError异常,缺少的那个值会出现在最后生成的字符串中(可能对调试有些帮助).
sub()函数使用了sys._getframe(1)来返回调用方法的栈帧.通过访问属性 f_locals来得到局部变量.无需多言,
在大部分代码中都应该避免去和栈帧打交道,但是对于类似完成字符串替换功能的函数来说,这会是有用的.插一句题外话,值得指出的是f_locals是一个字典,
它完成对调用函数中局部变量的拷贝.尽管访问不同的栈帧可能看起来是很邪恶的,但是意外地覆盖或修改调用方的本地环境也是不可能的.
'''