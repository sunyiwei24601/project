# -*- coding:utf-8 -*-"""@author:Levy@file:normalize.py@time:2017/12/1815:36"""
import pandas as pd
datafile=r"C:\Users\Administrator\Desktop\原始4属性数据.xls"
normalized_data="normalized_data.xls"

data=pd.read_excel(datafile)
data=(data-data.mean(axis=0))/(data.std(axis=0))

data.to_excel(normalized_data,index=False)
