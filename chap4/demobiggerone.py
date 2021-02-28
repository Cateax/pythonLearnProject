# -*- coding: utf-8 -*-
# @Time    : 2021/2/28 16:44
# @Author  : Cateax

# 从键盘获取两个整数，比较大小
a = int(input('请输入第一个数：'))
b = int(input('请输入第二个数：'))

bigger = a if a > b else b
print(bigger)