# coding=utf-8
import random
import time
import requests
from bs4 import BeautifulSoup
import json
import pyodbc
import os
import time

#爬取ip地址
def fetch_proxy(num):
    api = 'http://www.xicidaili.com/nn/'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
    # 保存到本地文件
    fp = open('F:\host.txt', 'w', encoding=('utf-8'))
    ass=0
    for i in range(num + 1):
        api = api + str(i)
        respones = requests.get(url=api, headers=header)
        soup = BeautifulSoup(respones.text, 'html.parser')
        container = soup.find_all(name='tr', attrs={'class': 'odd'})
        print(container)
        for tag in container:
            try:
                con_soup = BeautifulSoup(str(tag), 'html.parser')
                td_list = con_soup.find_all('td')
                ip = str(td_list[1])[4:-5]
                port = str(td_list[2])[4:-5]
                IPport = ip + '\t' + port + '\n'
                fp.write(IPport)
            except Exception as e:
                print('No IP！')
                # 这里要控制爬取频率，友好爬虫
        time.sleep(1)
    fp.close()

def fetch_proxy2(num):
    api = 'http://www.kuaidaili.com/free/inha/'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
    # 保存到本地文件
    fp = open('host.txt', 'w', encoding=('utf-8'))
    ass = 0
    for i in range(num + 1):
        print("i")
        api = api + str(i)
        respones = requests.get(url=api, headers=header)
        soup = BeautifulSoup(respones.text, 'html.parser')
        container = soup.find_all(name='tr')

        for tag in container[1:]:
            try:
                con_soup = BeautifulSoup(str(tag), 'html.parser')
                ip = con_soup.find_all('td',attrs={"data-title":"IP"})[0].get_text()
                port=con_soup.find_all("td",attrs={"data-title":"PORT"})[0].get_text()

                IPport = ip + '\t' + port + '\n'
                fp.write(IPport)
            except Exception as e:
                print('No IP！')
                # 这里要控制爬取频率，友好爬虫
        time.sleep(1)
    fp.close()

'''
User-Agent
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

'''
Cookie池

