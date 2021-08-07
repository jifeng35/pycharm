# -*- coding = utf-8 -*-
# 保证中文处理正常
from bs4 import BeautifulSoup as BS
import re
import urllib.request as req
import urllib.error as err
import xlwt
import sqlite3


def main():
    print("hello")
    # base_url = "https://movie.douban.com/top250?start="
    base_url = "https://www.baidu.com"
    save_path = r".\豆瓣电影250.xls"
    datalist = get_data(base_url)
    ask_url(base_url)


def ask_url(url):
    head = {"cookie": "_uuid=26BE186F-3B70-CCA5-9AF7-65D5C7E320EC54650infoc;buvid3=FA91269B-717D-49AC-92C7"
                      "-DD65181615FB184986infoc;URRENT_FNVAL=80; blackside_state=1; rpdid=|("
                      "u)YRkmY)Y|0J'uYulY|J)R);fingerprint=4f4a20d7dcf8185caa999d828634e398;buvid_fp=FA91269B-717D"
                      "-49AC-92C7-DD65181615FB184986infoc;buvid_fp_plain=FA91269B-717D-49AC-92C7"
                      "-DD65181615FB184986infoc;SESSDATA=392d90c5,1631155896,d552a*31; "
                      "bili_jct=2b25e43a627742569b78dab01216af2f;DedeUserID=15823751;DedeUserID__ckMd5"
                      "=8bc95b4438e931d3; sid=c55dom7v; LIVE_BUVID=AUTO6216170138703774; PVID=1; CURRENT_QUALITY=64 "
        , "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62"
            }
    test01 = req.Request(url=url, headers=head)
    html = ""
    try:
        html = req.urlopen(test01).read().decode('utf-8')
        # print(html)
    except err.URLError as e:
        print("出错了!")
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


def get_data(base_url):
    datalist = []
    for i in range(0, 1):
        url = base_url + str(i*25)
        html = ask_url(base_url)  # 获取网页源码
        # 逐个进行解析
        ana = BS(html, "html.parser")
        # print(ana.name, type(ana))
        # print(ana.title, type(ana.title))
        # print(ana.title.string, type(ana.title.string))
        # print(ana.a.attrs, type(ana.a.attrs))
        # print(ana.a, type(ana.a))
        # ------------------文档的遍历------------------
        # print(ana.head.contents) 遍历head中所有元素 list方式存储及返回
        # ------------------文档的搜索------------------

    return datalist


def save_data(save_path):
    return 0


if __name__ == "__main__":
    # 调用函数 程序入口
    main()
