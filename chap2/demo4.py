# -*- coding: utf-8 -*-
# @Time    : 2021/2/18 15:22
# @Author  : Cateax

# 类型转换
name = 'Cateax'
age = 14

print(type(name),type(age))

print('我叫'+ name + '今年' +str(age))

s1 = '111'
f = 1.11
s2 = '22.21'
boo = True
s3 = 'hello'

print(type(s1), type(f), type(s2), type(boo), type(s3))

print(int(s1), type(int(s1))) #字符串为整数时可转换
print(int(f), type(int(f))) #浮点型转为int时丢失小数部分

#print(int(s2), type(int(s2)))
#字符串为浮点型数时不能转换

print(int(boo), type(int(boo)))
#True为1

#print(int(s3), type(int(s3)))
#字符串为字符时不能转换