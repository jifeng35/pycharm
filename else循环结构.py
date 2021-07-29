s = "Hello python"

for i in s:
    if i == 'H':
        print(f"There is a {i} in the string!")
        break
    else:
        continue
else:
    print(f"Not in string")
# 如果不由break退出循环,则输出第二个else内容J
print(s[0], "<-展示第一个字符->", s[-12])
print(f"字符串的长度为{len(s)}")
# python的string容器中下标索引,第一个为0,也可以最后一个为-1
print(s*5)
# 整型可以乘上字符串,以表示连续输出整型个字符串
# 切片
print(s[1:3])
# 步长不输入默认是1 end位置不输入默认是最后一位 start位置不写默认是开始位置
print("1", s[1:3:1])
print("2", s[1:3:])
print("3", s[3:1:-1])
print("4", s[0::3])
print("5", s[:])
print("6", s[0:len(s)])
print("7逆置字符串", s[::-1])
print("字符串切片的所有值都可以取负数")
passage = '''
    这是一个段落
    可以进行多行的输出
'''
sentence = "jeff said :\"I am your teacher!\""
print(sentence)
# \单双引号进行转义避免引发报错
sentence = 'jeff said :"I am your teacher!!"'
# 使用不同的引号来进行编写可避免该问题
print(sentence)
# print('\b',end="b")
print(passage, end="end")
# 步长代表n个里面取一个
# 从第二位截取到第三位,不包含end对应的下标
print("hello\nworld!")
print(r"hello\nworld!")
# 输出字符串前面加上r可取消所有转义功能

