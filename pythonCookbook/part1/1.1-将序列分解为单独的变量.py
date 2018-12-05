#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/11/22

'''
question:
我们有一个包含N个元素的无组或序列,现在想将它分解为N个单独的变量.
'''
'''
解决方案:
任何序列(或可迭代的对象)都可以通过一个简单的赋值操作来分解为单独的变量.唯一的要求是变量的总数和结构要与序列想吻合.例如:
'''
p = (4,5)
x,y = p

print(x)
print(y)

'''
4
5
'''
data = ['ACME',50,91.1,(2012,12,21)]
name,shares,price,date=data
print(name)
print(shares)
print(price)
print(date)

'''
ACME
50
91.1
(2012, 12, 21)
'''
name,shares,price,(year,mon,day)=data

print(year)
print(mon)
print(day)

'''
2012
12
21
'''

'''
如果元素的数量不匹配,将得到一个错误提示.例如:
>>> p = (4,5)
>>> x,y,z = p
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: not enough values to unpack (expected 3, got 2)
'''
'''
讨论:
实际上不仅仅是元组或列表,只要对象恰好是可迭代的,那么就可以执行分解操作.这包括字符串,文件,迭代器以及生成器.比如:
'''
s = 'Hello'
a,b,c,d,e = s
print(a)
print(b)
print(e)
'''
H
e
o
'''
'''
当分解操作时,有时候可能想丢弃某些特定的值.Python并没有提供特殊的语法来实现这一点,但是通常可以选一个用不到变量名,以此来作为要丢弃的值的名称.
例如:
'''
data = ['ACME',50,91.1,(2012,12,21)]
_,shares,price,_=data
print(shares)
print(price)

'''
50
91.1
'''
'''
但请确保此变量名在其他地方没有使用过
'''
















'''
'''