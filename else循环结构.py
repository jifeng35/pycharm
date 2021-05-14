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

