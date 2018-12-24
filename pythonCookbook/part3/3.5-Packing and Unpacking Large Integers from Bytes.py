#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/12/23

'''
Problem:
You have a byte string and you need to unpack it into an integer value.Alternatively,you need to convert a large integer back into a byte string.
'''
'''
Solution:
Suppose your program needs to work with a 16-element byte string that holds a 128-bit integer value.For example:
'''
data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'

'''
To interpret the bytes as an integer,use int.from_bytes(),and specify the byte ordering like this:
'''
print(
    len(data)
)

print(
    int.from_bytes(data, 'little')
)

print(
    int.from_bytes(data, 'big')
)

'''
To convert a large integer value back into a byte string,use the int.to_bytes() method,specifying the number of bytes and the bytes and the byte order.For exmaple:
'''
x = 94522842520747284487217727783387188
print(
    x.to_bytes(16, 'big')
)

print(
    x.to_bytes(16, 'little')
)

'''
Discussion:
Converting large integer valeus to and from byte strings is not a common operation.However,it someitmes arises in certain application domains,such as cryptography or networking.For instance,IPv6 network addresses are represented as 128-bit integers. If you are writing code that needs to pull such values out of a data record,you might face this problem.
As an alternative to this recipe,you might be inclined to unpack values using the struct module, as described in Recipe 6.11. This works,but the size of integers that can be unpacked with struct is limited.Thus,you would need to unpack umltiple values and combine them to create the final value.For example:
'''
print(data)

import struct

hi, lo = struct.unpack('>QQ', data)
print(
    (hi << 64) + lo
)

'''
The specification of the byte order(little or bit) just indicates whether the bytes that make up the integer value are listed from the least to most significant or the orther way around.This is easy to view using a carefully carefully crafted hexadecimal value:
'''
x = 0x01020304
print(
    x.to_bytes(4, 'big')
)
print(
    x.to_bytes(4, 'little')
)

'''
If you try to pack an integer into a byte string,but it won't fit,you'll get an error.You can use the int.bit_length() method to determine how many bits are required to store a value if needed:
'''
x = 523 ** 23

print(
    x
)

# print(
#     x.to_bytes(16, 'little')
# )
print(
    x.bit_length()
)
print(
    nbytes, rem = divmod(x.bit_length(), 8)
)

if rem:
    nbytes += 1


print(
    x.to_bytes(nbytes, 'little')
)











