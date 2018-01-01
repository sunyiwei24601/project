# -*- coding:utf-8 -*-"""@author:Levy@file:get_api_movie.py@time:2017/11/1714:30"""
import requests
from bs4 import BeautifulSoup as Soup
import numpy as np
import time
import json
import urllib3
import ip_agent
import random

url_get_ip="http://www.whatismyip.com.tw"
url_douban_api="https://api.douban.com//v2/movie/search?type=movie&tag="
tags=['剧情', '爱情', '科幻', '喜剧', '动作', '悬疑', '犯罪', '恐怖',"青春","励志","战争","文艺","黑色幽默","传记","情色","暴力","音乐","家庭"]
def get_movie_api_tag(tag,n,proxy=None):
    start=0
    for i in range(n):
        print("******正在获取第"+str(i+1)+"页"+tag+"内容......******")
        details=[]
        doc=requests.get("https://api.douban.com//v2/movie/search?type=movie&tag=" +tag+ '&sort=recommend&start=' + str(start),proxies=proxy)
        s = json.loads(doc.content.decode("utf-8"))
        start+=20
        for j in s["subjects"]:
            print (j["title"])
            details.append(j)
    return details

def try_most(n,url=None,proxy=None):
    start=0
    url="https://api.douban.com//v2/movie/search?type=movie&tag=" + "喜剧" + '&sort=recommend&start='
    for i in range(n):
        print(i,end=" ")
        if not url:
            url = "https://api.douban.com//v2/movie/search?type=movie&tag=" + "喜剧" + '&sort=recommend&start='+ str(start)
        doc=requests.get(url,proxies=proxy)

def get_movie_test(url=None,proxy=None):
    start=0
    cookie=getCookie()
    userAgent=getUA()
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN',
               'Connection': 'Keep-Alive',
               'Cookie': random.choice(cookie),
               'Host': 'api.douban.com',
               'Referer': 'https://api.douban.com//v2/movie/',
               'User-Agent': random.choice(userAgent)}
    if not url:
        url = "https://api.douban.com//v2/movie/search?type=movie&tag=" + "喜剧" + '&sort=recommend&start=' + str(start)
    session=requests.session()
    print(url)
    doc = session.get(url,headers=headers,proxies=proxy)
    return doc.content.decode("utf-8")

def clear_movie_data(filename):
    with open(filename,"w") as f:
        f.write("[{}]")

def clean_tail(filename):
    with open(filename,"rb+") as f:
        f.seek(0,2)
        f.seek(f.tell()-2,0)
        f.write(",".encode("utf-8"))
        f.write(" ".encode("utf-8"))


