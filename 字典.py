info = {"name": "jifeng", "age": "19"}
print(info["name"])
# print(info["hobby"]) 潜在的非法访问,解决方法为下一行
print(info.get("hobby"))  # 默认返回值是None,可更改默认返回值
print(info.get("hobby", "basketball"))
info["id"] = "2020212265"  # 字典此种数据结构类似c++中的pair数据结构 通过key值索引value
# 增添内容方式与修改value内容方式相同,赋值即可
print(info.get("id"))
del info["id"]
print(info.get("id"))
del info
# print(info) 打印内容非法
info = {"name": "jifeng", "age": "19"}
info.clear()
print(info)  # 清空字典内容,将该字典仍然保留在内存中 del是从内存中删除
info = {"name": "jifeng", "age": "19"}
print(info.items())
print(info.keys())
print(info.values())
for key, value in info.items():  # 循环中可以有两个数值
    print(key, "\t", value)
