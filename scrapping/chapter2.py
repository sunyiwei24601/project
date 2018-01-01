# -*- coding:utf-8 -*-"""@author:Levy@file:chapter2.py@time:2017/12/151:11"""
import urllib
from download2 import download
import re
from bs4 import BeautifulSoup
url='http://www.pythonscraping.com/pages/page3.html'
html=download(url)
bsObj=BeautifulSoup(html,'lxml')
for sibling in bsObj.find("table",{'id':'giftList'}).tr.next_siblings:
    print(sibling)

print(len(list(bsObj.find("table",{'id':'giftList'}).tr.next_siblings)))
