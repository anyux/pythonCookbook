#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/12/11


'''
question:
有一系列字典或实例对象,我们想根据某个特定的字段(比如日期)来分组迭代数据.
'''
'''
解决方案:
itertools.groupby()函数对数据进行分组时特别有用.为了说明其用途.假设有如下字典列表:
'''
rows = [
    {'address':'5412 N CLARK','date': '07/01/2012'},
    {'address':'5148 N CLARK','date': '07/04/2012'},
    {'address':'5800 E 58TH','date': '07/02/2012'},
    {'address':'2122 N CLARK','date': '07/03/2012'},
    {'address':'5645 N RAVENSWOOD','date': '07/02/2012'},
    {'address':'1060 W ADDISON','date': '07/022012'},
    {'address':'4801 N BROADWAY','date': '07/01/2012'},
    {'address':'1039 W GRANVILLE','date': '07/04/2012'},
]

'''
现在假设想根据日期以分组的方式迭代数据.要做到这些,首先以目标字段(在这个例子中是date)来对序列排序,然后再使用itertools.groupby().
'''
from operator import itemgetter
from itertools import groupby

# Sort by the desired field first

print(
    rows.sort(
        key=itemgetter('date')
    )
)

# Iterate in groups
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ', i)


'''
这会产生如下输出:
'''
'''
07/01/2012
  {'address': '5412 N CLARK', 'date': '07/01/2012'}
  {'address': '4801 N BROADWAY', 'date': '07/01/2012'}
07/02/2012
  {'address': '5800 E 58TH', 'date': '07/02/2012'}
  {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'}
07/022012
  {'address': '1060 W ADDISON', 'date': '07/022012'}
07/03/2012
  {'address': '2122 N CLARK', 'date': '07/03/2012'}
07/04/2012
  {'address': '5148 N CLARK', 'date': '07/04/2012'}
  {'address': '1039 W GRANVILLE', 'date': '07/04/2012'}
'''

'''
讨论:
函数groupby()通过扫描序列找出拥有相同值(或是由参数key指定的函数所返回的值)的序列项.并将它们分组.groupby()创建了一个迭代器,而在每次迭代时都会返回一个值(value)和一个子迭代器(sub_iterator),这个子迭代器可以产生所有在该分组内具有该值的项.
在这里重要的是根据感兴趣的字段进行排序.因为groupby()只能检查边续的项,不首先排序的话,将无法按所想的方式来对记录分组.
如果只是简单地数据日期分组到一起,放进一个大的数据结构中以允许进随机访问,那么利用defaultdict()构建一个一键多值字典(multidict,见1.6节)可能会更好.例如:
'''
from collections import defaultdict

rows_by_date = defaultdict(list)

for row in rows:
        rows_by_date[
            row['date']
        ].append(row)
'''
这使得我们可以方便地访问每个日期的记录.如下所示:
'''

for i in rows_by_date['07/01/2012']:
    print(i)

'''
{'address': '5412 N CLARK', 'date': '07/01/2012'}
{'address': '4801 N BROADWAY', 'date': '07/01/2012'}
'''

'''
对于后面这个例子,我们并不需要先对记录做排序.因此,如果不考虑内存方面的因素,这种方式会比先排序再用groupby()迭代要来的更快
'''
