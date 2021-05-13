print('ascii', 18)
# 输出ascii和18以空格隔开
name = "jifeng"
print("我是%s,我是废物" % name)
# 格式化输出
# %s为占位使用(数据类型为字符串),可将内容改为变量进行输出
# 还有例如%d(int)%f(float)%c(char)
print(1+2)
age1 = 10
age2 = 9
print("今年%d岁" % (age1 + age2))
height = 168.65
print("我的身高是%fcm" % height)
# ctrl+d可快速复制一行代码(选中行)
# shift+enter在任意位置换行
print("我的身高是%.2fcm" % height)
# 小数输出默认保留六位小数,%.nf即为保留n位小数
print("我叫%s,我身高%.2fcm,我今年%d岁" % (name, height, (age1 + age2)))
# 多占位格式化输出如上所示
print(f"我叫{name},我身高{height}cm,我今年{age1+age2}岁")
# python3.6开始支持f-string,使用大括号{}占位,数据填入即可
print("%d%%" % 50)
# 在使用格式化输出时输出百分号需要输入两个百分号
print("hello world\nI am jifeng")
# \n换行,print默认在末尾加入一个换行,可以自定义print结束末尾内容
print("ji", end=" ")
print("feng")

