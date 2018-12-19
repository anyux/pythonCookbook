#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 18-12-18

'''
Perblem:
You need to perform accurate calculations with decimal numbers, and
 don't want the small errors that naturally occur with floats.
'''

'''
Solution:
A well-known issue with floating-point numbers is that they can't 
accurately represent all base-10 decimals. Moreover, even simple 
mathematical calculations introduce small errors. For example:
'''
a = 4.2
b = 2.1
print(
    a+b
)

print(
    (a + b) == 6.3
)
'''
6.300000000000001
False
'''


'''
These errors are a 'feature' of the underlying CPU and the IEEE 754
 arithmetic performed by its floating-point unit. Since Python's float
  data type stores data using the native representation,there's nothing
   you can do to avoid such errors if you write your code using float instances.
   if you want more accuracy(and are willing to give up some performance),you can use the decimal moduel:
'''
from decimal import Decimal

a = Decimal('4.2')
b = Decimal('2.1')

print(a+b)
print(
    (a+b) == Decimal('6.3')
)
'''
6.3
True
'''

'''
At first glance,it might look a little weird(i.e.,specifying numbers as strings).However,Decimal objects work in every way that you would expect them to(supporting all of the ususal math operations,etc.).if you print them or use them in string formatting functions,the look like normal numbers.
A major feature of decimal is that allows you to control different aspects of calculations,including number of digits and rounding.To do this,you create a local context and chage its settings.For example:
'''
from decimal import localcontext
a = Decimal('1.3')
b = Decimal('1.7')
print(a/b)

with localcontext() as ctx:
    ctx.prec = 3
    print(a/b)
'''
0.7647058823529411764705882353
0.765
'''
with localcontext() as ctx:
    ctx.prec = 50
    print(a/b)
'''
0.76470588235294117647058823529411764705882352941176
'''

'''
Discussion:
The decimal module implements IBM's "General Decimal Arithmetic Specification".Needles to say, there are a huge number of configuation optins that are beyond the scope of this book.
Newcomers to Python might be inclied to use the decimal module to work around perceived accuracy problems with the float data type. However,it's really important to understand your application domain.If you're working with science or engineering problems, computer graphic, or most things of a scentific nature,it's simply more common to use the normal floating-point type.For one,very few things in the real world are mesaured to the 17digtits of accuracy that floats provide.Thus,tiny errors introduced in calcutions just don't matter.Second,the performace of native flaots is significantly faster -somthing that's important if you're performing a large number of calculations.
That said,you can't ignore the errors completely.Mathematicians have spent a lot of time studying various algorithms,and some handle errors better than others.You also have to be a little careful with effects due to things such as subtractive cancellation and adding large and small numbers together.For example:
'''

nums = [1.23e+18, 1, -1.23e+18]
print(
    sum(nums) #Notice how 1 disappears
)

'''
0.0
'''
'''
This latter example can be addressed by using a more accurate implementation in math.fsum():
'''
import math

print(
    math.fsum(nums)
)
'''
1.0
'''
'''
However,for other algorithms, you really need to study the algorithm and understand its error propagation properties.
All of this said, the main use of the decimal module is in programs involving things such as finance. In such programs, it's extremely annoying to have small errors creep into the calculation.Thus,decimal provides a way to avoid that.It is also common to envounter Decimal objects when Python interfaces with databases--agin,especially when accessing financial data.
'''










