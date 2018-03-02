# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 14:46:28 2017

@author: DELL
"""
import pandas as pd
import os
import csv
#trainFile='/Users/apple/Desktop/TianchiUAV/Truedata/Trueday2.csv'
trainFile='/Users/apple/Desktop/qixiangshuju/testday10_all.csv'
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
for h in range(18):
        dff=df[df.hour==h+3]
        wind=[[0]*421 for i in range(548)]
        for i in range(548):
            for j in range(421):
                wind[i][j]=float(dff.iloc[i*421+j,25])
                
        filename='Testday'+str(10)+'_hour'+str(h+3)+'.csv'
        with open('/Users/apple/Desktop/20180205rainfall/'+filename,'w',newline='') as csvfile:
            writer=csv.writer(csvfile)
            writer.writerows(wind)