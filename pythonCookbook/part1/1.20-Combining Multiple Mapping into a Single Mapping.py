#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/12/18

'''
Problem:
You have multiple dictionaries or mappings that you want to logically combine into a single mapping to perform certain operations, such as looking up values or checking for the existence of keys.
'''

'''
Solution:
Suppose you have two dictionaries:
'''
a = {
    'x':1,'z':3,
}
b = {
    'y':2,'z':4,
}
'''
Now suppose you want to perform lookups where you have to check both dictionaries (e.g., first checking in a and the in b if not found).An easy way to do this is to use the ChainMap class from the collections module. For exmaple:
'''
from collections import ChainMap

c = ChainMap(a,b)

print(c['x'])
print(c['y'])
print(c['z'])
'''
1
2
3
'''

'''
Discussion:
A chainMap takes multiple mapping and makes them logically appear as one. However, the mappings are not literally merged together. Instead, a ChainMap simply keeps a list of the underlying mappings and redefines common dictionary operations to scan the list. Most operations will work. For example:
'''


print(
    len(c)
)

print(
    list(
        c.keys()
    )
)

print(
    list(
        c.values()
    )
)
'''
3
['x', 'z', 'y']
[1, 3, 2]
'''
'''
If there are duplicate keys, the avlues form the first mapping get used. Thus, the entry c['z'] in the example would  always refer to the value in dictionary a , not the value in dictionary b.

Operations that mutate the mapping always affect the firest mapping listed.For example:
'''

c['z'] = 10
c['w'] = 40

del c['x']

print(
    a
)
'''
{'z': 10, 'w': 40}
'''
# del c['y']
'''
Traceback (most recent call last):
...
KeyError: "key not found in the first mapping: 'y'"
'''

'''
A ChainMap is particularly useful when working with scoped values such as variables in a programming language (i.e., globals,locals,etc.).In fact, there are methods that make this easy:
'''
values = ChainMap()

values['x'] = 1

# Add a new mapping
vlaues = values.new_child()
values['x'] = 2

#Add a new mapping
values = values.new_child()
values['x'] = 3

print(values)

'''
ChainMap({'x': 3}, {'x': 2})
'''

# Discard last mapping
values = values.parents
print(
    values['x']
)
'''
2
'''

'''
As an alternative to ChainMap, you might consider merging dictionaries together using the update() method. For example:
'''
a = {
    'x':1,'z':3
}
b = {
    'y':2, 'z':4
}

merged = dict(b)
merged.update(a)
print(merged)
'''
{'y': 2, 'z': 3, 'x': 1}
'''

'''
This works , but it requires you to make a completely separate dictionary object (or destructively alter one of the existing dictionaries). Also,if any of the original dictionaries mutate, the chages don't get reflected in the merged dictionary. For example:
'''
a['x'] = 13
print(merged['x'])
'''
1
'''

'''
A ChainMap uses the original dictionaries, so it doesn't have this behavior. For example:
'''
a = {
    'x':1,'z':3
}

b = {
    'y':2,'z':4
}

merged = ChainMap(a,b)

print(
    merged['x']
)
'''
1
'''
a['x'] =42

print(merged['x']) #Notice change to merged dicts
'''
42
'''


