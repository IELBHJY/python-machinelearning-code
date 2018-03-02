#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 19:11:17 2017

@author: apple
"""
import pandas as pd
for h in range(3,21):
    print('-----------hour'+str(h)+'------------')
    df=pd.read_csv('/Users/apple/Desktop/test20171218_pro_15/TestDay6_hour'+str(h)+'.csv')
    #print(df.iloc[83,202])
    #print(df.iloc[198,370])
    #print(df.iloc[139,233])
    #print(df.iloc[235,240])
    #print(df.iloc[314,280])---wind is well
    #print(df.iloc[357,206])---wind is well
    #print(df.iloc[362,236])----wind is well
    #print(df.iloc[422,265])
    #print(df.iloc[124,374])
    #print(df.iloc[188,273])

