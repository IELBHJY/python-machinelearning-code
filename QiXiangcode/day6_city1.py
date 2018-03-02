#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 12:10:48 2017

@author: apple
"""
import pandas as pd
df=pd.read_csv('/Users/apple/Desktop/1/2.csv',header=None)
for i in range(len(df.index)-1):
    if df.iloc[i,3]!=df.iloc[i+1,3] and df.iloc[i,4]!=df.iloc[i+1,4]:
        print("error")