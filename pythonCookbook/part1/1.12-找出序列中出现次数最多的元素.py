#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/12/5

'''
我们有一个元素序列,想知道在序列中出现次数最多的元素是什么.
'''

'''
解决方案:
collections模块中的Counter类正是为此类问题所设计的.它甚至有一个非常方便的most_common()方法可以直接告诉我们答案.
为了说明用法,假设有一个列表,列表中是一系列的单词,我们想找出哪些单词的出现的最为频繁.下面是我们的做法:
'''

words =[
    'look','into','my','eyes', 'look','my','eyes','the','eyes','the','the',
    'eyes','not','arround','the','eyes',"don't",'look','arround','the',
    'eyes','look','into','my','eyes',"you're",'under',
]


from collections import Counter

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)

'''
[('eyes', 7), ('the', 5), ('look', 4)]
'''

'''
讨论:
可以给Counter对象提供可哈希的对象序列作为输入.在底层实现中,Counter是一个字典,在元素和它们出现的次数间做了映射.例如:
'''
print(word_counts['not'])
print(word_counts['eyes'])

'''
1
7
'''

'''
如果想手动增加计数,只需要简单地自增即可:
'''

morewords = [
    'why','are','you','not','looking','in','my','eyes'
]

for word in morewords:
    word_counts[word] += 1

print(word_counts['eyes'])

'''
8
'''

'''
另一种方法是update()方法
'''
word_counts.update(morewords)
print(word_counts['eyes'])
'''
9
'''
'''
关于COunter对象有一个不为人知的特性,那就是它们可以轻松同各种数学运算操作结合起来使用.例如:
'''

a = Counter(words)

b = Counter(morewords)

print(a)

print(b)

'''
Counter({'eyes': 7, 'the': 5, 'look': 4, 'my': 3, 'into': 2, 'arround': 2, 'not': 1, "don't": 1, "you're": 1, 'under': 1})
Counter({'why': 1, 'are': 1, 'you': 1, 'not': 1, 'looking': 1, 'in': 1, 'my': 1, 'eyes': 1})
'''

c = a+b
print(c)
'''
Counter({'eyes': 8, 'the': 5, 'look': 4, 'my': 4, 'into': 2, 'not': 2, 'arround': 2, "don't": 1, "you're": 1, 'under': 1, 'why': 1, 'are': 1, 'you': 1, 'looking': 1, 'in': 1})
'''

d = a- b
print(d)

'''
Counter({'eyes': 6, 'the': 5, 'look': 4, 'into': 2, 'my': 2, 'arround': 2, "don't": 1, "you're": 1, 'under': 1})
'''

'''
不用说,当面对任何需要对数据制表或计数的问题时,Counter对象都是你手边的得力工具.比起利用字典自己手写算法,更应该采用这种方式完成任务
'''



















'''
'''
