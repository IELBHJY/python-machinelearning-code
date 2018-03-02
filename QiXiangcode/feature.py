#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 10:04:29 2018

@author: apple
"""
import pandas as pd
import os
data=[]
wind=['wind1','wind2','wind3','wind4','wind5','wind6','wind7','wind8','wind9','wind10']
left=['leftwind1','leftwind2','leftwind3','leftwind4','leftwind5','leftwind6','leftwind7','leftwind8','leftwind9','leftwind10']
right=['rightwind1','rightwind2','rightwind3','rightwind4','rightwind5','rightwind6','rightwind7','rightwind8','rightwind9','rightwind10']
up=['upwind1','upwind2','upwind3','upwind4','upwind5','upwind6','upwind7','upwind8','upwind9','upwind10']
down=['downwind1','downwind2','downwind3','downwind4','downwind5','downwind6','downwind7','downwind8','downwind9','downwind10']
def getMoreData(df):
    df[left]=df[wind]
    df[right]=df[wind]
    df[up]=df[wind]
    df[down]=df[wind]
    for i in df.index:
        x,y,h=df.loc[i,'xid'],df.loc[i,'yid'],df.loc[i,'hour']
        if(x in range(1,548)):
           temp=df[df.xid==x+1][df.yid==y][df.hour==h][wind]
        else:
           temp=df.loc[i,wind]
        df.loc[i,right]=temp
        if(x in range(2,549)):
           temp=df[df.xid==x-1][df.yid==y][df.hour==h][wind]
        else:
           temp=df.loc[i,wind]
        df.loc[i,left]=temp
        if(y in range(1,421)):
           temp=df[df.xid==x][df.yid==y+1][df.hour==h][wind]
        else:
           temp=df.loc[i,wind]
        df.loc[i,up]=temp
        if(y in range(2,422)):
           temp=df[df.xid==x-1][df.yid==y-1][df.hour==h][wind]
        else:
           temp=df.loc[i,wind]
        df.loc[i,down]=temp
        
    return df
for d in range(1,6):
  trainFile = "/Users/apple/Desktop/TianchiUAV/train20171205/trainday"+str(d)+"_winds.csv"
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
  df=getMoreData(df)
  data.append(df)
datas=pd.concat(data,ignore_index=True)
 
