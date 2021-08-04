import urllib.request as req
# content = req.urlopen("http://www.baidu.com")
# f = open("my 百度.html", "w")
# # print(content.read().decode('utf-8'))
# f.write(content.read().decode('utf-8'))
# f.close()
# post方式获取数0据
import urllib.parse as par
import urllib.error as err
data = bytes(par.urlencode({"hello": "world"}), encoding="utf-8")
try:
    content = req.urlopen("http://httpbin.org/post", data=data, timeout=3)  # data是发送的数据,timeout是最大响应时长
    print(content.read().decode("utf-8"))
    print("状态码为:", content.status)
    print(content.getheader("Date"))
    print(content.getheaders())
except err.URLError as e:
    print("Time out!\n", e)


# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
# Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62
