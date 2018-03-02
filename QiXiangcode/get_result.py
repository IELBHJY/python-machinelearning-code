#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 20:40:20 2017

@author: apple
"""
import pandas as pd
df=pd.read_csv('/Users/apple/Desktop/tmp.csv',header=None)
df.columns=['city','day','time','xid','yid']
for day in [6,7,8,9,10]:
    for city in range(1,11):
        result=df[df.day==day][df.city==city]
        result.to_csv('/Users/apple/Desktop/reai/'+str(day)+'/'+str(city)+'.csv',header=None,index=False)