#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 07:49:22 2018

@author: apple
"""
import pandas as pd
data=pd.read_csv('/Users/apple/Desktop/test20180206.csv',header=None)
data.columns=['city','day','hour','xid','yid']
data7=data[data.day==7]
data9=data[data.day==9]
data10=data[data.day==10]
data7.to_csv('/Users/apple/Desktop/data7.csv',header=None,index=False)
data9.to_csv('/Users/apple/Desktop/data9.csv',header=None,index=False)
data10.to_csv('/Users/apple/Desktop/data10.csv',header=None,index=False)


data6=pd.read_csv('/Users/apple/Desktop/data6.csv',header=None)
data7=pd.read_csv('/Users/apple/Desktop/data7.csv',header=None)
data8=pd.read_csv('/Users/apple/Desktop/data8.csv',header=None)
data9=pd.read_csv('/Users/apple/Desktop/data9.csv',header=None)
data10=pd.read_csv('/Users/apple/Desktop/data10.csv',header=None)
result=pd.concat([data6,data7,data8,data9,data10],ignore_index=True)
result.to_csv('/Users/apple/Desktop/GA20180209.csv',header=None,index=False)


data1=pd.read_csv('/Users/apple/Desktop/result0208/8.csv')
path=pd.read_csv('/Users/apple/Desktop/routes1_multi/8.csv')
paths=[]
for i in data1.index:
    p=path[path.start_time==data1.loc[i,'flyTime']][path['0']==data1.loc[i,'city']+1]
    paths.append(p)
data6=pd.concat(paths,ignore_index=True)
data6=data6[['0','date_id','hour','x','y']]
data6.to_csv('/Users/apple/Desktop/data8.csv',header=None,index=False)


import pandas as pd
test=pd.read_csv('/Users/apple/Desktop/routes1_multi/7_risk.csv')
test=test[test['0']==10][test['1']==383]
print(test['2'])
    




