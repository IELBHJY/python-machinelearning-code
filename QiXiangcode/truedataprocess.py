#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 10:33:30 2017

@author: apple
"""
import pandas as pd
import numpy as np
import os
import csv
for date in range(5):
    file='testpre_date'+str(date+6)+'.csv'
    trainFile = 'H://算法//飞行器路线优化new//testdata//TestData01//TestData_pre'+'//'+file
    pwd = os.getcwd()
    os.chdir(os.path.dirname(trainFile))
    trainData = pd.read_csv(os.path.basename(trainFile),iterator=True)
    os.chdir(pwd)
    '''try:
        df = trainData.get_chunk(100000000)
        except StopIteration:
    print("Iteration is stopped.")'''
    loop = True
    chunkSize = 1000000
    chunks = []
    while loop:
        try:
            chunk = trainData.get_chunk(chunkSize)
            chunks.append(chunk)
        except StopIteration:
            loop = False
            print("Iteration is stopped.")
    dfpre = pd.concat(chunks, ignore_index=True)
    
    for h in range(18):
        dff=dfpre[dfpre.hour==h+3]
        wind=[[0]*421 for i in range(548)]
        for i in range(548):
            for j in range(421):
                wind[i][j]=dff.iloc[i*421+j,18]
        filename='testmaze_date'+str(date+1)+'_hour'+str(h+3)+'.csv'
        with open('H://算法//飞行器路线优化new//testdata//TestData01//TestData_pre//testmaze_pre'+'//'+filename,'w',newline='') as csvfile:
            writer=csv.writer(csvfile)
            writer.writerows(wind)
