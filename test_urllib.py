import urllib.request as req
# content = req.urlopen("http://www.baidu.com")
# f = open("my 百度.html", "w")
# # print(content.read().decode('utf-8'))
# f.write(content.read().decode('utf-8'))
# f.close()
# post方式获取数0据
import urllib.parse as par
data = bytes(par.urlencode({"hello": "world"}), encoding="utf-8")
content = req.urlopen("http://httpbin.org/post", data=data)
print(content.read().decode("utf-8"))
