# -*- coding:utf-8 -*-"""@author:Levy@file:k_means.py@time:2017/12/1815:50"""
import pandas as pd
from sklearn.cluster import KMeans
import csv
import numpy as np
inputfile="normalized_data.xls"
data=pd.read_excel(inputfile)
kmodel=KMeans(n_clusters=4,n_jobs=1)
kmodel.fit(data)

np.savetxt("cluster5_labels.csv",kmodel.labels_)
print(kmodel.cluster_centers_)