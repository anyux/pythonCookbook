#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/11/28

'''
question:
我们想要一个能将键(key)映射到多个值的字典(即所谓的一键多值字典[multidict])
'''

'''
解决方案:
字典是一种关联容器,每个键都映射到一个单独的值上.如果想让键映射到多个值,需要将这么多个值保存到另一个容器如列表或集合中.例如,可能会像这样的字典:
'''
d = {
    'a' : [1, 2, 3],
    'b' : [4, 5],
}

e = {
    'a' : {1, 2, 3},
    'b' : {4, 5}
}

'''
要使用列表还是集合完全取决于应用的意图.如果希望保留元素插入的顺序,就用列表.如果希望消除重复元素(且不在意它们的顺序),就用集合.
为了能方便地创建这些字典,可以利用collections模块中的defaultdict类.defaultdict的一个特点就是会自动初始化第一个值,
这样只需关注添加元素即可.例如:
'''
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)
'''
defaultdict(<class 'list'>, {'a': [1, 2], 'b': [4]})
'''
d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)

print(d)
'''
defaultdict(<class 'set'>, {'a': {1, 2}, 'b': {4}})
'''

'''
关于defaultdict,需要注意的一个地方是,它会自动创建字典表项以待稍后的访问(即使用这些表项当前在字典中还没有找到).如果不想要这个功能,
可以在普通字典上调用sedefault()方法来取代.例如:
'''
d = {} #A regular dictionary

d.setdefault('a',[]).append(1)
d.setdefault('a',[]).append(2)
d.setdefault('b',[]).append(4)

print(d)
'''
{'a': [1, 2], 'b': [4]}
'''
'''
然而,许多程序员觉得使用setdefault()有点不自然-----更别提每次调用它时都会创建一个初始值的实例了(例子中的空列表[])
'''

'''
讨论:
原则上,构建一个一键多值字典是很容易的.但是如果试着自己对第一个值做初始化操作,这就会变得很杂乱.例如,可能会写这样的代码:
'''
d = {}
pairs = {
    "1" : 'a',
    "2" : 'b',
    "3" : 'c',
}
for key, value in pairs.items():
    if key not in d:
        d[key] = []
    d[key].append(value)

print(d)

'''
{'1': ['a'], '2': ['b'], '3': ['c']}
'''

'''
使用default后代码会清晰得多:
'''
d = defaultdict(list)

for key, value in pairs.items():
    d[key].append(value)

print(d)
'''
defaultdict(<class 'list'>, {'1': ['a'], '2': ['b'], '3': ['c']})
'''

'''
这一节的内容同数据处理中的记录归组问题有很强的关联.请参见1.15节的示例.
'''




'''
'''