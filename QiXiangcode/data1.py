#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 12:33:25 2018

@author: apple
"""
import pandas as pd
import csv
df=pd.read_csv('/Users/apple/Desktop/regression_rmse_21041_15/In-situMeasurementforTraining_date10.csv',header=None)
df.columns=['xid','yid','hour']
for h in range(18):
        dff=df[df.hour==h+3]
        dff.index=range(len(dff))
        wind=[[0]*421 for i in range(548)]
        for j in dff.index:
           x=dff.iloc[j,0]-1
           y=dff.iloc[j,1]-1
           wind[x][y]=1
        '''
        for i in range(548):
            for j in range(421):
                wind[i][j]=float(dff.iloc[i*421+j,14])/15
        '''
        filename='Testday'+str(10)+'_hour'+str(h+3)+'.csv'
        with open('/Users/apple/Desktop/20180118/'+filename,'w',newline='') as csvfile:
            writer=csv.writer(csvfile)
            writer.writerows(wind)