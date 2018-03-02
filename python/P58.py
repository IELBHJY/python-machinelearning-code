# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 14:12:48 2017

@author: DELL
"""
#数据预处理
import pandas as pd
import numpy as np
df=pd.read_csv('C:/Users/DELL/Desktop/2.csv')
df.isnull().sum()
'''
data.loc[(data["Gender"]=="Female") & (data["Education"]=="Not Graduate") & (data["Loan_Status"]=="Y"), ["Gender","Education","Loan_Status"]]


'''