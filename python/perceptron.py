# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 14:05:08 2017

@author: DELL
"""
from sklearn import datasets
import numpy as np
iris=datasets.load_iris()
X=iris.data[:,[2,3]]
y=iris.target

#将数据集划分为训练数据集和测试数据集,随机将数据矩阵X与类标按照3：7的比例
from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)
#scikit-learn 中的preprocessing 中的standardscaler类对特征进行标准化处理
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
sc.fit(X_train)#fit方法计算出训练集中每个特征的均值和方差
X_train_std=sc.transform(X_train)
X_test_std=sc.transform(X_test)
#训练感知器
from sklearn.linear_model import Perceptron
ppn=Perceptron(n_iter=40,eta0=0.1,random_state=0)
ppn.fit(X_train_std,y_train)
y_pre=ppn.predict(X_test_std)

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,y_pre))
