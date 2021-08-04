import urllib.request as req
content = req.urlopen("http://www.baidu.com")
f = open("my 百度.html", "w")
# print(content.read().decode('utf-8'))
f.write(content.read().decode('utf-8'))
f.close()
