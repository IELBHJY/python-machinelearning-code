#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 09:10:56 2018

@author: apple
"""
import pandas as pd
#import numpy as np
import os
#trainFile = "/Users/apple/Desktop/TianchiUAV/In_situMeasurementforTraining_201712.csv"
truedata=pd.read_csv("/Users/apple/Desktop/TianchiUAV/In_situMeasurementforTraining_201712.csv")
for d in range(1,6):
  #truedata=pd.read_csv("/Users/apple/Desktop/TianchiUAV/In_situMeasurementforTraining_201712.csv")
     truedata=truedata[truedata['date_id']==d]
     trainFile="/Users/apple/Desktop/TianchiUAV/train20171205/trainday"+str(d)+"_windall.csv"
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
     df['windtrue']=truedata['wind']
     df.to_csv("/Users/apple/Desktop/TianchiUAV/train20171205/trainday"+str(d)+"_winds.csv",index=False)
     
     
     
     
     
     