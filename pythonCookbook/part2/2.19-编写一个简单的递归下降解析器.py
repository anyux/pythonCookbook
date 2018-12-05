#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/11/22

'''
question:
我们需要根据一组语法规则来解析文本,以此执行相应的操作或构建一个抽象语法树来表示输入.语法规则很简单,因此我们倾向于自己编写解析器而不使用某种解析器框架.
'''

'''
解决方案:
在这个问题中,我们把重点放在根据特定的语法来解析文本上.要做到这些,应该以BNF或EBNF的形式定义出语法的正式规格.比如,
对于简单的算术运算表达式.语法看起来是这样的:
'''
'''
expr    :: =expr + term
        |   expr - term
        |   term
expr    :: =term * factor
        |   term / factor
        |   factor
factor  :: =(expr)
        |   NUM
'''

'''
又或者以EBNF的形式定义为如下形式:
'''

