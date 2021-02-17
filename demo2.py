# -*- coding: utf-8 -*-
# @Time    : 2021/2/17 16:01
# @Author  : Cateax
# 数据类型

print('十进制', 118)
print("二进制", 0b11111111) #二进制0b开头
print('八进制',0o777)  #八进制0o开头

a = 3.14
print(type(a))

#使用decimal可以消除浮点数运算误差
a = 1.1
b = 2.2
c = 2.1
print(a+b)
print(a+c)

from decimal import Decimal
print(Decimal('1.1') + Decimal('2.2'))

#boolean型
f1 = True
f2 = False
# 布尔型可以转成整数计算
print(f1+1)
print(f2+1)

