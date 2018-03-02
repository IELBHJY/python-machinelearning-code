# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 12:23:10 2017

@author: Apple
"""
import pandas as pd
import os
trainFile = '/Users/apple/Desktop/TianchiUAV/train20171205/trainday3_windall.csv'
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
df=df.drop(['xid','yid','date_id','hour'],1)
w=[0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]
df['weight1']=df['wind1']*w[0]+df['wind2']*w[1]+df['wind3']*w[2]+df['wind4']*w[3]+df['wind5']*w[4]+df['wind6']*w[5]+df['wind7']*w[6]+df['wind8']*w[7]+df['wind9']*w[8]+df['wind10']*w[9]
trainFile = '/Users/apple/Documents/data/Trueday3.csv'
pwd = os.getcwd()
os.chdir(os.path.dirname(trainFile))
train = pd.read_csv(os.path.basename(trainFile),iterator=True)
os.chdir(pwd)
loop = True
chunkSize = 200000
chunks = []
while loop:
    try:
        chunk = train.get_chunk(chunkSize)
        chunks.append(chunk)
    except StopIteration:
        loop = False
        print("Iteration is stopped.")
true = pd.concat(chunks, ignore_index=True)
count1=0
count2=0
for i in range(len(true.wind)):
    count=0
    for j in ['wind1','wind2','wind3','wind4','wind5','wind6','wind7','wind8','wind9','wind10','wind_avg']:
        if df.loc[i,j]<15:
            count+=1
    if float(true.iloc[i,5])<15 and count>=5:
           count1+=1
    if float(true.iloc[i,5])>=15 and count<5:
           count2+=1
print((count1+count2)/len(true.wind))
'''
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
df1_model.columns=['xid','yid','date_id','hour','wind1']
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
sort_df1_model.insert(5,'wind2',sort_df1_model2['wind'].values)
sort_df1_model.insert(6,'wind3',sort_df1_model3['wind'].values)
sort_df1_model.insert(7,'wind4',sort_df1_model4['wind'].values)
sort_df1_model.insert(8,'wind5',sort_df1_model5['wind'].values)
sort_df1_model.insert(9,'wind6',sort_df1_model6['wind'].values)
sort_df1_model.insert(10,'wind7',sort_df1_model7['wind'].values)
sort_df1_model.insert(11,'wind8',sort_df1_model8['wind'].values)
sort_df1_model.insert(12,'wind9',sort_df1_model9['wind'].values)
sort_df1_model.insert(13,'wind10',sort_df1_model10['wind'].values)
#aver=(sort_df1_model['wind'].values+sort_df1_model2['wind'].values+sort_df1_model3['wind'].values+sort_df1_model4['wind'].values+sort_df1_model5['wind'].values+sort_df1_model6['wind'].values+sort_df1_model7['wind'].values+sort_df1_model8['wind'].values+sort_df1_model9['wind'].values+sort_df1_model10['wind'].values)/10
aver=(sort_df1_model['wind1'].values+sort_df1_model2['wind'].values+sort_df1_model3['wind'].values+sort_df1_model4['wind'].values+sort_df1_model5['wind'].values+sort_df1_model6['wind'].values+sort_df1_model7['wind'].values+sort_df1_model8['wind'].values+sort_df1_model9['wind'].values+sort_df1_model10['wind'].values)/10
sort_df1_model.insert(14,'wind_avg',aver)
df2=sort_df1_model.drop('xid',axis=1)
df3=df2.drop('yid',axis=1)
df4=df3.drop('hour',axis=1)
df5=df4.drop('date_id',axis=1)
df5['wind_max']=df5.apply(lambda x:x.max(),axis=1)
df5['wind_min']=df5.apply(lambda x:x.min(),axis=1)
sort_df1_model.insert(15,'wind_max',df5['wind_max'].values)
sort_df1_model.insert(16,'wind_min',df5['wind_min'].values)
sort_df1_model.to_csv('/Users/apple/Desktop/TianchiUAV/test20171205/test10_windall.csv',index=False)
'''

















