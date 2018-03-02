# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 19:19:02 2017

@author: DELL
"""
import pandas as pd
import numpy as np
df_wine=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data',header=None)
df_wine.columns=['Class label','Alcohol','Malic acid','Ash','Alcalinity','Magnesium','Total phenols',\
                 'Flavanoids','Np','pro','ci','hue','OD280','Proline']
X,y=df_wine.iloc[:,1:].values,df_wine.iloc[:,0].values
from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)
#scikit-learn 中的preprocessing 中的standardscaler类对特征进行标准化处理
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
sc.fit(X_train)#fit方法计算出训练集中每个特征的均值和方差
X_train_std=sc.transform(X_train)
X_test_std=sc.transform(X_test)
from sklearn.ensemble import RandomForestClassifier
feat_labels=df_wine.columns[1:]
forest=RandomForestClassifier(n_estimators=10000,random_state=0,n_jobs=-1)
forest.fit(X_train,y_train)
importances=forest.feature_importances_
indices=np.argsort(importances)[::-1]
for f in range(X_train.shape[1]):
    print(feat_labels[f],importances[indices[f]])
import matplotlib.pyplot as plt
plt.bar(range(X_train.shape[1]),importances[indices],align='center')
plt.xlim([-1,X_train.shape[1]])
plt.tight_layout()
plt.show()