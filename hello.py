#

# 输出字符串
print("hello,world")

# 含有运算符的表达式
print(3 + 1)

# # 输出到文件
# # 1.必须有文件盘符 2.file = fp
# fp = open('F:\Code\Python\\files\outputs.txt', 'a+')  # a+: 如果文件不存在就创建文件，存在就在文件上进行编辑
# print('hello,world', file=fp)
# fp.close()

# 转义字符
print('hello,\n world')

# 不希望字符串中的转义字符生效,最后一个字符不能是反斜杠
print(r'hello,\n world')