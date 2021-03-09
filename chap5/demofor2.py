# -*- coding: utf-8 -*-
# @Time    : 2021/3/9 22:30
# @Author  : Cateax

# 输出100到999之间的水仙花数

for item in range(100,1000):
    ge = item%10
    shi = item//10 %10
    bai = item // 100

    if ge**3 + shi**3 + bai**3 == item:
        print(item)