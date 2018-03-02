# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 12:23:10 2017

@author: GeLiang
"""
import pandas as pd
import numpy as np
import os
#trainFile = "H:\算法\飞行器路线优化\ForecastDataforTraining\ForecastDataforTraining.csv"
trainFile = '/Users/apple/Desktop/trainday/trainday5.csv'
#trainFile='/Users/apple/Desktop/TianchiUAV/test20171205/test6_windall.csv'
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
#df1.columns=['xid','yid','date_id','hour','model','wind']
df1_model1=df1[df1.model==1]
df1_model2=df1[df1.model==2]
df1_model3=df1[df1.model==3]
df1_model4=df1[df1.model==4]
df1_model5=df1[df1.model==5]
df1_model6=df1[df1.model==6]
df1_model7=df1[df1.model==7]
df1_model8=df1[df1.model==8]
df1_model9=df1[df1.model==9]
df1_model10=df1[df1.model==10]
df1_model=df1_model1.drop('model',axis=1)
df1_model.columns=['xid','yid','date_id','hour','wind1','rainfall1']
sort_df1_model=df1_model.sort_values(by=['hour','xid','yid'],axis=0,ascending=True)
sort_df1_model2=df1_model2.sort_values(by=['hour','xid','yid'],axis=0,ascending=True)
sort_df1_model3=df1_model3.sort_values(by=['hour','xid','yid'],axis=0,ascending=True)
sort_df1_model4=df1_model4.sort_values(by=['hour','xid','yid'],axis=0,ascending=True)
sort_df1_model5=df1_model5.sort_values(by=['hour','xid','yid'],axis=0,ascending=True)
sort_df1_model6=df1_model6.sort_values(by=['hour','xid','yid'],axis=0,ascending=True)
sort_df1_model7=df1_model7.sort_values(by=['hour','xid','yid'],axis=0,ascending=True)
sort_df1_model8=df1_model8.sort_values(by=['hour','xid','yid'],axis=0,ascending=True)
sort_df1_model9=df1_model9.sort_values(by=['hour','xid','yid'],axis=0,ascending=True)
sort_df1_model10=df1_model10.sort_values(by=['hour','xid','yid'],axis=0,ascending=True)
sort_df1_model.insert(6,'wind2',sort_df1_model2['wind'].values)
sort_df1_model.insert(7,'wind3',sort_df1_model3['wind'].values)
sort_df1_model.insert(8,'wind4',sort_df1_model4['wind'].values)
sort_df1_model.insert(9,'wind5',sort_df1_model5['wind'].values)
sort_df1_model.insert(10,'wind6',sort_df1_model6['wind'].values)
sort_df1_model.insert(11,'wind7',sort_df1_model7['wind'].values)
sort_df1_model.insert(12,'wind8',sort_df1_model8['wind'].values)
sort_df1_model.insert(13,'wind9',sort_df1_model9['wind'].values)
sort_df1_model.insert(14,'wind10',sort_df1_model10['wind'].values)
#----------------------------------------------------
sort_df1_model.insert(15,'rainfall2',sort_df1_model2['rainfall'].values)
sort_df1_model.insert(16,'rainfall3',sort_df1_model3['rainfall'].values)
sort_df1_model.insert(17,'rainfall4',sort_df1_model4['rainfall'].values)
sort_df1_model.insert(18,'rainfall5',sort_df1_model5['rainfall'].values)
sort_df1_model.insert(19,'rainfall6',sort_df1_model6['rainfall'].values)
sort_df1_model.insert(20,'rainfall7',sort_df1_model7['rainfall'].values)
sort_df1_model.insert(21,'rainfall8',sort_df1_model8['rainfall'].values)
sort_df1_model.insert(22,'rainfall9',sort_df1_model9['rainfall'].values)
sort_df1_model.insert(23,'rainfall10',sort_df1_model10['rainfall'].values)
#aver=(sort_df1_model['wind'].values+sort_df1_model2['wind'].values+sort_df1_model3['wind'].values+sort_df1_model4['wind'].values+sort_df1_model5['wind'].values+sort_df1_model6['wind'].values+sort_df1_model7['wind'].values+sort_df1_model8['wind'].values+sort_df1_model9['wind'].values+sort_df1_model10['wind'].values)/10
aver=(sort_df1_model['wind1'].values+sort_df1_model2['wind'].values+sort_df1_model3['wind'].values+sort_df1_model4['wind'].values+sort_df1_model5['wind'].values+sort_df1_model6['wind'].values+sort_df1_model7['wind'].values+sort_df1_model8['wind'].values+sort_df1_model9['wind'].values+sort_df1_model10['wind'].values)/10
sort_df1_model.insert(24,'wind_avg',aver)
aver1=(sort_df1_model['rainfall1'].values+sort_df1_model2['rainfall'].values+sort_df1_model3['rainfall'].values+sort_df1_model4['rainfall'].values+sort_df1_model5['rainfall'].values+sort_df1_model6['rainfall'].values+sort_df1_model7['rainfall'].values+sort_df1_model8['rainfall'].values+sort_df1_model9['rainfall'].values+sort_df1_model10['rainfall'].values)/10
sort_df1_model.insert(25,'rainfall_avg',aver1)

'''
df2=sort_df1_model.drop('xid',axis=1)
df3=df2.drop('yid',axis=1)
df4=df3.drop('hour',axis=1)
df5=df4.drop('date_id',axis=1)
df5['wind_max']=df5.apply(lambda x:x.max(),axis=1)
df5['wind_min']=df5.apply(lambda x:x.min(),axis=1)
'''

#sort_df1_model.insert(15,'wind_max',df5['wind_max'].values)
#sort_df1_model.insert(16,'wind_min',df5['wind_min'].values)

sort_df1_model.to_csv('/Users/apple/Desktop/trainday_all/trainday5_all.csv',index=False)


















