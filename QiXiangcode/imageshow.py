#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 20:19:35 2017

@author: apple
"""
import pylab as plt
import numpy as np
import numpy as np
import pandas as pd
import os
import matplotlib
import matplotlib.cm as cm
from matplotlib.colors import LogNorm
from matplotlib.colors import Normalize

#trainFile = "/Users/apple/Desktop/In-situMeasurementforTraining_20171124.csv"
trainFile="/Users/apple/Desktop/TianchiUAV/Truedata/Trueday3.csv"
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
df1 = pd.concat(chunks, ignore_index=True)
df1=df1[df1.hour==3]
df1.index=range(230708)
df=pd.read_csv('/Users/apple/Desktop/TianchiUAV/train20171205/trainday3_windall.csv')
df=df[df.hour==3]
df.index=range(230708)
x,y,z = df['xid'].values,df['yid'].values,df['wind1'].values
for i in df.index:
    if float(df.loc[i,'wind6'])<15 and float(df1.loc[i,'wind'])<15:
        z[i]=30
    elif float(df.loc[i,'wind6'])>=15 and float(df1.loc[i,'wind'])>=15:
        z[i]=30
    else:
        z[i]=0
N = int(len(z)**.5)
z = z.reshape(548, 421)
fig=plt.figure(figsize=(10,8))
titles='Truedata'
plt.title(titles)
filename='True_date1_hour3_wind2.jpg'
plt.savefig('/Users/apple/Desktop/picture'+filename)
plt.imshow(z, extent=(np.amin(x), np.amax(x), np.amin(y), np.amax(y)),
        cmap=cm.jet , aspect='auto',vmin=0,vmax=30)
plt.colorbar()
#filename='True_date1_hour3.jpg'
#plt.savefig('/Users/apple/Desktop/picture/'+filename)
plt.show()
