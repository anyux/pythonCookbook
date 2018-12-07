#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/12/7

'''
question:
我们想在同一个实例之间做排序,但是它们并不原生支持比较操作.
'''
'''
解决方案:
内建的sorted()函数可接受一个接受一佧用来传递可调用对象(callable)的参数,而该可调用对象会回待排序对象中的某些值,sorted则利用这些值来比较对象.例如,如果应用中有一系列的User对象实例,而我们想通过user_id,属性来对它们排序,则可以提供一个可调用对象将User实例作为输入然后返回user_id.示例如下:
'''
class User:
    def __init__(self,user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})' .format(self.user_id)

users = [
    User(23),
    User(3),
    User(99),
]

print(users)
'''
[User(23), User(3), User(99)]
[User(23), User(3), User(99)]
'''

print(sorted(users,key=lambda u: u.user_id))
'''
[User(3), User(23), User(99)]
'''
'''
除了可以用lambda表达式外,另一种方式是使用operator.attrgetter().
'''
from operator import attrgetter


print(sorted(users,key=attrgetter('user_id')))

'''
[User(3), User(23), User(99)]
'''

'''
讨论:
要使用lambda表达式还是attrgetter()或许只是一种个人喜好.但是通常来说,attrgetter()要更快一些,而且具有允许同时提取多个字段值的能力.这和针对字典的operator.itemgetter()的使用很类似(参见1.13).例如,如果User实例还有一个first_name和last_name属性的话,可以执行如下的排序操作:
'''

# by_name = sorted(users, key= attrgetter('last_name','first_name'))

'''

'''

'''
同样值得一提的是,本节所用到的技术也适用于像min()和max()这样的函数.例如:
'''
print(
    min(users,key=attrgetter('user_id'))
)

print(

    max(users,key=attrgetter('user_id'))
)

'''
User(3)
User(99)
'''




