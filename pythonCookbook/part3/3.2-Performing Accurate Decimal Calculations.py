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
  data type sotre data using the native representation,there's nothing
   you can do to avoid such erro
'''













