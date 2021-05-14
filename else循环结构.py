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
# python的string容器中下标索引,第一个为0,也可以最后一个为-1
