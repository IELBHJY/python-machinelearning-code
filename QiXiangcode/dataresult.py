#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 23:55:45 2017

@author: apple
"""
import pandas as pd
df=pd.read_csv('/Users/apple/Desktop/result0205/10/1.csv',header=None)
for i in [2,3,4,5,6,7,8,9,10]:
    df1=pd.read_csv('/Users/apple/Desktop/result0205/10/'+str(i)+'.csv',header=None)
    df=pd.concat([df,df1],ignore_index=True)
df.to_csv('/Users/apple/Desktop/result0205/result5.csv',index=False,header=None)

df1=pd.read_csv('/Users/apple/Desktop/result0205/result1.csv',header=None)
df2=pd.read_csv('/Users/apple/Desktop/result0205/result2.csv',header=None)
df3=pd.read_csv('/Users/apple/Desktop/result0205/result3.csv',header=None)
df4=pd.read_csv('/Users/apple/Desktop/result0205/result4.csv',header=None)
df5=pd.read_csv('/Users/apple/Desktop/result0205/result5.csv',header=None)
df=pd.concat([df1,df2,df3,df4,df5],ignore_index=True)
df.to_csv('/Users/apple/Desktop/result0205/result.csv',index=False,header=None)
'''
for i in range(1,11):
    df=pd.read_csv('/Users/apple/Desktop/8/'+str(i)+'.csv',header=None)
    df.iloc[0,3]=142
    df.iloc[0,4]=328
    df.to_csv('/Users/apple/Desktop/8/'+str(i)+'.csv',header=None,index=False)
'''