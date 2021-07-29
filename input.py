password = input("请输入密码:")
print(f"您输入的密码为{password}")
print(f"密码的数据类型为{type(password)}")
print(f"密码的数据类型为{type(eval(password))}")
# input函数输入的数据类型均为字符串类,用户输入回车则输入结束
secret = 1
word = eval('secret')
print(f"word的数据类型为{type(word)}")
secret0 = "11"
name = "j"
# python中没有char数据类型
print(f"名字的类型是{type(eval(name))}")
word0 = eval('secret0')
print(f"word0的数据类型为{type(word0)}")
# eval()不能传入字符串类型的数据,否则会报错
# eval()函数可理解为去掉引号,显然字符串不能去掉引号


0