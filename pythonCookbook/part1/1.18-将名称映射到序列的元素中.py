#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/12/17

'''
question:
我们的代码是通过位置(即索引,或下标)来访问列表或元组的,但有时候这会使用代码变得难以阅读.希望可以通过名称来访问元素,以此减少结构中对位置的依赖性.
'''
'''
解决方案:
相比普通的元组,collections.namedtuple()(命名元组)只增加了极小的开销就提供了这些便利.实际上collections.namedtuple()是一个工厂方法,它返回的是Python中标准元组类型的子类.我们提供给它一个类型名称以及相应的字段,它就返回一个可实例化的类,为你已经定义好的字段传入值等.例如:
'''
from collections import namedtuple
Subscriber = namedtuple(
    'Subscrible', ['addr', 'joined']
)

sub = Subscriber(
    'jonesy@example.com', '2012-10-19'
)
print(sub)
print(sub.addr)
print(sub.joined)
'''
Subscrible(addr='jonesy@example.com', joined='2012-10-19')
jonesy@example.com
2012-10-19
'''

'''
尽管namedtuple的实例看起来就像一个普通的类实例,但它的实例与普通的元组是可以相互转换的.而且支持普通元组所支持的操作,例如索引(index)和分解(upacking).比如:
'''
print(
    len(sub)
)
addr,joined = sub

print(addr)
print(joined)
'''
2
jonesy@example.com
2012-10-19
'''

'''
命名元组的主要作用在于将代码同它所控制的元素位置间解锁.所以,如果从数据库调用中得到一个大型的元组列表,而且通过元素的位置来访问数据,那么假如在表单中新增一列数据,那么代码就会崩溃.但如果首先将返回的元组转型为命名元组,就不会出现问题.
为了说明这个问题,下面有一些使用普通元组的代码:
'''

def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total

'''
通过位置来引用元素常常使得代码的表达力不够强,而且也很依赖于记录的具体结构.
下面是使用命名元组的版本:
'''
from collections import namedtuple

Stock = namedtuple(
    'Stock', ['name', 'shares', 'price']
)
def compute_cost(records):
    totals = 0.0
    for rec in records:
        s = Stock(*rec)
        totals += s.shares * s.price
    return totals
'''
当然,如果示例中的records序列已经包含了这样的实例,那么可以避免显式地将记录转换为Stock命名元组.
'''
'''
讨论:
namedtuple是一种可能用法是作为字典的替代,后者需要更多的空间来存储.因此,如果要构建涉及字典的大型数据结构,使用namedtuple()会更加高效.但是与字典不同的是,namedtuple是不可变的(immutable).例如:
'''
s = Stock(
    'ACME', 100, 123.45
)

print(s)

# s.shares = 75
'''
报错如下:
Traceback (most recent call last):
  File "C:/pythoncookbook/pythonCookbook/pythonCookbook/part1/1.18-将名称映射到序列的元素中.py", line 86, in <module>
    s.shares = 75
AttributeError: can't set attribute
'''

'''
如果需要修改任何属性,可以通过使用namedtuple实例的_replace()方法来实现.
该方法会创建一个全新的命名元组,并对相应的值做替换.示例如下:
'''
s = s._replace(shares=75)
print(s)
'''
Stock(name='ACME', shares=75, price=123.45)
'''

'''
_replace()方法有一个微妙的用途,那就是它可以作为一种简便的方法填充具有可选或缺失字段的命名元组.要做到这点,首先创建一个包含默认值的"原型"元组,然后使用_replace()方法创建一个新的实例,把相应的值替换掉.示例如下:
'''

from collections import namedtuple

Stock = namedtuple(
    'Stock', ['name', 'shares', 'price', 'date', 'time']
)

#Create a prototype instance

stock_prototype = Stock('', 0, 0.0, None, None)

#Function to convert a dictionary to a Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)

'''
让我们演示一下上面的代码是如何工作的:
'''
a = {
    'name'      : 'ACME',
    'shares'    : 100,
    'price'     : 123.45,
}
print(
    dict_to_stock(a)
)

b = {
    'name'      : 'ACME',
    'shares'    : 100,
    'price'     : 123.45,
    'date'      : '12/17/2012',
}

print(
    dict_to_stock(b)
)

'''
Stock(name='ACME', shares=100, price=123.45, date=None, time=None)
Stock(name='ACME', shares=100, price=123.45, date='12/17/2012', time=None)
'''

'''
最后,也是相当重要的是,应该注意我们的目标是定义一个高效的数据结构,而且将来会修改各种实例属性,那么使用namedtuple并不是最佳选择.相反,可以考虑定义一个使用__slots__属性的类(参见8.4节)
'''
