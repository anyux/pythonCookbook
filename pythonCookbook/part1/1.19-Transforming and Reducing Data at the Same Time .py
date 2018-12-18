#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 18-12-18

'''
Problem:
You need to execute a reduction function (e.g sum(),min(), max()),but first need to transform or filter the data.
'''

'''
Solution:
A very elegant way to combine a data reduction and transformation is to use a generator-expression argument.
For example, if you want to calcuate the sum of squares, do the following:
'''

nums = [1, 2, 3, 4, 5]
s = sum(
    x * x for x in nums
)

print(s)
'''
55
'''

'''
ere are a few other examples:
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

portfolio = [
    {'name': 'GooG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65},
]

min_shares = min(
    s['shares'] for s in portfolio
)
print(min_shares)
'''
20
'''

'''
Discussion:
The solution shows a subtle synactic aspect of generator expressions when supplied as the single argument to a function (i.e, you don't need repeated parentheses).For example, these statements are the same:
'''
s = sum(
    (    x * x for x in nums) # Pass generator-expr as argument
)
print(s)
s = sum(
    x * x for x in nums # More elegant syntax
)
print(s)

'''
55
55
'''

'''
Using a generator argument is often a more efficient and  elegant approach than first creating a temporary list. For example, if you didn't use a generator expression, you might consider this alternative implementation:
'''
nums = [1, 2, 3, 4, 5]
s = sum(
    [x*x for x in nums]
)
print(s)
'''
55
'''
'''
This works, but it introduces an extra step and creates an extra list. For such a small list, it might not matter, but if nums was huge, you would end up creating a large temporary data structure to only be used once and discarded. The generator solution transforms the data iteratively and is therefore much more memory-efficient.
Certain reduction functions such as min() and max() accept a key argument that might be useful in situations where you might be inclined to use a generator. For example, in the portolio example, you might consider this alternative:
'''
portfolio = [
    {'name': 'GooG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65},
]
# Original: Return 20
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)

#Alternative: Returns {'name': 'AOL', 'shares': 20}

min_shares = min(
    portfolio, key=lambda s: s['shares']
)

print(
    min_shares
)
'''
20
{'name': 'AOL', 'shares': 20}
'''
