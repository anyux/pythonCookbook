#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/11/15

'''
question:
我们正同Unicode字符串打交道,但需要确保所有的字符串都拥有相同的底层表示.
'''

'''
解决方案:
在Unicode中,有些特定的字符可以被表示成多种合法的代码点序列.为了说明这个问题,请看下面的示例:
'''
s1 = 'Spliy Jalape\u00f1o'
s2 = 'Spliy Jalapen\u0303o'

print(s1)

print(s2)

print(s1 == s2)

print(len(s1))

print(len(s2))

'''
运行结果如下:

Spliy Jalapeño
Spliy Jalapeño
False
14
15

'''
'''
这里的文本"Spliy Jalapeñ"以两种形式呈现.第一种使用的是字符"ñ"的全组成(fully composed)形式 (
U+00F1).第二种使用的是拉丁字母"n"紧跟着一个"~"组合而成的字符(U+0303).
对于一个比较字符串的程序来说,同一个文本拥有多种不同的表示形式是个大问题.为了解决这个问题,应该先将文本统一表示为规范形式,
这可以通过unicodedata模块来完成:
'''

import unicodedata

t1 = unicodedata.normalize('NFC',s1)
t2 = unicodedata.normalize('NFC',s2)

print(t1 == t2)

print(ascii(t1))

t3 = unicodedata.normalize('NFD',s1)
t4 = unicodedata.normalize('NFD',s2)

print(t3 == t4)

print(ascii(t3))

'''
运行结果如下:

True
'Spliy Jalape\xf1o'

True
'Spliy Jalapen\u0303o'

'''
'''
normalize()的第一个参数指定了字符串应该如何完成规范表示.NFC表示字符串应该是全组成的(即,
如果可能的话就使用单个代码点).NFD表示应该使用组合字符.每个字符应该能完全分解开的.
python还支持NFKC和NFKD的规范形式,它们为处理特定类型的字符增加了额外的兼容功能.例如:
'''
s = '\ufb01' # A single character
print(s)

print(unicodedata.normalize('NFD',s))


# Notice how the combined letters are broken apart here

print(unicodedata.normalize('NFKD',s))

print(unicodedata.normalize('NFKC',s))

'''
运行结果如下:
ﬁ
ﬁ
fi
fi
'''
'''
讨论:
对于任何需要确保以规范和一致性的方式处理Unicode文本的程序来说,规范化都是重要的部分.尤其是在处理用户输入时接收到字符串时,
此时你无法控制字符串的编码形式,那么规范化文本的表示就显得尤其重要了.
在对文本进行过滤和净化时,规范化同样也占据了重要的部分.例如,假设想从某些文本中去除音符标记(可能是为了进行搜索或匹配):
'''
t1 = unicodedata.normalize('NFD',s1)

print(''.join(c for c in t1 if not unicodedata.combining(c)))

'''
最生一个例子展示了 unicodedata模块的另一个重要功能----用来检测字符是否属于某个字符类别.使用工具combining()函数可对字符做检查,
判断它是否为一个组合型字符.这个模块有一些函数可用来查找字符类别,检测数字字符等.
很显然,Unicode是一个庞大的主题.要获得更多有关规范化文本方面的参考信息,
访问http://www.unicode.org/faq/normalization.html.Ned 
Batchelder也在他的网站https://nedbatchelder.com/text/unipain.html上对Python中的Unicode
处理给出了优秀的示例说明.
'''








