#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/12/5

'''
question:
我们想去除序列中出现的重复元素,但仍然保持元素顺序不变.
'''

'''
解决方案:
如果序列中的值是可哈希的(hashable),那么这个问题可以通过使用集合和生成器轻松解决.示例如下:
注:如果一个对象是可哈希的,那么在它的生存期内必须是不可变的,它需要一个__hash__()方法.整数,浮点,字符串,元组都是不可变的,它们都是可哈希的.
'''
def dedup(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
'''
这里是如何使用这个函数的例子:
'''
a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedup(a)))
'''
[1, 5, 2, 9, 10]
'''
'''
只有当序列中的元素是可哈希的才能这么做.如果想在不可哈希的对象(比如列表)序列中去除重复项,需要对上述代码稍作修改:
'''
def dedupe_list(items,key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

'''
这里参数key的作用是指定一个函数用来将序列中的元素转换为可哈希的类型,这么做的目的是为了检测重复项.它可以像这样工作:
'''
a = [
    {'x' : 1, 'y' : 2},
    {'x' : 1, 'y' : 3},
    {'x' : 1, 'y' : 2},
    {'x' : 2, 'y' : 4},
]

print(list(dedupe_list(a, key=lambda d: (d['x'], d['y']))))
'''
[{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]
'''

print(list(dedupe_list(a, key=lambda d: d['x'])))
'''
[{'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
'''

'''
讨论:
如果想要做的只是去除重复项,那么通常足够简单的办法就是构建一个集合.例如:
'''
a = [1, 5, 2, 1, 9, 1, 5, 10]

print(set(a))

'''
{1, 2, 5, 9, 10}
'''

'''
但是这种方法不能保证元素间的顺序不变,因此得到的结果会被打乱.前面展示的解决方案可避免出现这个问题.
本节中对生成器的使用反映出一个事实,那就是我们可能会希望这个函数尽可能的通用---不必绑定在只能对列表进行处理.比如,如果想读一个文件,
去除其中重复的文本行,可以只需要这样处理:
'''
with open('xxx.txt','r') as f:
    for line in dedup(f):
        pass

'''
我们的dedupe()函数也模仿了内置函数sorted(),min()以及max()对key函数的使用方式.例子可参考1.8,和1.13.
'''



'''

'''
