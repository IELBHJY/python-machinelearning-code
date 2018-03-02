# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 15:47:02 2017

@author: DELL
"""
import pandas as pd
df=pd.DataFrame([['green','M','10.1','calss1'],['red','L','13.5','class2'],['blue','XL',15.3,'class1']])
df.columns=['color','size','price','classlabel']
size_mapping={'XL':3,'L':2,'M':1}
inv_size_mapping={v:k for k,v in size_mapping.items()}
df['size']=df['size'].map(size_mapping)
df['size']=df['size'].map(inv_size_mapping)

