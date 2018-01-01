# -*- coding:utf-8 -*-"""@author:Levy@file:test_proxy.py@time:2017/12/2517:32"""
import os
import requests
def test_proxy():
    N = 1

    url = 'https://www.baidu.com'
    fp = open('host.txt', 'r')
    ips = fp.readlines()
    proxys = list()
    for p in ips:
        ip = p.strip('\n').split('\t')
        proxy = 'http:\\' + ip[0] + ':' + ip[1]
        proxies = {'proxy': proxy}
        proxys.append(proxies)
    for pro in proxys:
        try:
            s = requests.get(url, proxies=pro)
            print('第{}个ip：{} 状态{}'.format(N,pro,s.status_code))
        except Exception as e:
            print(e)
        N+=1

test_proxy()