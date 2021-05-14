s = "Hello python"

for i in s:
    if i == 'H':
        print(f"There is a {i} in the string!")
        break
    else:
        continue
else:
    print(f"Not in string")
# 如果不由break退出循环,则输出第二个else内容
print(s[0], "<-展示第一个字符->", s[-12])
print(f"字符串的长度为{len(s)}")
# python的string容器中下标索引,第一个为0,也可以最后一个为-1
print(s*5)
# 整型可以乘上字符串,以表示连续输出整型个字符串
# 切片
print(s[1:3])
# 步长不输入默认是1
print(s[1:3:1])
print(s[0:11:3])
# 步长代表n个里面取一个
# 从第二位截取到第三位,不包含end对应的下标

