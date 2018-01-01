# -*- coding:utf-8 -*-"""@author:Levy@file:ip-agent.py@time:2017/11/1713:52"""
import requests
import json
import numpy as np
import time
import urllib
from bs4 import BeautifulSoup
import random

def get_ip_list(url, headers):
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[1].text + ':' + tds[2].text)
    return ip_list

def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    return proxies

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"}

def get_ip_good(view=False):
    n = 0
    url_ip = 'http://www.xicidaili.com/nn/'
    url_test="http://www.baidu.com/"

    ip_list = get_ip_list(url_ip, headers=headers)
    while True:
        try:
            a=time.time()
            if view:
                print(n)
            n += 1
            proxy = get_random_ip(ip_list)
            requests.get(url_test,proxies=proxy)
            b=time.time()
            if view:
                print(proxy,b-a)
            return proxy
        except Exception:
            b = time.time()
            if view:
                print(proxy,b-a)

def test_ip(proxy=None):
    url_ip_test="http://www.whatismyip.com.tw/"
    doc=requests.get(url_ip_test,proxies=proxy,headers=headers)
    soup=BeautifulSoup(doc.content,"html.parser")
    ip=soup.find_all("div",class_="ip")
    ip_num=[]
    return doc.content.decode("utf-8")

def test_ip2(proxy=None):
    url_ip_test= "http://whatismyip.org"
    doc = requests.get(url_ip_test, proxies=proxy,headers=headers)
    soup = BeautifulSoup(doc.content, "html.parser")
    ip = soup.find_all("span")
    return doc.content.decode("utf-8")

if __name__=="__main__":
    #print (get_ip_good(view=True))
    print (test_ip2(proxy={"http":"http://139.196.126.158"}))
