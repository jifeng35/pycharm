# -*- coding = utf-8 -*-
# 保证中文处理正常
from bs4 import BeautifulSoup
import re
import urllib.request as req
import urllib.error as err
import xlwt
import sqlite3


def main():
    print("hello")
    base_url = "https://movie.douban.com/top250?start="
    save_path = r".\豆瓣电影250.xls"
    datalist = get_data(base_url)


def get_data(base_url):
    datalist=[]
    return datalist


def save_data(save_path):
    return 0


if __name__ == "__main__":
    # 调用函数 程序入口
    main()
