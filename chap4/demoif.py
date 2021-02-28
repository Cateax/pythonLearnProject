# -*- coding: utf-8 -*-
# @Time    : 2021/2/28 14:39
# @Author  : Cateax

money = 1000
s = int(input('请输入取款金额'))

# 判断余额是否充足
if money >= s:
    money = money - s
    print('取款成功，余额为：',money)