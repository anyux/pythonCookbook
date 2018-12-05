#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/11/24

'''
question:
我们希望在迭代或是其他形式的处理过程中对最后几项记录做一个有限的历史记录统计.
'''

'''
解决方案:
保存有限的历史记录可算是collections.deque的完美应用场景了.例如,下面的代码对一系列文本做简单的匹配操作,
当发现有匹配时就输出当前匹配行以及最后检查过的N行文本.
'''
from collections import deque

def search(lines,pattern,history=5):
    # A list-like sequence optimized for data accesses near its endpoints.
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line,previous_lines
        previous_lines.append(line)

#Example use on a file

if __name__ == "__main__":
    with open('README.txt',mode='r',encoding='utf-8') as f:
        for line, prevlines in search(f,'Python',5):
            for pline in prevlines:
                print(pline,end='')
            print(line,end='')
            print('-'*20)

'''
运行结果如下:

数据结构和算法
Python内置了许多非常有用的数据结构,比如列表(list),集合(set),以及字典(directory).
--------------------

'''

'''
讨论:
如同上面的代码所做的那样,当编写搜索某项记录的代码时,
通常会含有yield关键字的生成器函数.这将处理搜索过程的代码和使用搜索结果的代码成功解耦开来.如果请生成器不熟悉,参见4.3.
deque(maxlen=N)创建一个固定长度的队列.当有新记录加入而队列已满时会自动移除最老的那条记录.例如:
'''
q = deque(maxlen=3)

for i in range(5):
    q.append(i)
    print(q)

'''
运行结果如下:

deque([0], maxlen=3)
deque([0, 1], maxlen=3)
deque([0, 1, 2], maxlen=3)
deque([1, 2, 3], maxlen=3)
deque([2, 3, 4], maxlen=3)
'''

'''
尽管可以在列表上手动完成这样的操作(append,del),w但队列这种解决方案要优雅得多,运行速度也快得多.
更普遍的是,当需要一个简单的队列结构时,deque可祝你一臂之力.如果不指定队列的大小,也就得到了一个无界限的队列,可以在两端执行添加和弹出操作,例如:
'''
q = deque()

for i in range(5):
    q.append(i)

print(q)

'''
deque([0, 1, 2, 3, 4])
'''
q.appendleft(5)
print(q)
'''
deque([5, 0, 1, 2, 3, 4])
'''
q.pop()

print(q)
'''
deque([5, 0, 1, 2, 3])
'''
q.popleft()

print(q)
'''
deque([0, 1, 2, 3])
'''


'''
从队列两端添加或弹出元素的复杂度都是O(1).这和队列不同,当从列表的头部插入或移除元素时,列表的复杂度为O(N)
'''
