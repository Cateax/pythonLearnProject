# -*- coding: utf-8 -*-
# @Time    : 2021/3/9 21:20
# @Author  : Cateax

# range() 的三种创建方式

'''第一种创建方式，只有一个参数,默认从0开始，步长为1'''

r = range(10)
print(list(r))

'''第二种创建方式，两个参数，默认步长为1'''
r = range(0,10)
print(list(r))

'''第二种创建方式，三个参数，默认步长为1'''
r =range(1,10,2)
print(list(r))

print(9 in r)
print(6 in r)