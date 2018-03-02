# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 19:26:37 2017

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
cov_mat=np.cov(X_train_std.T)
eigen_vals,eigen_vecs=np.linalg.eig(cov_mat)
tot=sum(eigen_vals)
var_exp=[(i/tot) for i in sorted(eigen_vals,reverse=True)]
cum_var_exp=np.cumsum(var_exp)

import matplotlib.pyplot as plt
'''
plt.bar(range(1,14),var_exp,alpha=0.5,align='center')
plt.step(range(1,14),cum_var_exp,alpha=0.5,where='mid')
plt.legend(loc='best')

plt.show()
'''
eigen_pairs=[(np.abs(eigen_vals[i]),eigen_vecs[:,i]) for i in range(len(eigen_vals))]
#print(eigen_pairs)
eigen_pairs.sort(reverse=True)
#print(eigen_pairs)
w=np.hstack((eigen_pairs[0][1][:,np.newaxis],eigen_pairs[1][1][:,np.newaxis]))
print(w)
X_train_pca=X_train_std.dot(w)
print(X_train_pca)
colors=['r','b','g']
markers=['s','x','o']
for l,c,m in zip(np.unique(y_train),colors,markers):
    plt.scatter(X_train_pca[y_train==l,0],X_train_pca[y_train==l,1],c=c,label=l,marker=m)
plt.xlabel('PC 1')
plt.ylabel('PC 2')
plt.legend(loc='lower left')  
from sklearn.decomposition import PCA
pca=PCA(n_components=2)
X_train_pca=pca.fit_transform(X_train_std)
X_test_pca=pca.transform(X_test_std)




