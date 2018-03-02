#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 20:43:49 2017

@author: apple
"""
import os
import pandas as pd
#os.chdir()
df=pd.read_csv('/Users/apple/Desktop/lbh20171117_203103.csv')
df.to_csv('/Users/apple/Desktop/submission.csv',index=False)
