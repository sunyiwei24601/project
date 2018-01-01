# -*- coding:utf-8 -*-"""@author:Levy@file:get_user_details.py@time:2017/12/1414:32"""
import requests
from bs4 import BeautifulSoup
import json
import random
import time



def get_cookie():

    cookies = [
       'll="108296"; bid=imGZGDnver8; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1513880481%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DPD8sEabTyr6QuW1rsUJlJFfNMziKL08PEl071Kifz_CpkT2pOsDUvky1RycrtmtBo-cwI25KgSr32A8c4F-HJa%26wd%3D%26eqid%3Dc1417e0600005bfb000000045a3bfb9d%22%5D; _pk_id.100001.8cb4=1eb11aa368062b28.1513529859.6.1513880507.1513868740.; __utma=30149280.540834791.1513529863.1513880481.1514114570.14; __utmz=30149280.1514114570.14.7.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); ps=y; push_noty_num=0; push_doumail_num=0; ap=1; _vwo_uuid_v2=FCD01F65BAFB3827290038ECE855618B|5213d0236b27c6866fd50b81997c0c13; __utmv=30149280.14651; ct=y; ue="664629747@qq.com"; dbcl2="147826859:cI6QqO2YFtE"; ck=LPAb'
      'll="108296"; bid=imGZGDnver7; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1513880481%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DPD8sEabTyr6QuW1rsUJlJFfNMziKL08PEl071Kifz_CpkT2pOsDUvky1RycrtmtBo-cwI25KgSr32A8c4F-HJa%26wd%3D%26eqid%3Dc1417e0600005bfb000000045a3bfb9d%22%5D; _pk_id.100001.8cb4=1eb11aa368062b28.1513529859.6.1513880507.1513868740.; __utma=30149280.540834791.1513529863.1513880481.1514114570.14; __utmz=30149280.1514114570.14.7.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); ps=y; push_noty_num=0; push_doumail_num=0; ap=1; _vwo_uuid_v2=FCD01F65BAFB3827290038ECE855618B|5213d0236b27c6866fd50b81997c0c13; __utmv=30149280.14651; ct=y; ue="664629747@qq.com"; dbcl2="147826859:cI6QqO2YFtE"; ck=LPAb',
       'll="108296"; bid=imGZGDnver9; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1513880481%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DPD8sEabTyr6QuW1rsUJlJFfNMziKL08PEl071Kifz_CpkT2pOsDUvky1RycrtmtBo-cwI25KgSr32A8c4F-HJa%26wd%3D%26eqid%3Dc1417e0600005bfb000000045a3bfb9d%22%5D; _pk_id.100001.8cb4=1eb11aa368062b28.1513529859.6.1513880507.1513868740.; __utma=30149280.540834791.1513529863.1513880481.1514114570.14; __utmz=30149280.1514114570.14.7.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); ps=y; push_noty_num=0; push_doumail_num=0; ap=1; _vwo_uuid_v2=FCD01F65BAFB3827290038ECE855618B|5213d0236b27c6866fd50b81997c0c13; __utmv=30149280.14651; ct=y; dbcl2="146925119:8UFklI1xE30"; ck=MkYc; ue="877646746@qq.com"'
    ]
    return random.choice(cookies)

def get_agent():
    UA_list = [
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) App leWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53",
        "Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ;  QIHU 360EE)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; Maxthon/3.0)",
        "'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/5.0 (Macintosh; U; IntelMac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1Safari/534.50",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"]
    return random.choice(UA_list)

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

def get_headers():
    cookie=get_cookie()
    headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
     'Accept-Encoding': 'gzip, deflate, br',
     'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
     'Connection': 'keep-alive',
     'Cookie': cookie,
     'Host': 'movie.douban.com',
     'Origin': 'https://movie.douban.com',
     'Referer': "https://www.douban.com/people/170279827/",
     'User-Agent': get_agent(),
     'Upgrade-Insecure-Requests': '1',
     'Cache-Control': 'max-age=0'
     }
    return headers

def get_movie_id(url):
    splits=url.split("/")
    return splits[-2]



def get_details(id,proxy=None,headers=None):
    base_url="https://movie.douban.com/people/{}/collect".format(id)
    proxies=random.choice(proxy)
    r1 = requests.get(base_url,proxies=proxies,headers=get_headers())
    rcontent = r1.text
    print(rcontent)
    soup=BeautifulSoup(rcontent,"html.parser")
    #得到最大数量
    try:
        num = soup.find_all("span", {"class": "subject-num"})[0]
    except:
        return None
    splits = num.text.split("/")
    nums = int(splits[-1])
    if nums>=105:
        nums=105
    indexs=[]
    for i in range(1,int(nums/15)+2):
        indexs.append(base_url+'?start='+str((i-1)*15)+"&sort=time&rating=all&filter=all&mode=grid")
    details=[]
    for index in indexs:
        proxies = random.choice(proxy)
        time.sleep(random.uniform(1.6, 2.1))
        page=requests.get(index,proxies=proxies,headers=get_headers())
        soup=BeautifulSoup(page.text,"html.parser")

        titles=soup.find_all("li",{'class':'title'})
        for i in titles:
            movie_url=i.a.attrs["href"]
            print(movie_url)
            detail=[]
            detail.append(get_movie_id(movie_url))
            sublings=list(i.next_siblings)
            rates=sublings[3].span.attrs["class"]
            print(rates)
            date=sublings[3].find("span",{'class':'date'}).text
            print(date)
            detail.append(rates)
            detail.append(date)
            details.append(detail)


    return details



id="122251575"

with open("id_collections3.txt") as f:
    ids=json.load(f)
details=[]
n=400

for id in ids[400:500]:
    detail={}
    detail['id']=id

    try:
        rates=get_details(id,proxy=proxypool(100))
    except:
        break
    detail['rates']=rates
    try:
        if(rates==None):
            print(("在第{}位用户停下").format(n))
            break
    except:
        print(("在第{}位用户停下").format(n))
        break

    details.append(detail)
    print(("————————*****{}*****————————").format(n))
    n+=1


with open("user_details400-500.txt",'w') as f:
    json.dump(details,f)

