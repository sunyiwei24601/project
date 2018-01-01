# -*- coding:utf-8 -*-"""@author:Levy@file:chapter5.py@time:2017/12/1521:17"""
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html,'html.parser')
imageLocation = bsObj.find("a", {"id": "logo"}).find("img")["src"]
urlretrieve (imageLocation, "logo.jpg")

import smtplib