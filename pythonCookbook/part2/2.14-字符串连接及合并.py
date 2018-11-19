#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/11/19

'''
question:
我们想将许多小字符串合并成一个大的字符串.
'''
'''
解决方案:
如果相要合并的一个字符串在一个序列或可迭代对象中,那么将它们合并起来的最快方法是join().示例如下:
'''
parts = ['Is', 'Chicago', 'Not', 'Chicago?']

print(' '.join(parts))

print(','.join(parts))

print(''.join(parts))

'''
运行结果如下:

Is Chicago Not Chicago?
Is,Chicago,Not,Chicago?
IsChicagoNotChicago?

'''
'''
初看上去语法可能有些怪异,但是join(
)操作其实是字符串对象的一个方法.这么设计的部分原因是因为想要合并在一起的对象可能来自各种不同的数据序列.比如列表,元组,字典,文件,集合或生成器,
如果单独在每一种序列对象中实现一个join()方法显得太冗余了.因此只需要指定想要分隔字符串,然后在字符串对象上使用join(
)方法将文本片段粘合在一起就可以了.
如果只是想连接一些字符串,一般使用+操作符就足够完成任务了.
'''
a = 'Is Chicago'

b = 'Not Chicago?'

print(a + ' ' + b)

'''
Is Chicago Not Chicago?
'''
'''
针对更加复杂的字符串格式化操作,+操作符同样可以作为format()的替代,很好地完成任务:
'''
print('{} {}'.format(a,b))

print(a+ ' ' + b)

'''
运行结果如下:

Is Chicago Not Chicago?
Is Chicago Not Chicago?

'''
'''
如果打算在源代码中将字符串字面值合并在一起,可以简单地将它们排列在一起,中间不加+操作符.示例如下:
'''
a = 'hello' 'world'

print(a)

'''
helloworld
'''
'''
讨论:
字符串连接这个主题可能看起来还没有高级到要用一整节的篇幅来讲解,但是程序员常常会在这个问题上做出错误的编程选择,使用得他们的代码性能受到影响.
最重要的一点是要意识到+操作符做大量的连接是非常低效的,原因是由于内存拷贝和垃圾收集产生的影响.特别是你绝不会想写出这样的字符串连接代码:
'''
s = ''
for p in parts:
    s +=p

print(s)

'''
IsChicagoNotChicago?
'''
'''
这种做法比使用join()方法要慢上许多.主要是因为每个+=操作都会创建一个新的字符串对象.我们最好先收集所有要连接的部分,最再一次将它们连接起来.
一个相关技巧(很漂亮的技巧)是利用生成器表达式(见1.19)在将数据转换为字符串的同时完成连接操作.示例如下:
'''
data = ['ACME',50,91.1]
print(','.join(str(d) for d in data))
'''
ACME,50,91.1
'''
'''
对于不必要的字符串连接操作也要引起重视.有时候在技术上并非必需的时候,程序员们也会忘乎所以地使用字符串连接操作.例如在打印的时候:
'''
c = '@'
print(a + ':' + b + ':'+ c) # ugly

print(':'.join([a,b,c])) #  Still ugly

print(a,b,c,sep=':') #better

'''
运行结果如下:

helloworld:Not Chicago?:@
helloworld:Not Chicago?:@
helloworld:Not Chicago?:@

'''
'''
将字符串连接同I/O操作混合起来的时候需要对就用做仔细的分析.例如,考虑如下两段代码:
'''
import sys
def version1():
    # Version 1 (string concatenation)
    f_old = open(sys.argv[0], 'r', 'utf-8')
    f = open(sys.argv[0].join('.bak'), 'w', 'utf-8')
    chunk1 = f.read()
    chunk2 = f.read()
    f.write(chunk1 + chunk2)

def version2():
    #Version 2 (separate I/O operations)
    f_old = open(sys.argv[0], 'r', 'utf-8')
    f = open(sys.argv[0].join('.bak'), 'w', 'utf-8')
    chunk1 = f.read()
    chunk2 = f.read()

    f.write(chunk1)
    f.write(chunk2)

'''
如果这两个字符串都很小,那么每一个版本的代码能带来更好的性能,这是因为执行一次I/O系统调用的固有开销就很高.另一方面,如果这两个字符串都很大,
那么第二个版本的代码会更加高效.因为这里避免了创建大的临时结果,也没有对大块的内存进行拷贝.这里必须再次强调,你需要对自己的数据做分析,
以此才能判定哪一种方法可以获得最好的性能.
最后但也是最重要的是,如果我们编写的代码要从许多短字符串中构建输出,则应该考虑编写生成器函数,通过yield关键字生成字符串片段.示例如下:
'''
def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'

'''
关于这种方法有一个有趣的事实,那就是它不会假设产生的片段要如何组合在一起.比如说可以用join()将它们简单地连接起来:
'''
text = ''.join(sample())
print(text)

'''
IsChicagoNotChicago?
'''
'''
或者,也可以将这些片段重定向到I/O:
'''
def write_IO():
    f = open(sys.argv[0].join('.bak'), 'r', 'utf-8')
    for part in sample():
        f.write(part)

'''
又或者我们能以混合的方式将I/O操作智能化地结合在一起:
提示:因为yield是一次性的,所以这里重新定义一个函数
'''
def sample2():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'

def combine(source,maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if int(size) > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
    yield ''.join(parts)

for part in combine(sample2(),32768):
    print(part)
'''
运行结果如下:

IsChicagoNotChicago?

'''

'''
关键在于这里的生成器函数并不需要知道精确的细节,它只是产生片段而已.
'''
