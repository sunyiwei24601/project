# -*- coding:utf-8 -*-"""@author:Levy@file:douban_login.py@time:2017/12/1718:06"""
cookies='"ll"="108296";bid	=imGZGDnver8;__utma	=223695111.1713362382.1513529870.1513529870.1513529870.1;__utmb	=223695111.0.10.1513529870;__utmc	=223695111;__utmz	=223695111.1513529870.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/;__utmt	=1;_pk_ref.100001.4cf6=	["","",1513529870,"https://www.douban.com/"];_pk_id.100001.4cf6=	0b84cb941b456850.1513529870.1.1513529985.1513529870.;_pk_ses.100001.4cf6=	*;ps=	y;dbcl2=	"146518831:N14+Zc7zJ5M";ck=	b6eO;push_noty_num=	0;push_doumail_num=	0;ap=	1;_vwo_uuid_v2=	FCD01F65BAFB3827290038ECE855618B|5213d0236b27c6866fd50b81997c0c13;'

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, br',
           'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
           'Connection': 'keep-alive',
           'Cookie': cookies,
            'Host': 'movie.douban.com',
           'Origin': 'https://movie.douban.com',
           'Referer': "https://movie.douban.com/subject/1292720/collections",
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:57.0) Gecko/20100101 Firefox/57.0'
           }
headers2={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, br',
           'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
           'Referer': "https://www.douban.com/accounts/login",
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:57.0) Gecko/20100101 Firefox/57.0'
           }
import requests
params={"form_email":'18930721408',
        'form_password':'19283746',
        'redir':"https://movie.douban.com/subject/1292052/collections",
        'login':'登录'}
url="https://www.douban.com/accounts/login"
r=requests.post(url,params=params,headers=headers2)
print(r.text)