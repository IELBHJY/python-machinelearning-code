#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 09:48:06 2017

@author: apple
"""
import pandas as pd
#import numpy as np
import os
#trainFile = "/Users/apple/Documents/data/ForecastDataforTesting_20171124.csv"
trainFile = "/Users/apple/Desktop/TianchiUAV/In_situMeasurementforTraining_201712.csv"

#for k in range(7,11):
  #trainFile="/Users/apple/Documents/data/test20171124/testday"+str(k)+".csv"
pwd = os.getcwd()
os.chdir(os.path.dirname(trainFile))
trainData = pd.read_csv(os.path.basename(trainFile),iterator=True)
os.chdir(pwd)
loop = True
chunkSize = 200000
chunks = []
while loop:
  try:
     chunk = trainData.get_chunk(chunkSize)
     chunks.append(chunk)
  except StopIteration:
     loop = False
     print("Iteration is stopped.")
df = pd.concat(chunks, ignore_index=True)
df1=df[df.date_id==1]
df1.to_csv('/Users/apple/Documents/data/Trueday1.csv')
df2=df[df.date_id==2]
df2.to_csv('/Users/apple/Documents/data/Trueday2.csv')
df3=df[df.date_id==3]
df3.to_csv('/Users/apple/Documents/data/Trueday3.csv')
df4=df[df.date_id==4]
df4.to_csv('/Users/apple/Documents/data/Trueday4.csv')
df5=df[df.date_id==5]
df5.to_csv('/Users/apple/Documents/data/Trueday5.csv')
'''
#df=pd.read_csv("/Users/apple/Documents/data/testday10/model1.csv")
#print("数据读完")
  df=df[df.model==1]
  for i in range(3,21):
    df1=df[df['hour']==i]
    df_con=pd.DataFrame(np.random.randn(548,421))
    print("Hour:"+str(i))
    for j in range(1,549):
        df2=df1[df1['xid']==j]
        for k in range(1,422):  
          df3=df2[df2['yid']==k]
          if float(df3['wind'])<20:
              df_con.iloc[j-1,k-1]=1
          else:
              df_con.iloc[j-1,k-1]=-1
    df_con.to_csv("/Users/apple/Documents/data/test20171124/model1/model1_day"+str(k)+"_hour"+str(i)+".csv",index=False,header=False)
     
'''
'''
try:
    df = trainData.get_chunk(100000000)
except StopIteration:
    print("Iteration is stopped.")
'''
'''
df=pd.read_csv('/Users/apple/Documents/data/testday10.csv')
for i in range(1,11):
    df1=df[df['realization']==i]
    df1=df1[df1['hour']>=9]
    df1=df1[df1['hour']<=21]
    df1.to_csv("/Users/apple/Documents/data/testday10/model"+str(i)+".csv",index=False)
'''
'''
df1=df[df['date_id']==6]
df2=df[df['date_id']==7]
df3=df[df['date_id']==8]
df4=df[df['date_id']==9]
df5=df[df['date_id']==10]
df1.to_csv('/Users/apple/Documents/data/test20171205/testday6.csv')
df2.to_csv('/Users/apple/Documents/data/test20171205/testday7.csv')
df3.to_csv('/Users/apple/Documents/data/test20171205/testday8.csv')
df4.to_csv('/Users/apple/Documents/data/test20171205/testday9.csv')
df5.to_csv('/Users/apple/Documents/data/test20171205/testday10.csv')
'''
'''
list=[]
for i in df['date_id']:
    if i not in list:
        list.append(i)
'''







