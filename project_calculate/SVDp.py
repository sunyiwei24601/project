# -*- coding:utf-8 -*-"""@author:Levy@file:SVDp.py@time:2017/12/2310:21"""
from math import *
import math
import random
import numpy as np

trains={}
trains[1]={"b":1,"d":3,"f":5}
trains[2]={"a":4,"c":2,"e":3,"g":1}
trains[3]={"a":2,"c":3,"d":5,"e":4}
trains[4]={"b":4,"c":2,"e":3,"g":5}
trains[5]={"a":5,"c":5,"e":5,"g":3}
trains[6]={"b":4,"c":2,"e":3,"f":5}
trains[7]={"a":2,"b":3,"c":4,"e":5,"f":3}


def LearningBiasLFM(train_ui,F,n,alpha,lamb,lamb2,miu):
    [bu,bi,p,q,y]=InitLFM(train_ui,F)
    z=dict()
    prermse=10000000
    for step in range(0,n):
        for u,items in train_ui.items():
            z[u]=p[u]
            ru=1/math.sqrt(1.0*len(items))
            for i,rui in items.items():
                for  f in range(0,F):
                    z[u][f]+=y[i][f]*ru
            sum=[0 for i in range(0,F)]
            for i ,rui in items.items():
                pui=Predict(train_ui,miu,bu,bi,p,q,u,i,F,y)
                print("第{}用户对{}电影的预测评价为{}，实际评价为{}".format(u, i, pui, rui))
                eui=rui-pui
                print("eui差值为{}".format(eui))
                bu[u]+=alpha*(eui-lamb*bu[u])
                bi[i]+=alpha*(eui-lamb*bi[i])
                #print("先前的p[u][k]为{}".format(p[u]))
                #print("先前的q[i][k]为{}".format(q[i]))
                for k in range(0,F):
                    sum[k]+=q[i][k]*eui*ru
                    p[u][k]+=alpha*(q[i][k]*eui-lamb2*p[u][k])
                    q[i][k]+=alpha*((z[u][k])*eui-lamb2*q[i][k])
                #print("后来的p[u][k]为{}".format(p[u]))
                #print("后来的q[i][k]为{}".format(q[i]))
            for i ,rui in items.items():
                for f in range(0,F):
                    y[i][f]+=alpha*(sum[f]-lamb2*y[i][f])
                print(y[i])
            alpha*=0.9
            print("alpha为{}".format(alpha))
        rmse=cal_rmse(train_ui,bu,bi,p,q,F,lamb,miu,y)
        print("——————————***********————————————")
       #if(rmse>prermse):break
        #else:prermse=rmse
        print("第{}词迭代的误差为{}".format(step, rmse))
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

train={}
train[1]={"a":4,'b':5}
train[2]={'a':3,'c':4,'d':4}
train[3]={"a":2,"b":5,"c":5}
train[4]={'b':3,'c':2,"d":5}
miu2=96/28
LearningBiasLFM(trains,3,20,0.1,0.01,1,miu2)


