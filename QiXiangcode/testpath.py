#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 20:00:49 2017

@author: apple
"""

import pandas as pd
'''
df=[]
for i in [2]:
    df1=pd.read_csv('/Users/apple/Desktop/1/'+str(i)+'.csv',header=None)
    df.append(df1)
df1=pd.concat(df,ignore_index=True)
#df2=pd.read_csv('/Users/apple/Desktop/day6_city3.csv',header=None)
ds=[]
for i in [2]:
    df2=pd.read_csv('/Users/apple/Desktop/6/'+str(i)+'.csv',header=None)
    ds.append(df2)
df2=pd.concat(ds,ignore_index=True)
for i in range(0,len(df1.index)-1):
    if df1.iloc[i,3]!=df2.iloc[i,3] or df1.iloc[i,4]!=df2.iloc[i,4]:
        print("路径不相同")
    
count=0
df1=pd.read_csv('/Users/apple/Desktop/1/3.csv',header=None)
for i in range(len(df1.index)-1):
    if df1.iloc[i,3]==df1.iloc[i+1,3] and df1.iloc[i,4]==df1.iloc[i+1,4]:
        #print("停留")
        count+=1
print(count)
'''
df=pd.read_csv('/Users/apple/Desktop/8/5.csv',header=None)
weather3=pd.read_csv('/Users/apple/Desktop/test20171218_pro_15/Testday8_hour3.csv',header=None)
weather4=pd.read_csv('/Users/apple/Desktop/test20171218_pro_15/Testday8_hour4.csv',header=None)
weather5=pd.read_csv('/Users/apple/Desktop/test20171218_pro_15/Testday8_hour5.csv',header=None)
weather6=pd.read_csv('/Users/apple/Desktop/test20171218_pro_15/Testday8_hour6.csv',header=None)
weather7=pd.read_csv('/Users/apple/Desktop/test20171218_pro_15/Testday8_hour7.csv',header=None)
weather8=pd.read_csv('/Users/apple/Desktop/test20171218_pro_15/Testday8_hour8.csv',header=None)
weather9=pd.read_csv('/Users/apple/Desktop/test20171218_pro_15/Testday8_hour9.csv',header=None)
weather10=pd.read_csv('/Users/apple/Desktop/test20171218_pro_15/Testday8_hour10.csv',header=None)
weather11=pd.read_csv('/Users/apple/Desktop/test20171218_pro_15/Testday8_hour11.csv',header=None)
count=0
for i in range(len(df.index)-1):
    x=df.iloc[i,3]
    y=df.iloc[i,4]
    if i<30:
        weather=weather3.iloc[x-1,y-1]
    elif i<60:
        weather=weather4.iloc[x-1,y-1]
    elif i<90:
        weather=weather5.iloc[x-1,y-1]
    elif i<120:
        weather=weather6.iloc[x-1,y-1]
    elif i<150:
        weather=weather7.iloc[x-1,y-1]
    elif i<180:
        weather=weather8.iloc[x-1,y-1]
    elif i<210:
        weather=weather9.iloc[x-1,y-1]
    elif i<240:
        weather=weather10.iloc[x-1,y-1]
    elif i<270:
        weather=weather11.iloc[x-1,y-1]
    #print(weather*15)
    if weather*15>=14:
        count+=1
print(count/len(df.index))
