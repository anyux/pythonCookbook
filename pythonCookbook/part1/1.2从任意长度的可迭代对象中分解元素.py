#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/11/23

'''
question:
需要从某个可迭代对象中分解出N个元素,但是这个可迭代对象的长度可能起过N,这会导致出现"分解的值过多(too many values to
unpack)"的异常
'''
'''
解决方案:
Python的"*表达式"可以用来解决这个问题.例如,假设开设了一门课程,并决定在期末的作业成绩中去掉成绩中第一个和最后一个,
只对中间剩下的成绩做平均分统计.如果只有4个成绩,也许可以简单地将4个都分解出来,但是如果有24个呢?*表达式使这一切都变得简单:
'''
def avg(my_list):

    my_num = len(my_list)
    my_sum = sum(my_list)
    return int(my_sum/my_num)

def drop_first_last(grades):

    first,*middle,last = grades
    return avg(middle)

my_grades = [100,95,97,93,99,100,100]

print(drop_first_last(my_grades))
'''
96
'''
'''
另一个用例是假设有一些用户记录,记录由姓名和电子邮件地址组成,后面跟着任意数量的电话号码.则可以像这样分解记录:
'''
record = ('Dave','dave@example.com','773-555-1212','847-555-1212')
name,email,*iphone_numbers =record
print(name,email,iphone_numbers)
'''
Dave dave@example.com ['773-555-1212', '847-555-1212']
'''

'''
不管需要分解出多少个电话号码(甚至没有电话号码),变量,iphone_numbers都一直是列表,而这是这毫无意义的.如此一来,
对于任何用到了变量phone_numbers的代码都是不必对它可能不是一列表的情况负责,或者额外做任何形式的类型检查.
由于*修饰的变量也可以位于列表的第一个位置.例如,比方说用一系列的值来代表公司过去8个季度的销售额.如果想对最近一个季度的销售额的平均值做比较可以这么做:
'''
def avg_conparision(num1,num2,str1,str2):
    if num1 > num2:
        return (str1,str2)
    elif num2 > num1:
        return (str2,str1)
    else:
        return None

sales_record = [100,80,95,87,93,99,88,99]
*trailing_qtrs,current_qtr = sales_record
trailing_avg = avg(trailing_qtrs)
str1 = "前7个季度的销售额"
str2 = "近一个季度的销售额"
res = avg_conparision(trailing_avg,current_qtr,str1,str2)

if res:
    print('{} 大于 {}'.format(*res))
else:
    print("值相同")

'''
运行结果如下:

近一个季度的销售额 大于 前7个季度的销售额

'''

'''
讨论:
对于分解未知或任意长度的可迭代对象,这种扩展的分解操作可谓是量身定做的工具.通常,这类可迭代对象中会有一些已知的组件或模式(例如,
元素1之后的所有内容都是电话号码),利用*表达式分解可迭代对象使得开发者能够轻松利用这些模式,而不必在可迭代对象中做复杂花哨的操作才能得到的相关的元素.
*式的语法在迭代一个变长的元组序列时尤其有用.例如,假设有一个带标记的元组序列:
'''
records = [
    ('foo',1,2),
    ('bar','hello'),
    ('foo',3,4),
]
def do_foo(x,y):
    print('foo',x,y)

def do_bar(s):
    print('bar',s)

for tag,*args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

'''
运行结果如下:

foo 1 2
bar hello
foo 3 4
'''

'''
当和某些特定的字符串处理操作结合,比如拆分(splitting)操作时,这种*式的语法所支持的分解操作也非常有用.例如:
'''
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname,*fields,homedir,sh = line.split(":")
print(uname)

print(*fields)

print(homedir)

print(sh)
'''
nobody
* -2 -2 Unprivileged User
/var/empty
/usr/bin/false
'''
'''
有时候可能分解出某些值然后会丢弃它们.在分解的时候,不能只是指定一个单独的*,但是可以使用几个常用来表示待丢弃值的变量名,比如_或者ign(
ignored).例如:
'''

record = ('ACME', 50, 123.45, (12, 18, 2013))
name,*_, (*_,year) = record

print(name)
print(year)

'''
ACME
2013
'''
'''
*分解操作和各种函数式语言中的列表处理功能有着一定的相似性.例如,如果有一个列表,可以像下面这样轻松将其分解为头部和尾部:
'''
items = [1, 10, 7, 4, 5, 9]
head, *tail = items

print(head)
print(tail)
'''
运行结果如下:

1
[10, 7, 4, 5, 9]

'''

'''
在编写执行这类拆分函数时,人们可以假设这是为了实现某种精巧的递归算法.例如:
'''
items = [1, 10, 7, 4, 5, 9]
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

print(sum(items))

'''
36
'''

'''
但是请注意,递归真的不算是Python的强项,这是因为其内在的递归限制所致.因此,最后一例子在实践中没有太大的意义,只不过是一点学术上的好友罢了.
'''




'''



'''
