#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/12/19

'''
Problem:
You need to format a number for output,controlling the number of digits,alignment,inclusion of a thousands separator, and other details.
'''
'''
Solution:
To format a single number for output, use the built-in format() function.For example:
'''
x = 1234.56789
#Two decimal places of accuracy
print(
    format(x, '0.2f')
)

# Right justified in 10 chars, one-digit accuracy
print(
    format(x, '>10.1f')
)

# Left justified

print(
    format(x, '<10.1f')
)

# centered

print(
    format(x, '^10.1f')
)

# Inclusion of thousands separator

print(
    format(x, ',')
)

print(
    format(x, '0,.1f')
)

'''
1234.57
    1234.6
1234.6    
  1234.6  
1,234.56789
1,234.6
'''

'''
If you want to use exponential notation,change the f 
to an e or E, depending on the case you want used 
for the exponential specifier.
For example:
'''
print(
    format(x, 'e')
)

print(
    format(x, '0.2E')
)
'''
1.234568e+03
1.23E+03
'''

'''
The general form of the width and precision in both
cases is '[<>^]?width[,]?(.digits)?' where width 
and digits are integers and ? signifies optional
parts. The same format codes are also used in the 
.format() method of string.
For example:
'''
print(
    'The value is {:0.2f}'.format(x)
)

'''
The value is 1234.57
'''

'''
Discussion:
Formatting numbers for output is usually straightforward. The eachnique shown works for both floating-point numbers and Decimal numbers in the decimal module.
When the number of digits is restricted, values are rounded away according to the same rules of the round() function. For example:
'''
x = 1234.56789
print(
    format(x, '0.1f')
)

print(
    format(-x, '0.1f')
)
'''
1234.6
-1234.6
'''

'''
Formatting of values with a thousands separator is not locale aware. If you need to take that into account, you might investigate functions in the locale module. You can also swap separator characters using the translate() method of strings.
For example:
'''

swap_separators = {
    ord('.'):',',
    ord(','):'.'
}

print(
    format(x,',').translate(swap_separators)
)

'''
1.234,56789
'''

'''
In a lot of Python code,numbers are formatted using the % operator.
For example:
'''
print(
    '%0.2f' % x
)

print(
    '%10.1f' % x
)

print(
    '%-10.1f' % x
)

'''
1234.57
    1234.6
1234.6    
'''

'''
This formatting is still acceptable, but less powerful than the more modern format() method.
For example, some features (e.g.,adding thousands separators) aren't supported when using the % operator to format numbers.
'''























