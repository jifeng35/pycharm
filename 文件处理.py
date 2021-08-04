# f = open("hello world.txt", "w")
# f.write("Hello world! My name is jifeng")  write模式会覆盖掉以前的内容,若想追加应使用add模式
# f.close()
f = open("hello world.txt", "r")
content = f.readlines()
i = 1
for temp in content:
    print(f"这是第{i}行:", temp, end="")
    i += 1
f.close()
f = open("hello world.txt", "r")
print("\n", f.readline(), end="")
print(f.readline())
