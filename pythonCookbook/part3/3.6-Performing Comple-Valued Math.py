#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/12/25

'''
Problem
Your code for interacting with the latest web authentication scheme has encountered a singularity and your only solution is to go around it int he comple plane.Or maybe you just need to perform some calculations using complex numbers.
'''
'''
Solution:
Complex numbers can be specified using the comple(real,imag) function or bye floating-point numbers with a j suffix. For example:
'''
a = complex(2,4)
b = 3 - 5j
print(a)
print(b)
'''
(2+4j)
(3-5j)
'''

'''
The real,imaginary,and conjugate vlaues are easy to abtain, as shown here:
'''
print(a.real)

print(a.imag)

print(a.conjugate())
'''
2.0
4.0
(2-4j)
'''

'''
In addition, all of the usual meathematical operators work:
'''
print(a+b)

print(a*b)

print(a/b)

print(abs(a))


'''
(5-1j)
(26+2j)
(-0.4117647058823529+0.6470588235294118j)
4.47213595499958
'''

'''
To perform additional complex-valued functions such as sines,cosines,or square roots,use the cmath module:
'''
import cmath

print(
    cmath.sin(a)
)

print(
    cmath.cos(a)
)

print(
    cmath.exp(a)
)
'''
(24.83130584894638-11.356612711218174j)
(-11.36423470640106-24.814651485634187j)
(-4.829809383269385-5.5920560936409816j)
'''

'''
Discussion:
Most of Python's math-related moduels are aware of complex values.For example,if you use numpy,it is straightforward to make arrays of complex values and perform operations on them:
'''

import numpy as np

a = np.array(
    [2+3j,4+5j,6-7j,8+9j]
)
print(a)
'''
[2.+3.j 4.+5.j 6.-7.j 8.+9.j]
'''

print(
    a+2
)

print(
    np.sin(a)
)

'''
[ 4.+3.j  6.+5.j  8.-7.j 10.+9.j]
[   9.15449915  -4.16890696j  -56.16227422 -48.50245524j
 -153.20827755-526.47684926j 4008.42651446-589.49948373j]
'''

'''
Python's standard matchmatical functions do not produce complex values by default, so it is unlikely that such a value would accedentally show up in your code.For example:
'''
import math

'''
math.sqrt(-1)
'''
'''
If you want complex numbers to be produced as r rsult,you have to explicityly use cmapth or declare the use of a complex type in libraries that know about them.For example:
'''
import cmath
print(
    cmath.sqrt(-1)
)

'''
1j
'''








