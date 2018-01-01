# -*- coding:utf-8 -*-"""@author:Levy@file:get_user_id.py@time:2017/12/1414:33"""
import random
import time
import requests
from bs4 import BeautifulSoup
import json
import pyodbc
import os
import time
import selenium
import json
model_movie_ids=[
26862829,
26607693,
26378579,
20495023,
1292052,
1291546,
1292720,
1292722,
1291841,
1291858
]
model_movie_ids2=[26580232,
                  3604148,
                  3011091,
                  26363254,
                  26596361]
'''User-Agent
构建浏览器代理
'''

def getUA():
    UA_list = [
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) App leWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53",
        "Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ;  QIHU 360EE)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; Maxthon/3.0)",
        "'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/5.0 (Macintosh; U; IntelMac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1Safari/534.50",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"]
    return UA_list

'''Cookie池'''
def getCookie():
    cookie_list = [
        'll="118237"; bid=KvZaCPoQKJk; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1490332252%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _vwo_uuid_v2=912FADCFB9317239E37ED315ED9F488F|7ad5255e106b04510fc5d59ed2abc07b; _pk_id.100001.4cf6=490a4f915c676455.1490320279.2.1490333053.1490320313.; _pk_ses.100001.4cf6=*; __utma=30149280.90895996.1490320277.1490320277.1490332251.2; __utmb=30149280.1.10.1490332251; __utmc=30149280; __utmz=30149280.1490332251.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.2019742000.1490320279.1490320279.1490332252.2; __utmb=223695111.0.10.1490332252; __utmc=223695111; __utmz=223695111.1490332252.2.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
        '"ll" = "108296"; bid = V6Dk7UCBgr4; gr_user_id = ef71798b-0eea-4112-8e05-59505bc33fdc;viewed = "10769749_1858513_2221902_6862061_1765426_1977222_1892345_3112503_1462854_1782032"; ct = y; ps = y;ap = 1;dbcl2 = "146518831:pwAN1vWskt8"; ck = kl_f; __utma = 30149280.1933122932.1492703170.1513247615.1513249853.62;__utmb = 30149280.3.10.1513249853;__utmc = 30149280;__utmz = 30149280.1513249853.62.38.utmcsr = movie.douban.com | utmccn = (referral) | utmcmd = referral | utmcct = / subject / 1292052 / collections;utmv = 30149280.14651;push_noty_num = 0;push_doumail_num = 0;_vwo_uuid_v2 = 27AA77ABAE99D11EF7D92C8467B60DD1 | ea352d7b1415b500ab6deea92b0f9ffe;frodotk = "75153fcb7cf44dca5f3fbf6276dce95e"',
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

'''构建代理IP池'''
def proxypool(num):
    n = 1
    # os.chdir(r'/Users/apple888/PycharmProjects/proxy IP')
    fp = open('host.txt', 'r')
    proxys = list()
    ips = fp.readlines()
    while n < num:
        for p in ips:
            ip = p.strip('\n').split('\t')
            proxy = 'https://' + ip[0] + ':' + ip[1]
            proxies = {'http': proxy}
            # print(proxies)
            proxys.append(proxies)
            n += 1
    return proxys

def find_user(cookie,movie_id):


    url = 'https://movie.douban.com/subject/{}/collections'.format(movie_id)
    cookie = 'll="108296"; bid=imFZGDnfer8; __utma=30149280.540834791.1513529863.1513703501.1513708366.8; __utmz=30149280.1513619745.3.3.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/accounts/login; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1513708366%2C%22https%3A%2F%2Fwww.douban.com%2Faccounts%2Flogin%3Fredir%3Dhttps%253A%2F%2Fmovie.douban.com%2Fsubject%2F26862829%2Fcollections%22%5D; _pk_id.100001.4cf6=0b84cb941b456850.1513529870.8.1513708694.1513704179.; __utma=223695111.1713362382.1513529870.1513703501.1513708366.8; __utmz=223695111.1513619745.3.3.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/accounts/login; ps=y; push_noty_num=0; push_doumail_num=0; ap=1; _vwo_uuid_v2=FCD01F65BAFB3827290038ECE855618B|5213d0236b27c6866fd50b81997c0c13; __utmv=30149280.14651; dbcl2="146518831:IB3TzikoGJg"; ck=4TIo; __utmc=30149280; __utmc=223695111; ct=y; _pk_ses.100001.4cf6=*; __utmb=30149280.0.10.1513708366; __utmb=223695111.0.10.1513708366'

    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
               'Connection': 'keep-alive',
               'Cookie': cookie,
               'Host': 'movie.douban.com',
               'Referer': 'https://movie.douban.com/subject/{}/'.format(movie_id),
               'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:57.0) Gecko/20100101 Firefox/57.0',
               }
    r = requests.get(url, headers=headers)
    collections=[]
    for start in range(0,5):
        print (start)
        collection_url=url+'?start={}'.format(20*start)
        print(url)
        html = requests.get(collection_url, headers=headers)
        print(html.text)
        obj_bs = BeautifulSoup(html.text, 'html.parser')
        # 获取带有电影链接的html段
        movie_html = list(obj_bs.findAll("div", {"class": "pl2"}))
        for part in movie_html:
            id=part.a.attrs["href"]
            print(id)
            collections.append(split_user_id(id))
    return collections

def split_user_id(url):
    splits=url.split('/')
    return (splits[-2])


id_collections=[]
for id in model_movie_ids2:
    collections=find_user(0,id)
    for i in collections:
        id_collections.append(i)

with open('id_collections2.txt','w') as f:
    json.dump(id_collections,f)









