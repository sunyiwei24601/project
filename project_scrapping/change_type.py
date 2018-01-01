# -*- coding:utf-8 -*-"""@author:Levy@file:change_type.py@time:2017/12/2514:08"""
import json
filename="user_details1-500.txt"
with open(filename) as  f:
    details=json.load(f)
data=dict()
for item in details:
    data[item["id"]]=dict()
    rates=item["rates"]
    for i in rates:
        if(i[1][0]=="rating4-t"):
            rate=4
        elif (i[1][0] == "rating5-t"):
            rate = 5
        elif (i[1][0] == "rating3-t"):
            rate = 3
        elif (i[1][0] == "rating2-t"):
            rate =2
        elif (i[1][0] == "rating1-t"):
            rate = 1
        else:
            continue
        data[item["id"]][i[0]]=rate

with open("processed_data1-500.txt","w") as f:
    json.dump(data,f)
