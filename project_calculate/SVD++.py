# -*- coding:utf-8 -*-"""@author:Levy@file:SVDp.py@time:2017/12/2310:21"""
from math import *
import math
import random
import numpy as np
import json

trains={}
trains[1]={"b":1,"d":3,"f":5}
trains[2]={"a":4,"c":2,"e":3,"g":1}
trains[3]={"a":2,"c":3,"d":5,"e":4}
trains[4]={"b":4,"c":2,"e":3,"g":5}
trains[5]={"a":5,"c":5,"e":5,"g":3}
trains[6]={"b":4,"c":2,"e":3,"f":5}
trains[7]={"a":2,"b":3,"c":4,"e":5,"f":3}


def LearningBiasLFM(train_ui,F,n,alpha,lamb,miu):
    [bu,bi,p,q,y]=InitLFM(train_ui,F)
    z=dict()
    prermse=10000000
    for step in range(0,n):
        for u,items in train_ui.items():

            for i ,rui in items.items():
                ru = 1 / math.sqrt(1.0 * len(items))

                pui=Predict(train_ui,miu,bu,bi,p,q,u,i,F,y)

                eui=rui-pui


                z[u] = [0 for i in range(0, F)]

                for it, rui in items.items():

                    for f in range(0, F):
                        z[u][f] += y[it][f] * ru

                #print("z[u]:{}".format(z[u]))
                bu[u]+=alpha*(eui-lamb*bu[u])
                bi[i]+=alpha*(eui-lamb*bi[i])
                #print("先前的p[u][k]为{}".format(p[u]))
                #print("先前的q[i][k]为{}".format(q[i]))
                for k in range(0,F):
                    p[u][k]+=alpha*(q[i][k]*eui-lamb*p[u][k])


                for k in range(0, F):
                    q[i][k]+=alpha*((p[u][k]+z[u][k])*eui-lamb*q[i][k])
                #print("后来的p[u][k]为{}".format(p[u]))
                #print("后来的q[i][k]为{}".format(q[i]))


                for it in items:
                    sum = [0 for i in range(0, F)]
                    for k in range(0, F):
                        sum[k] += q[it][k] * eui * ru
                    for f in range(0,F):
                        y[it][f]+=alpha*(sum[f]-lamb*y[it][f])

            print("第{}用户对{}电影的预测评价为{}，实际评价为{}".format(u, i, pui, rui))


        rmse=cal_rmse(train_ui,bu,bi,p,q,F,lamb,miu,y)
        print("——————————————************************——————————————————")
       #if(rmse>prermse):break
        #else:prermse=rmse
        print("第{}次迭代的误差为{}".format(step, rmse))
    return (bu,bi,p,q,y)

def InitLFM(train ,F):
    p=dict()
    q=dict()
    bu=dict()
    bi=dict()
    y=dict()
    for u,items in train.items():
        bu[u]=0
        for i,rui in items.items():
            if i not in bi:
                bi[i]=0
            if u not in p:
                p[u]=[random.random()/math.sqrt(F) for i in range(0,F)]
            if i not in q:
                q[i]=[random.random()/math.sqrt(F) for i in range(0,F)]
            if i not in y:
                y[i]=[random.random()/math.sqrt(F) for i in range(0,F)]

    return [bu,bi,p,q,y]

def cal_rmse(train,bu,bi,p,q,F,lamb,miu,y):
    sum=0
    for u,item in train.items():
        for i,rui in item.items():
            sum+=(Predict(train,miu,bu,bi,p,q,u,i,F,y)-rui)**2

    for u in p:
        sum+=lamb*l2(p[u])
    for i in q:
        sum+=lamb*l2(q[i])
    for u,item in y.items():
        sum+=l2(item)

    for i in bi.values():
        sum+=i**2
    for i in bu.values():
        sum+=i**2

    return sum

def l2(list):
    sum=0
    for i in list:
        sum+=i**2
    return sum

def Predict(train,miu,bu,bi,p,q,u,i,F,y):
    rui=miu+bu[u]+bi[i]
    nu=train[u].keys()
    sum=[0 for i in range(0,F)]
    for j in nu:
        for f in range(0,F):
            sum[f]+=y[j][f]
    for f in range(0,F):
        sum[f]=sum[f]/math.sqrt(len(nu))

    for f in range(0,F):
        rui+=(p[u][f]+sum[f])*q[i][f]
    return rui
def cal_miu(data):
    n=0
    sum=0
    for u,item in data.items():
        for i ,rui in item.items():
            sum+=rui
            n+=1
    return sum/n

train3={}
train3[1]={"a":4,'b':5}
train3[2]={'a':3,'c':4,'d':4}
train3[3]={"a":2,"b":5,"c":5}
train3[4]={'b':3,'c':2,"d":5}
miu2=96/28
miu=42/11
filename="F:\python_project\project_scrapping\processed_data1-500.txt"
with open(filename) as f:
    data=json.load(f)


train_dual=dict()
for  u,item  in data.items():
    for i ,rui in item.items():
        if(train_dual.get(i)):
            train_dual[i][u]=rui
        else:
            train_dual[i]=dict()
            train_dual[i][u]=rui
LearningBiasLFM(train_dual,20,50,0.01,0.002,cal_miu(data))