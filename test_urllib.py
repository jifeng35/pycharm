import urllib.request as req
content = req.urlopen("http://www.baidu.com")
f = open("my 百度.html", "w")
f.write(content.read().decode("utf-8"))
