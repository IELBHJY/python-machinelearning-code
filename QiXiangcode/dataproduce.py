#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 01:31:26 2018

@author: apple
"""
import pandas as pd
import numpy as np
import os
trainFile = '/Users/apple/Desktop/ForecastDataforTraining_201802.csv'
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
day1=df1[df1.date_id==1]
day1.to_csv('/Users/apple/Desktop/trainday1.csv',index=False)

day2=df1[df1.date_id==2]
day2.to_csv('/Users/apple/Desktop/trainday2.csv',index=False)

day3=df1[df1.date_id==3]
day3.to_csv('/Users/apple/Desktop/trainday3.csv',index=False)

day4=df1[df1.date_id==4]
day4.to_csv('/Users/apple/Desktop/trainday4.csv',index=False)

day5=df1[df1.date_id==5]
day5.to_csv('/Users/apple/Desktop/trainday5.csv',index=False)
