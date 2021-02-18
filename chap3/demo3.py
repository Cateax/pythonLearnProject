# -*- coding: utf-8 -*-
# @Time    : 2021/2/18 16:14
# @Author  : Cateax

# 赋值运算符
a = 3+4

b=c=d=20 # 链式赋值，一个对象，三个引用
print(d,id(d))
print(b,id(b))
print(c,id(c))

# 解包赋值,变量和数值个数要相等
x,y,z = 1,2,3
print(x,y,z,id(x),id(y),id(z))
#解包赋值应用：数值交换
i = 1
k = 2
print('交换之前：', i, k)
i,k = k,i
print('交换之后：', i, k)