def getCookie():
    cookie_list = [
        'll="118237"; bid=KvZaCPoQKJk; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1490332252%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _vwo_uuid_v2=912FADCFB9317239E37ED315ED9F488F|7ad5255e106b04510fc5d59ed2abc07b; _pk_id.100001.4cf6=490a4f915c676455.1490320279.2.1490333053.1490320313.; _pk_ses.100001.4cf6=*; __utma=30149280.90895996.1490320277.1490320277.1490332251.2; __utmb=30149280.1.10.1490332251; __utmc=30149280; __utmz=30149280.1490332251.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.2019742000.1490320279.1490320279.1490332252.2; __utmb=223695111.0.10.1490332252; __utmc=223695111; __utmz=223695111.1490332252.2.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
        'll="118237"; bid=KvZaCPoQKJk; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1490332252%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _vwo_uuid_v2=912FADCFB9317239E37ED315ED9F488F|7ad5255e106b04510fc5d59ed2abc07b; _pk_id.100001.4cf6=490a4f915c676455.1490320279.2.1490334307.1490320313.; _pk_ses.100001.4cf6=*; __utma=30149280.90895996.1490320277.1490320277.1490332251.2; __utmb=30149280.1.10.1490332251; __utmc=30149280; __utmz=30149280.1490332251.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.2019742000.1490320279.1490320279.1490332252.2; __utmb=223695111.0.10.1490332252; __utmc=223695111; __utmz=223695111.1490332252.2.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
        'll="118237"; bid=KvZaCPoQKJk; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1490332252%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _vwo_uuid_v2=912FADCFB9317239E37ED315ED9F488F|7ad5255e106b04510fc5d59ed2abc07b; _pk_id.100001.4cf6=490a4f915c676455.1490320279.2.1490334337.1490320313.; _pk_ses.100001.4cf6=*; __utma=30149280.90895996.1490320277.1490320277.1490332251.2; __utmb=30149280.1.10.1490332251; __utmc=30149280; __utmz=30149280.1490332251.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.2019742000.1490320279.1490320279.1490332252.2; __utmb=223695111.0.10.1490332252; __utmc=223695111; __utmz=223695111.1490332252.2.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
        'll="118237"; bid=KvZaCPoQKJk; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1490332252%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_id.100001.4cf6=490a4f915c676455.1490320279.2.1490334547.1490320313.; _pk_ses.100001.4cf6=*; __utma=30149280.90895996.1490320277.1490320277.1490332251.2; __utmb=30149280.1.10.1490332251; __utmc=30149280; __utmz=30149280.1490332251.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.2019742000.1490320279.1490320279.1490332252.2; __utmb=223695111.0.10.1490332252; __utmc=223695111; __utmz=223695111.1490332252.2.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _vwo_uuid_v2=912FADCFB9317239E37ED315ED9F488F|7ad5255e106b04510fc5d59ed2abc07b',
        'll="118237"; bid=KvZaCPoQKJk; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1490332252%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _vwo_uuid_v2=912FADCFB9317239E37ED315ED9F488F|7ad5255e106b04510fc5d59ed2abc07b; _pk_id.100001.4cf6=490a4f915c676455.1490320279.2.1490334576.1490320313.; _pk_ses.100001.4cf6=*; __utma=30149280.90895996.1490320277.1490320277.1490332251.2; __utmb=30149280.1.10.1490332251; __utmc=30149280; __utmz=30149280.1490332251.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.2019742000.1490320279.1490320279.1490332252.2; __utmb=223695111.0.10.1490332252; __utmc=223695111; __utmz=223695111.1490332252.2.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
        'll="118237"; bid=-2pPxf20f-A; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1490334617%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D6-V4k_jr0yx56VVthcFdBh1dsEw-fM_VidsCvjvnZDu%26wd%3D%26eqid%3Ddb5853390004c0f20000000258d4b38f%22%5D; _pk_id.100001.8cb4=cd9595388e4feada.1490334617.1.1490334617.1490334617.; _pk_ses.100001.8cb4=*; __utma=30149280.570766634.1490334619.1490334619.1490334619.1; __utmb=30149280.1.10.1490334619; __utmc=30149280; __utmz=30149280.1490334619.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1',
        'll="118237"; bid=-2pPxf20f-A; __utma=30149280.570766634.1490334619.1490334619.1490334619.1; __utmb=30149280.2.10.1490334619; __utmc=30149280; __utmz=30149280.1490334619.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1490334690%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_id.100001.4cf6=bf4769f7b1df18c6.1490334690.1.1490334690.1490334690.; _pk_ses.100001.4cf6=*; __utma=223695111.922720766.1490334690.1490334690.1490334690.1; __utmb=223695111.0.10.1490334690; __utmc=223695111; __utmz=223695111.1490334690.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _vwo_uuid_v2=33C4215F5DF769BE6B0F85B747086484|15d772cb7307ac132a5f9503a1565460',
        'll="118237"; bid=-2pPxf20f-A; __utma=30149280.570766634.1490334619.1490334619.1490334619.1; __utmb=30149280.2.10.1490334619; __utmc=30149280; __utmz=30149280.1490334619.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1490334690%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_id.100001.4cf6=bf4769f7b1df18c6.1490334690.1.1490334724.1490334690.; _pk_ses.100001.4cf6=*; __utma=223695111.922720766.1490334690.1490334690.1490334690.1; __utmb=223695111.0.10.1490334690; __utmc=223695111; __utmz=223695111.1490334690.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _vwo_uuid_v2=33C4215F5DF769BE6B0F85B747086484|15d772cb7307ac132a5f9503a1565460',
        'll="118237"; bid=-2pPxf20f-A; __utma=30149280.570766634.1490334619.1490334619.1490334619.1; __utmb=30149280.2.10.1490334619; __utmc=30149280; __utmz=30149280.1490334619.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1490334690%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_id.100001.4cf6=bf4769f7b1df18c6.1490334690.1.1490334758.1490334690.; _pk_ses.100001.4cf6=*; __utma=223695111.922720766.1490334690.1490334690.1490334690.1; __utmb=223695111.0.10.1490334690; __utmc=223695111; __utmz=223695111.1490334690.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _vwo_uuid_v2=33C4215F5DF769BE6B0F85B747086484|15d772cb7307ac132a5f9503a1565460',
        'll="118237"; bid=-2pPxf20f-A; __utma=30149280.570766634.1490334619.1490334619.1490334619.1; __utmb=30149280.2.10.1490334619; __utmc=30149280; __utmz=30149280.1490334619.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1490334690%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_id.100001.4cf6=bf4769f7b1df18c6.1490334690.1.1490334785.1490334690.; _pk_ses.100001.4cf6=*; __utma=223695111.922720766.1490334690.1490334690.1490334690.1; __utmb=223695111.0.10.1490334690; __utmc=223695111; __utmz=223695111.1490334690.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _vwo_uuid_v2=33C4215F5DF769BE6B0F85B747086484|15d772cb7307ac132a5f9503a1565460',
        '__utmc=30149280; ll=118237; bid=BpRkUyl8224; __utma=30149280.2117353028.1490334856.1490334856.1490334856.1; __utmb=30149280.1.10.1490334856; __utmz=30149280.1490334856.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; _vwo_uuid_v2=3DE3A5524E7D8D0F707D6C9AEB95A43B|da39a7ae190f4c2de62535e9911c57a6; __utma=223695111.747047863.1490334857.1490334857.1490334857.1; __utmb=223695111.0.10.1490334857; __utmc=223695111; __utmz=223695111.1490334857.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1490334858%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_id.100001.4cf6=0025ca3c57b38c6f.1490334858.1.1490334858.1490334858.; _pk_ses.100001.4cf6=*',
        '__utmc=30149280; ll=118237; bid=BpRkUyl8224; __utma=30149280.2117353028.1490334856.1490334856.1490334856.1; __utmb=30149280.1.10.1490334856; __utmz=30149280.1490334856.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; _vwo_uuid_v2=3DE3A5524E7D8D0F707D6C9AEB95A43B|da39a7ae190f4c2de62535e9911c57a6; __utma=223695111.747047863.1490334857.1490334857.1490334857.1; __utmb=223695111.0.10.1490334857; __utmc=223695111; __utmz=223695111.1490334857.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1490334858%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_id.100001.4cf6=0025ca3c57b38c6f.1490334858.1.1490334918.1490334858.; _pk_ses.100001.4cf6=*']
    return cookie_list

def getUA():
    UA_list = ["Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36","Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) App leWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53",
              "Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13","Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ;  QIHU 360EE)",
              "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; Maxthon/3.0)",
              "'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
              "Mozilla/5.0 (Macintosh; U; IntelMac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1Safari/534.50",
              "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"]
    return UA_list

'''
for tag in tags[8:12]:
    filename=tag+".json"
    data_movies=get_movie_api_tag(tag,25)
    data_movies_str=json.dumps(data_movies)
    with open(filename,"w") as f:
        json.dump(data_movies_str,f)
        '''

