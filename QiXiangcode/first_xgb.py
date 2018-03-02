#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 15:17:11 2017

@author: apple
"""
import pandas as pd
#import numpy as np
import xgboost as xgb
#from sklearn.cross_validation import train_test_split
#df=pd.read_csv('/Users/apple/Documents/data/In-situMeasurementforTraining_20171124.csv')
df1=pd.read_csv('/Users/apple/Desktop/TianchiUAV/traindata/traindata_day1.csv')
df2=pd.read_csv('/Users/apple/Desktop/TianchiUAV/traindata/traindata_day2.csv')
df3=pd.read_csv('/Users/apple/Desktop/TianchiUAV/traindata/traindata_day3.csv')
df4=pd.read_csv('/Users/apple/Desktop/TianchiUAV/traindata/traindata_day4.csv')
df5=pd.read_csv('/Users/apple/Desktop/TianchiUAV/traindata/traindata_day5.csv')
df=pd.concat([df1,df2,df3,df4,df5],ignore_index=True)
X=df[['xid','yid','date_id','hour','wind1','wind2','wind3','wind4','wind5','wind6','wind7','wind8','wind9','wind10','wind_avg','wind_min','wind_max']]
y=df['wind']
for i in range(0,len(y)):
    if y.values[i]<15:
        y.values[i]=0
    else:
        y.values[i]=1
#X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)
dtrain=xgb.DMatrix(data=X,label=y)
Trate=0.25  
params = {'booster':'gbtree',
                  'eta': 0.1,
                   'max_depth': 4,
                   'max_delta_step': 0,
                   'subsample':0.9,      
                   'colsample_bytree': 0.9,
                   'base_score': Trate,
                   'objective': 'multi:softmax',
                   'num_class':2,
                   'lambda':5,
                   'alpha':8,
                   'random_seed':100
                   }
params['eval_metric'] = 'auc' 
xgb_model=xgb.train(params,dtrain,num_boost_round=200,maximize=True,verbose_eval=True)
X_test=pd.read_csv('/Users/apple/Desktop/Testdata/testday6_windall.csv')
y_pre=xgb_model.predict(xgb.DMatrix(X_test))
X_test['wind']=y_pre
X_test.to_csv('/Users/apple/Desktop/pre_day6.csv',index=False)
#from sklearn.metrics import accuracy_score
#print(accuracy_score(y_test,y_pre))
'''
day1真值构建模型 0.966466370852
day1真值训练模型预测day2 0.905075535598
1-5天xgboost 预测准确率 0.951701493438
'''