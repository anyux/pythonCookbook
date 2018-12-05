#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/11/26

'''
question:
我们想在某个集合中找出某个最大或最小的N个元素.
'''

'''
解决方案:
heapq模块中有两个函数----nlargest()和nsmallest()----它们正是我们所需要的.例如:
'''
import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3,nums))
print(heapq.nsmallest(3,nums))

'''
[42, 37, 23]
[-4, 1, 2]
'''

'''
这两个函数都可以接受一个参数key,从而允许它们工作在更加复杂的数据结构之上.例如:
'''

portfolio = [
    {'name':'IBM', 'shares':100, 'price':91.1},
    {'name':'AAPL', 'shares':50, 'price':543.22},
    {'name':'FB', 'shares':200, 'price':21.09},
    {'name':'HPQ', 'shares':35, 'price':31.75},
    {'name':'YHOO', 'shares':45, 'price':16.35},
    {'name':'ACME', 'shares':75, 'price':115.65},
]

cheap = heapq.nsmallest(3,portfolio,key=lambda s: s['price'])

expensive = heapq.nlargest(3,portfolio,key=lambda s: s['price'])

print(cheap)
print(expensive)

'''
[{'name': 'YHOO', 'shares': 45, 'price': 16.35}, {'name': 'FB', 'shares': 200, 'price': 21.09}, {'name': 'HPQ', 'shares': 35, 'price': 31.75}]
[{'name': 'AAPL', 'shares': 50, 'price': 543.22}, {'name': 'ACME', 'shares': 75, 'price': 115.65}, {'name': 'IBM', 'shares': 100, 'price': 91.1}]
'''

'''
讨论:
如果正在寻找最大或最小的元素,且同集合中元素的总数目相比,N很小,那么下面这些函数可以提供更好的性能.这些函数首先会在底层将数据转化成列表,
且元素会以堆的顺序排列.例如:
'''

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

heap = list(nums)
heapq.heapify(heap)
print(heap)
'''
[-4, 2, 1, 23, 7, 2, 18, 23, 42, 37, 8]
'''

'''
堆最重要的特性就是heap[0]总是会最小那个的元素.此外,接下来的元素可依次通过heapq.heappop()方法轻松找到.该方法会将第一个元素(
最小的)弹出,然后以第二小的元素取而代之(这个操作的复杂度O(logN),N代表堆的大小).例如,要找到第3小的元素,可以这样做:
'''
print(heapq.heappop(heap))
'''
-4
'''
print(heapq.heappop(heap))
'''
1
'''
print(heapq.heappop(heap))
'''
2
'''
'''
当所要找的元素数量相对较小时,函数nlargest()和nsmallest()才是最适用的.如果只是简单地想找到最小或最大的元素(N=1时),
那么用min()和max()会更加快.同样,如果N和集合本身的大小差不多大,通常更快的方法是先对集合排序,然后做切片操作(例如,使用sorted(
items)[:N]或者sorted(items)[-N:]).应该要注意的是,nlargest()和nsmallest(
)的实际实现会根据使用它们的方式而有所不同,可能会相应作出一些优化措施(比如,当N的大小同输入大小很接近时,就会采用排序的方法).
使用本节的代码片段并不需要知道如何实现堆数据结构,
但这仍然是一个有趣也是值得去学习的主题.通常在优秀的算法和数据结构的书籍里都能找到堆数据结构的实现方法.heapq模块的文档中也讨论底层实现的细节.
'''








'''

'''