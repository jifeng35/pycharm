my_tuple = (60,70)
# my_tuple1 = (50) # 该数据类型仍为<class 'int'>
my_tuple1 = (50,)
print(type(my_tuple))
print(type(my_tuple1))
# 元组内容不可修改
tup = my_tuple+my_tuple1
print(tup)
del my_tuple1
# print(my_tuple1) 此处打印为非法
print(tup[::])
print(tup[1:3:2])
