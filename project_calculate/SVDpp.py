# -*- coding:utf-8 -*-"""@author:Levy@file:SVDpp.py@time:2017/12/2222:57"""
from math import *
import math
import random
import numpy as np
'''def LearningBiasLFM(train_ui,F,n,alpha,lamb,mu):
    [bu,bi,p,q,y]=InitLFM(train_ui,F)
    z=dict()
    for step in range(0,n):
        for u,items in train_ui.items():
            z[u]=p[u]
            ru=1/math.sqrt(1.0*len(items))
            for i ,rui in items.items():
                for  f in range(0,F):
                    z[u][f]+=y[i][f]*ru
            sum=[0 for i in range(0,F)]
            for i ,rui in items.items():
                pui=Predict()
                eui=rui-pui
                bu[u]+=alpha*(eui-lamb*bu[u])
                bi[i]+=alpha*(eui-lamb*bi[i])
                for k in range(0,F):
                    sum[k]+=q[i][k]*eui*ru
                    p[u][k]+=alpha*(q[i][k]*eui\
                                    -lamb*p[u][k])
                    q[i][k]+=alpha*((z[u][k]+p[u][k])*eui\
                                    -lamb*q[i][k])
                for i ,rui in items.items():
                    for f in range(0,F):
                        y[i][f]+=alpha*(sum[f]-lamb*y[i][f])
            alpha*=0.9
    return list(bu,bi,p,q,y)
'''

trains={}
trains[1,'b']=1 ;trains[1,'d']=3 ;trains[1,'f']=5
trains[2,'a']=4;trains[2,'c']=2;trains[2,'e']=3;trains[2,'g']=1
trains[3,'a']=2;trains[3,'c']=3;trains[3,'d']=5;trains[3,'e']=4
trains[4,'b']=4;trains[4,'c']=2;trains[4,'e']=3;trains[4,'g']=5
trains[5,'a']=5;trains[5,'c']=5;trains[5,'e']=5;trains[5,'g']=3
trains[6,'b']=4;trains[6,'c']=2;trains[6,'e']=3;trains[6,'f']=5
trains[7,'a']=2;trains[7,'b']=3;trains[7,'c']=4;trains[7,'e']=5;trains[7,'f']=3;
def BiasSVD(train,F,n,alpha,lamb,miu):
    bu,bi,p,q=InitLFM(train,F)
    for step in range(0,n):
        print(p)
        print(q)
        print(bu)
        print(bi)
        for (u,i),rui in train.items():

            pui=Predict(miu,bu,bi,p,q,u,i,F)
            print("第{}用户对{}电影的预测评价为{}，实际评价为{}".format(u, i, pui, rui))
            eui=rui-pui
            bu[u]+=alpha*(eui-lamb*bu[u])
            bi[i]+=alpha*(eui-lamb*bi[i])
            for f in range(0,F):
                ps=p[u][f]
                qs=q[i][f]
                p[u][f]+=alpha*(qs*eui-lamb*ps)
                q[i][f]+=alpha*(ps*eui-lamb*qs)
        alpha*=0.9
        rmse = cal_rmse(train, bu, bi, p, q, F, lamb)
        print("第{}次迭代的误差为{}".format(step, rmse))

    return (bu,bi,p,q)

def SVDpp(train,F,n,alpha,lamb,miu):
    bu,bi,p,q=InitLFM(train,F)
    for step in range(0,n):
        print(p)
        print(q)
        print(bu)
        print(bi)
        for (u,i),rui in train.items():

            pui=Predict(miu,bu,bi,p,q,u,i,F)
            print("第{}用户对{}电影的预测评价为{}，实际评价为{}".format(u, i, pui, rui))
            eui=pui-rui
            bu[u]+=alpha*(eui-lamb*bu[u])
            bi[i]+=alpha*(eui-lamb*bi[i])
            for f in range(0,F):
                p[u][f]+=alpha*(q[i][f]*eui-lamb*p[u][f])
                q[i][f]+=alpha*(p[u][f]*eui-lamb*q[i][f])
        alpha*=0.9
        rmse = cal_rmse(train, bu, bi, p, q, F, lamb)
        print("第{}词迭代的误差为{}".format(step, rmse))

    return (bu,bi,p,q)

def InitLFM(train ,F):
    p=dict()
    q=dict()
    bu=dict()
    bi=dict()
    for (u,i),rui in train.items():
        bu[u]=0
        bi[i]=0
        if u not in p:
            p[u]=[random.random()/math.sqrt(F) for i in range(0,F)]
        if i not in q:
            q[i]=[random.random()/math.sqrt(F) for i in range(0,F)]

    return [bu,bi,p,q]

def cal_rmse(train,bu,bi,p,q,F,lamb):
    sum=0
    for (u,i),rui in train.items():
        sum+=(Predict(miu,bu,bi,p,q,u,i,F)-rui)**2
    for u in p:
        sum+=lamb*l2(p[u])
    for i in q:
        sum+=lamb*l2(q[i])
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



def Predict(miu,bu,bi,p,q,u,i,F):
    rui=miu+bu[u]+bi[i]
    for f in range(0,F):
        rui+=p[u][f]*q[i][f]
    return rui

train={}
train[1,'a']=4
train[1,'b']=5
train[2,'a']=3
train[2,'c']=4
train[2,'d']=4
train[3,'a']=2
train[3,'b']=5
train[3,'c']=5
train[4,'b']=3
train[4,'c']=2
train[4,'d']=5
miu=42/11
miu2=96/28
F=3
bu,bi,p,q=BiasSVD(trains,F,100,0.25,0.05,miu2)
print(p)
for (u,i),rui in trains.items():
    pui=Predict(miu,bu,bi,p,q,u,i,F)
    print("第{}用户对{}电影的预测评价为{}，实际评价为{}".format(u,i,pui,rui))
