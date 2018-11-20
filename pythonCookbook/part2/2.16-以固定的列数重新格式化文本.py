#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/11/20

'''
question:
我们有一些很长的字符串,想将它们重新格式化,使得它们能按照用户指定的列数来显示.
'''
'''
解决方案:
可以使用textwrap模块重新格式化文本的输出.例如,假设有如下这段长字符串:
'''
s = "Look into my eyes, look into my eyes, the eyes, the eyes, the eyes, " \
    "not around the eyes, don't look around the eyes, look into my eyes, " \
    "you're under"

'''
这里可以用textwrap模块以多种方式重新格式化字符串:
'''
import textwrap
print(textwrap.fill(s,70))
'''
运行结果如下:

Look into my eyes, look into my eyes, the eyes, the eyes, the eyes,
not around the eyes, don't look around the eyes, look into my eyes,
you're under
'''

print(textwrap.fill(s,40))
'''
运行结果如下:

Look into my eyes, look into my eyes,
the eyes, the eyes, the eyes, not around
the eyes, don't look around the eyes,
look into my eyes, you're under
'''
print(textwrap.fill(s,40,initial_indent=' '))
'''
运行结果如下:

 Look into my eyes, look into my eyes,
the eyes, the eyes, the eyes, not around
the eyes, don't look around the eyes,
look into my eyes, you're under
'''

print(textwrap.fill(s,40,subsequent_indent=' '))
'''
运行结果如下:

 the eyes, the eyes, the eyes, not
 around the eyes, don't look around the
 eyes, look into my eyes, you're under
'''

'''
讨论:
textwrap模块能够以简单直接的方式对文本格式做整理使用其适合于打印----尤其是当希望输出结果能很好地显示在终端上时.关于终端的尺寸大小,
可以通过os.get_terminal_size()来获取.例如:
注:此处需要通过 python xxx.py 这样来执行才能获取屏幕的尺寸大小
'''
import os
print(os.get_terminal_size().columns)
print(os.get_terminal_size().lines)
'''
运行结果如下:
127
6
'''
'''
fill()方法还有一些额外的选项可以用来控制如何处理制表符,句号等.请参阅textwrap.TextWrapper类的文档(
http://docs.python.org/3.3/library/textwrap.html#textwrap.TextWrapper)以获得进一步的细节.
'''