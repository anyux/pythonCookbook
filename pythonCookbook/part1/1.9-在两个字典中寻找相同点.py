#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/12/3

'''
question:
有两个字典,我们想找出它们中间可能相同的地方(相同的键,相同的值等).
'''
'''
解决方案:
考虑如下两个字典:
'''
a = {
    'x' : 1,
    'y' : 2,
    'z' : 3,
}

b = {
    'w' : 10,
    'x' : 11,
    'y' : 2,
}

'''
要找出这两个字典中的相同之处,只需要通过keys()或者items()方法执行常见的集合操作即可.例如:
'''
# Find keys in common

print(a.keys() & b.keys())

'''
{'x', 'y'}
'''
#Find keys in a that are not in b

print(a.keys() - b.keys())

'''
{'z'}
'''

#Find (key,value) pairs in common

print(a.items() & b.items())

'''
{('y', 2)}
'''

'''
这些类型的操作也可用来修改或过滤掉字典中的内容.例如,假设想创建一个新的字典,其中会去掉某些键.下面是使用了字典推导式的代码示例:
'''

#Make a new dictionary with certain keys removed

c = {key:a[key] for key in a.keys() - {'z','w'}}

print(c)

'''
{'y': 2, 'x': 1}
'''

'''
讨论:
字典就是一系列键和值之间的映射集合.字典的keys()方法会返回keys-view对象,其中显露了所有的键.关于字典的键有一个很少有人知道的特性,
那就是它们也支持常见的集合操作,比如求并集,交集,差集.因此,如果需要对字典的键做常见的集合操作,
那么就能直接使用keys-view对象而不必先将它们转化为集合.
字典的items()方法返回由(key,value)对组成的items-key对象.这个对象支持类似的集合操作,
可用来完成找出两个字典间有哪些键值对有相同之处的操作.
尽管类似,但字典的values()方法并不支持集合操作.部分原因在字典的键值是不同的,
从值的角度来看并不能保证所有的值都是唯一的.单这一条原因就使得某些特定的集合操作是有问题的.但是,如果必须执行这些操作,还是可以先将值转化为集合来实现.
'''












'''

'''