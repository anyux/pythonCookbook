#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/11/27

'''
question:
我们想实现一个队列,它能够以给定的优先级来对元素排序,且每次pop操作都会返回优先级最高的那个元素.
'''

'''
解决方案:
下面的类利用heapq模块实现一个简单的优先级队列:
'''
import heapq

class PriorityQueue:

    '''

    '''
    def __init__(self):
        self._queue = []
        self._index = 0


    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority,self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

'''
下面是如何使用这个类的例子:
'''
class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()

q.push(Item('foo'),1)
q.push(Item('bar'),5)
q.push(Item('spam'),4)
q.push(Item('grok'),1)

print(q.pop())
'''
Item('bar')
'''
print(q.pop())
'''
Item('spam')
'''
print(q.pop())
'''
Item('foo')
'''
print(q.pop())
'''
Item('grok')
'''
'''
请主意观察,第一次执行pop()操作时返回的元素具有最高的优先级.我们也观察到拥有相同优先级的两个元素(
foo和grok)返回的顺序同它们插入到队列时的顺序相同.
'''

'''
讨论:
上面的代码片段的核心在于heapq模块的使用.函数heapq.heappush()以及heapq.heappop(
)分别实现将元素从列表_queue中插入和移除,且保证列表中第一个元素的优先级最低(如1.4所述).heapqpop()方法总是返回"最小"的元素,
因此这就是让队列能弹出正确元素的关键.此外,由于push和pop操作复杂度都是O(logN),其中N代表堆中元素的数量,因此就算N的值很大,
这些操作的效率也非常高.
在这段代码中,队列以元组(-priority,index,
item)的形式组成.把priority取负值是为了让队列能够按元素的优先级从高到低的顺序排列.这和正常的堆排序相反,一般情况下堆是按从小到大的顺序排序的.
变量index的作用是为了将具有相同优先级的元素以适当的顺序排列.通过维护一个不断递增的索引,元素将以它们入队列时的顺序来排列.但是,
index在对具有相同优先级的元素间做比较操作时同样扮演了重要的角色.
为了说明Item实例是没法进行次序比较的,我们来看下面这个例子:
'''
a = Item('foo')

b = Item('bar')

# a < b

'''
File "E:/pythonCookbook/pythonCookbook/part1/1.5-实现优先级队列.py", line 88, in <module>
    a < b 
TypeError: '<' not supported between instances of 'Item' and 'Item'
'''
'''
如果以元组(priority,item)的形式来表示元素,那么只要优先级不同,它们就可以进行比较.但是,如果两个元组的优先级值相同,
做比较操作时还是会像之前那样失败.例如:
'''
a = (1,Item('foo'))

b = (5,Item('bar'))

print(a < b)
'''
True
'''

c = (1,Item('grok'))

# a < c
'''
e "E:/pythonCookbook/pythonCookbook/part1/1.5-实现优先级队列.py", line 110, in <module>
a < c
TypeError: '<' not supported between instances of 'Item' and 'Item'
'''
'''
通过引入额外的索引值,以(priority,index,item)的方式建立元组,就可以完全避免这个问题.因为没有哪两个无组会有相同的index值(
一旦比较操作的结果可以确定,Python就不会再云比较剩下的元组元素了):
'''
a = (1,0,Item('foo'))
b = (5,1,Item('bar'))
c = (1,2,Item('grok'))
print(a<b)

print(a<c)
'''
True
True
'''
'''
如果想将这个队列用于线程间通信,还需要增加适当的锁和信号机制.请参见12.3节的示例学习如何去做.
关于堆的理论和现实在heapq模块的文档中有着详细的示例和相关讨论.
'''
















'''

'''