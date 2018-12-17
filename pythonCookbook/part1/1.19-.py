#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 18-12-18

'''
question:

'''

'''

'''

nums = [1, 2, 3, 4, 5]
s = sum(
    x * x for x in nums
)

print(s)
'''
55
'''

# Determine if any .py files exist in a directory

import os
files = os.listdir('.')
if any(name.endswith('.py')  for name in files):
    print(
        'There be python'
    )
else:
    print(
        'Sorry, no python'
    )

#output a tuple as CSV

s = ('ACME', 50, 123.45)

print(','.join(str(x) for x in s))

'''
There be python
ACME,50,123.45
'''

# Data reduction across fields of a data structure



