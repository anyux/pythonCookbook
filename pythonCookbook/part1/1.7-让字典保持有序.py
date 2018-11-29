#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/11/29

'''
question:
我们想创建一个字典,同时对字典做迭代或序列化操作时,也能控制元素的顺序.
'''

'''
解决方案:
要控制字典中元素的顺序,可以使用collections模块中的OrderdDict类.当对字典做迭代时,它会严格按照元素初始加的顺序进行.例如:
'''
from collections import OrderedDict

d = OrderedDict()

d['foo'] = 1

d['bar'] = 2

d['spam'] = 3

d['grok'] = 4

#Output "foo 1" "bar 2" "spam 3" "grok 4"

for key in d:
    print(key,d[key])

'''
foo 1
bar 2
spam 3
grok 4
'''

'''
当想构建一个映射结构以便稍后对其做序列化或编码成另一种格式时,OrderedDict就显得特别有用.例如,如果想在进行JSON编码时精确控制各字段的顺序,
那么只需要首先在OrderedDict中构建数据结构就可以了.
'''

import json

print(json.dumps(d))
'''
{"foo": 1, "bar": 2, "spam": 3, "grok": 4}
'''

'''
讨论:
OrderedDict内部维护一个双向链表,
它会根据元素加入的顺序来排列键的位置.第一个新加入的元素被放置在链表的末尾.接下来对已存在的键做重新赋值不会改变键的顺序.
请注意OrderedDict的大小是普通字典的2倍多,这是由于它额外创建的链表所致.因此,如果打算构建一个涉及大量OrderedDict实例的数据结构(
例如从CSV文件中读取1000行内容到OrderedDict列表中),那么需要认真对应用做需求分析,
从而判断使用OrderedDict的好处是否能超越因额外的内存开销所带来的缺点.
'''