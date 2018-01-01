# -*- coding:utf-8 -*-"""@author:Levy@file:chapter9.py@time:2017/12/170:45"""
import requests
params={"form_email":'18930721408','form_password':'19283746'}
session=requests.session()
s = session.post("https://accounts.douban.com/login", params)
print("Cookie is set to:")
print()
print(s.cookies.get_dict())
print("-----------")
print("Going to profile page...")
r=session.get("https://movie.douban.com/subject/1292052/collections")
print(r.text)