'''

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

'''
构建代理IP池
'''

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

'''
getMoviePakge()
此函数用于获取电影列表页面的url链接
返回值为列表pakge_urls
'''

def getMoviePakge(start,end):
    pakge_urls = []
    for i in range(start, end, 20):
        url = 'https://movie.douban.com/tag/%E7%88%B1%E6%83%85?start=' + str(i) + '&type=T'

        pakge_urls.append(url)
    return pakge_urls

'''getMovieUrls()
此函数用于获取电影的链接用于后面的信息的访问url入口
返回一个列表，里面存储着电影链接
'''

def getMovieUrls(pakgeurl, cookie, userAgent, proxys):
    movie_urls = []
    time.sleep(random.uniform(1.6, 2.1))
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN',
               'Connection': 'Keep-Alive',
               'Cookie': random.choice(cookie),
               'Host': 'movie.douban.com',
               'Referer': 'https://movie.douban.com/tag/',
               'User-Agent': random.choice(userAgent)}

    session = requests.Session()
    html = session.get(pakgeurl, headers=headers, proxies=random.choice(proxys))
    obj_bs = BeautifulSoup(html.text, 'html.parser')
    # 获取带有电影链接的html段
    movie_html = list(obj_bs.findAll("div", {"class": "pl2"}))
    for each_movie in movie_html:
        # 获取电影介绍的链接
        movie_url = each_movie.select('a')[0]['href']
        # print(movie_url)
        movie_urls.append(movie_url)
    return movie_urls

''' 获取并返回电影数据'''

def getMovieData(movieurl, cookie, userAgent, proxys):
    urls=movieurl.split("/")
    id=urls[-2]

    global x
    time.sleep(random.uniform(1.6, 2.1))
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN',
               'Connection': 'Keep-Alive',
               'Cookie': random.choice(cookie),
               'Host': 'movie.douban.com',
               'Referer': 'https://movie.douban.com/tag/',
               'User-Agent': random.choice(userAgent)}
    print(movieurl)
    movie_data={}
    movie_data["movname"] = '无'
    movie_data["soup_director"] = '无'
    movie_data["scen"] = '无'
    movie_data["actorname"]= '无'
    movie_data["leixing"] = '无'
    movie_data["soup_country"] = '无'
    movie_data["soup_language"] = '无'
    movie_data["showtime"] = '无'
    movie_data["runtime"] = '无'
    movie_data["people"] = 0
    movie_data["grade"] = 0
    try:
        x = x + 1
        session = requests.Session()
        html = session.get(movieurl, headers=headers, proxies=random.choice(proxys))
        obj_bs = BeautifulSoup(html.text, 'html.parser')


        # 获取电影名字

        soup_movname = obj_bs.find("span", {"property": "v:itemreviewed"})
        movname = soup_movname.get_text()
        movie_data["movname"]=movname
        print('电影名字：', movname)

        # 获取电影导演的名字


        soup_director = obj_bs.find("a", {"rel": "v:directedBy"})
        if soup_director:
            soup_director=soup_director.get_text()
            movie_data["soup_director"] = soup_director
            print('导演：' + soup_director)


        # 获取电影编剧名字
        try:
            soup_scenarist = list(obj_bs.findAll("span", {"class": "pl"})[1].next_siblings)[1:]
            for scenarist in soup_scenarist:
                scenarist_name = scenarist.select("a")
                scen = ''
                for bianju in scenarist_name:
                    scen = scen + bianju.get_text() + '/'
                movie_data["scen"] =scen
            print('编剧：' + scen)
        except:
            pass

        # 获取主演的名字
        # 将所有演员名字变成字符串，便于存储入数据库
        try:
            soup_actor = obj_bs.find("span", {"class": "actor"}).find("span", {"class": "attrs"}).findAll("a")
            actor_name = ''
            for actor in soup_actor:
                # print(actor.get_text())
                actor_name = actor_name + actor.get_text() + '/'
            movie_data["actor_name"] =actor_name
            print('主演：' + actor_name)
        except:
            pass

        # 获取电影类型
        try:
            soup_type = obj_bs.findAll("span", {"property": "v:genre"})
            leixing = ''
            for type_moive in soup_type:
                leixing = leixing + type_moive.get_text() + '/'
            movie_data["leixing"] =leixing
            print('类型：' + leixing)
        except:
            pass
        # 获取电影的制片国家
        # 这个比较有难度
        try:
            soup_country = list(obj_bs.findAll("span", {"class": "pl"})[4].next_siblings)[0]
            movie_data["soup_country"] =soup_country
            print('制片国家：' + soup_country)
        except:
            pass
        # 语言

        try:
            soup_language = list(obj_bs.findAll("span", {"class": "pl"})[5].next_siblings)[0]
            movie_data["soup_language"] =soup_language
            print('语言：' + soup_language)
        except:
            pass

        # 上映日期
        try:
            soup_showtime = obj_bs.find("span", {"property": "v:initialReleaseDate"})
            if soup_showtime:
                showtime = soup_showtime.get_text()
                movie_data["showtime"] = showtime
                print('上映日期：' + showtime)
        except:
            pass


        # 电影时长
        try:
            soup_runtime = obj_bs.find("span", {"property": "v:runtime"})
            if soup_runtime != None:
                runtime = soup_runtime.get_text()
                movie_data["runtime"] =runtime
                print("时长：" + runtime)
        except:
            pass
        # 电影的评价人数
        try:
            soup_people = obj_bs.find("span", {"property": "v:votes"})
            people = int(soup_people.get_text())
            movie_data["people"] =people
            print('评论人数：', people)
        except:
            pass

        # 豆瓣评分
        # float类型的grade表示分数

        soup_grade = obj_bs.find("strong", {"class": "ll rating_num"})
        grade = float(soup_grade.get_text())
        movie_data["grade"] =grade
        print('评分：', grade)

        return id,movie_data
    except:
        print('+++')

'''用以保存数据'''
def save_data(datas,file_path):

    if not (os.path.exists(file_path)):
        with open(file_path,"w") as f:
            json.dump(datas,f)

    else:
        with open(file_path, "rb+") as f:
            datas_json=json.dumps(datas)
            f.seek(0, 2)

            f.seek(f.tell()-1, 0)
            z=", "+datas_json[1:]
            f.write(z.encode("utf-8"))

x = 0
datas={}
start=500
end=1000
for i in range(start,end,20):
    for pakgeurl in getMoviePakge(i,i+20):
        for movieurl in getMovieUrls(pakgeurl, getCookie(), getUA(), proxypool(100)):
            id,data=getMovieData(movieurl, getCookie(), getUA(), proxypool(100))
            datas[id]=data
            print('=========================帅气的分隔符================================')
            print(x)
    save_data(datas, "movies.txt")
    with open("保存到哪一页啦！！.txt","a") as f:
        now = time.strftime('    %Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        f.write(str(i+20)+now)
        f.write("\n")



