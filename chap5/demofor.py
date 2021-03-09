# -*- coding: utf-8 -*-
# @Time    : 2021/3/9 22:18
# @Author  : Cateax

for item in 'Python':
    print(item)

for i in range(10):
    print(i)

for _ in range(5):
    print('Hello,World')

sum = 0
for item in range(1,101):
    if item%2 == 0:
        sum += item

print('1到100之间的偶数和是：', sum)