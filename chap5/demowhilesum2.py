# -*- coding: utf-8 -*-
# @Time    : 2021/3/9 22:14
# @Author  : Cateax

'''计算1到100之间的偶数和'''

'''初始化变量'''
a = 0
sum = 0

'''条件判断'''
while a < 100:
    '''条件执行体（循环体）'''
    if not bool(a%2):
        sum+=a
    '''改变变量'''
    a+=1

print(sum)