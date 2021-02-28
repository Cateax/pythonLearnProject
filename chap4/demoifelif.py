# -*- coding: utf-8 -*-
# @Time    : 2021/2/28 15:43
# @Author  : Cateax

'''多分支结构，多选一执行
    从键盘录入一个整数
    90 - 100 A
    80 - 89 B
    '''

score = int(input("请输入一个分数："))
if score >= 90 and score <=100:
    print("A")
elif score >= 80 and score <=89:
    print("B")
elif score >= 70 and score <= 79:
    print("C")
elif score >= 60 and score <= 69:
    print("D")
elif score >= 0 and score <= 59:
    print("E")
else:
    print("分数无效")