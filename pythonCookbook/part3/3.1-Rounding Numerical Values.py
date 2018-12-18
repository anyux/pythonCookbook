#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/12/18

'''
Perblem:
You want to round a floating-point number to a fixed number of decimal places.
'''
'''
Solution:
For simple rounding,use the built-in round(value, ndigits)function.For example:
'''
print(
    round(
        1.23, 1
    )
)
'''
1.2
'''
print(
    round(
        1.27, 1
    )
)
'''
1.3
'''
print(
    round(
        -1.27, 1
    )
)
'''
-1.3
'''
print(
    round(
        1.25361, 3
    )
)
'''
1.254
'''
'''
when a value is exactly halfway between two choices, the behavior of round is to round to the nearest even digit. That is, values such as 1.5 or 2.5 both get rounded to 2.
'''
