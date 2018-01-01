# -*- coding:utf-8 -*-"""@author:Levy@file:request_download.py@time:2017/12/151:56"""
import requests
def  download(url):
    r=requests.get(url)
    return r.content.decode("utf-8")

