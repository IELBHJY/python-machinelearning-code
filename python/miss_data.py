# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 20:23:39 2017

@author: DELL
"""
import pandas as pd
from io import StringIO
csv_data='''A,B,C,D
1,2,3,4
5,6,,8
0,11,12,'''
df=pd.read_csv(StringIO(csv_data))
df.isnull()
df.isnull().sum()
df.values
df.dropna()
df.dropna(axis=1)
df.dropna(how='all')
df.dropna(thresh=4)
df.dropna(subset=['C'])
from sklearn.preprocessing import Imputer
imr=Imputer(missing_values='NaN',strategy='mean',axis=0)
imr=imr.fit(df)
data=imr.transform(df.values)

