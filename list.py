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
a.insert(0, 'see')
# insert(int pos,template<class T> T object)
print(a)
del a[0]
print(a)
a.pop()
# pop()=pop_back()
print(a)
a.remove(b)
# 列表中内容重复,删除的时候删除对应内容下标较小的那个
# a.remove(10) 输入不存在的数据会报错,抛出异常
# 删除的是元素内容
print(a)
if 'q' in a:
    print("exist")
else:
    print("cannot find!")
print(a.index(1, 0, len(a)))
# 范围区间左闭右开,不包含结尾数字的对应下标的元素
print(a.count(1))
a.insert(3, 0)
a.insert(0, 4)
a.insert(0, 8)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
