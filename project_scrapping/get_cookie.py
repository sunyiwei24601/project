# -*- coding:utf-8 -*-"""@author:Levy@file:get_cookie.py@time:2017/12/1420:51"""
def get_cookie_from_network():
    from selenium import webdriver
    url_login = 'http://login.weibo.cn/login/'
    driver = webdriver.PhantomJS()
    driver.get(url_login)
    driver.find_element_by_xpath('//input[@type="text"]').send_keys('your_weibo_accout') # 改成你的微博账号
    driver.find_element_by_xpath('//input[@type="password"]').send_keys('your_weibo_password') # 改成你的微博密码

    driver.find_element_by_xpath('//input[@type="submit"]').click() # 点击登录

    # 获得 cookie信息
    cookie_list = driver.get_cookies()
    print (cookie_list)

get_cookie_from_network()