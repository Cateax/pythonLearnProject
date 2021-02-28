# -*- coding: utf-8 -*-
# @Time    : 2021/2/28 16:02
# @Author  : Cateax

'''会员 >200 八折
        >= 100 九折
        其余情况不打折
    非会员 >= 200 9.5折
          其余情况不打折'''

identity = input("您是会员吗？y\n")
money = float(input('请输入您的购物金额：'))
# 外层判断是否是会员
if identity == 'y':
    print('会员')
    if money > 200:
        print('打八折，付款金额为：', money*0.8)
    elif money >= 100 and money <= 200:
        print('打九折，付款金额为：', money*0.9)
    else:
        print('不打折，付款金额为：', money)
else:
    print('非会员')
    if money >= 200:
        print('打九五折，付款金额为：', money*0.95)
    else:
        print('付款金额为：', money)