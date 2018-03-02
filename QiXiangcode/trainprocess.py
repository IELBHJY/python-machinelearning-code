#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 11:09:46 2017

@author: apple
"""
import pandas as pd
import os
import random
'''
for i in range(4,11):
    trainFile="/Users/apple/Documents/data/train20171126/trainday1.csv"
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
    df=df[df.model==i]
    df.to_csv('/Users/apple/Documents/data/train20171126/day1/model'+str(i)+'.csv')
'''
#truedata=pd.read_csv('/Users/apple/Documents/data/In-situMeasurementforTraining_20171124.csv')
truedata=pd.read_csv('/Users/apple/Documents/data/Trueday3.csv')
model=pd.read_csv('/Users/apple/Desktop/TianchiUAV/train20171205/trainday3_windall.csv')
#model_avg=model_avg[['xid','yid','hour','wind_avg']]
model.drop(['xid','yid','date_id','hour'],1)
model['weightsum']=-1
w=[0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]
count1=0
count2=0
for i in range(0,len(model.wind1)):
    #for j in range(0,10):
        #model.iloc[i,13]+=w[j]*model.iloc[i,j]
    if model.iloc[i,10]>=14.5 and model.iloc[i,10]<=15.5:
        n=random.random()
        if n<0.5:
            model.iloc[i,10]=14.5
        else:
            model.iloc[i,10]=15.5
    if float(truedata.iloc[i,5])<15 and model.iloc[i,10]<15:
        count1+=1
    if float(truedata.iloc[i,5])>=15 and model.iloc[i,10]>=15:
        count2+=1
print((count1+count2)/len(model.wind1))
'''
count1=0
count2=0
for i in range(0,len(model.xid)):
    count=0
    for j in range(4,14):
        if float(model.iloc[i,j])<15:
            count=count+1
    if float(truedata.iloc[i,5])<15 and count>3:
        count1+=1
    if float(truedata.iloc[i,5])>=15 and count<=3:
        count2+=1
print((count1+count2)/len(model.xid))
'''
'''
0.9311847780648169
0.9416629101143725
0.9405785668464033
0.942231209051172
0.9396493017628825
0.9421173084591778
0.9316182264064435
0.9433988707225873
0.9380152015149501
0.9419937756818142
'''