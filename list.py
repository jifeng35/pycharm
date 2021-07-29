my_list = [1, 'a', 2.3875, "小李"]
print(my_list)
print(my_list[3], "输出末尾元素的两种方式", my_list[-1])
# -1是最后一个 0是第一个元素
print(type(my_list[0]))
print(type(my_list[1]))
print(type(my_list[2]))
print(type(my_list[3]))
# 列表中存储的元素为定义时的数据类型
for i in my_list:
    print(i, end=",")
print("列表的长度为:", len(my_list))
j = 0
while j < len(my_list):
    print(my_list[j], end=",")
    j += 1
my_list.append("A1")
# append = push_back
for i in my_list:
    print(i, end=",")
print("列表的长度为:", len(my_list))
a = [1, 2]
b = [3, 4]
a.append(b)
# append 是将括号内的数据作为一个元素插入到list中
print(a)
a.extend(b)
# extend 为扩展,将a中插入b中所有的单个元素
print(a)
