#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 14:04:57 2017

@author: apple
"""
from sklearn import datasets
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
iris=datasets.load_iris()
X=iris.data[:,[0,1,2,3]]
y=iris.target
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)
sc=StandardScaler()
sc.fit(X_train)
X_train_std=sc.transform(X_train)
X_test_std=sc.transform(X_test)
from sklearn.svm import SVC
svm=SVC(kernel='rbf',random_state=0,gamma=0.1,C=1.0)
svm.fit(X_train_std,y_train)
y_pre_svm=svm.predict(X_test_std)
print((y_pre_svm!=y_test).sum())

from sklearn.svm import SVC
svm1=SVC(kernel='linear',random_state=0,C=1.0)
svm1.fit(X_train_std,y_train)
y_pre_svm1=svm1.predict(X_test_std)
print((y_pre_svm1!=y_test).sum())

from sklearn.tree import DecisionTreeClassifier
tree=DecisionTreeClassifier(criterion='entropy',max_depth=3,random_state=0)
tree.fit(X_train_std,y_train)
y_pre_tree=tree.predict(X_test_std)
print((y_pre_tree!=y_test).sum())
'''
from sklearn.linear_model import Perceptron
ppn=Perceptron(n_iter=40,eta0=0.1,random_state=0)
ppn.fit(X_train_std,y_train)
y_pre_ppn=ppn.predict(X_test_std)
print((y_pre_ppn!=y_test).sum())
from sklearn.linear_model import LogisticRegression
lr=LogisticRegression(C=1000,random_state=0)
lr.fit(X_train_std,y_train)
y_pre_lr=lr.predict(X_test_std)
print((y_pre_lr!=y_test).sum())
'''
'''
def plot_decision_regions(X,y,classifier,test_idx=None,resolution=0.02):
    markers=('s','x','o','^','v')
    colors=('red','blue','lightgreen','gray','cyan')
    cmap=ListedColormap(colors[:len(np.unique(y))])
    x1_min,x1_max=X[:,0].min()-1,X[:,0].max()+1
    x2_min,x2_max=X[:,0].min()-1,X[:,0].max()+1
    xx1,xx2=np.meshgrid(np.arange(x1_min,x1_max,resolution),np.arange(x2_min,x2_max,resolution))
    Z=classifier.predict(np.array([xx1.ravel(),xx2.ravel()]).T)
    Z=Z.reshape(xx1.shape)
    plt.contourf(xx1,xx2,Z,alpha=0.4,cmap=cmap)
    plt.xlim(xx1.min(),xx1.max())
    plt.ylim(xx2.min(),xx2.max())
    X_test,y_test=X[test_idx,:],y[test_idx]
    for idx,cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y==cl,0],y=X[y==cl,1],alpha=0.8,c=cmap(idx),marker=markers[idx],label=cl)
    if test_idx:
        X_test,y_test=X[test_idx,:],y[test_idx]
        plt.scatter(X_test[:,0],X_test[:,1],c='',alpha=1.0,linewidth=1,marker='o',s=55,label='test set')
X_combined_std=np.vstack((X_train_std,X_test_std))
y_combined_std=np.hstack((y_train,y_test))
plot_decision_regions(X=X_combined_std,y=y_combined_std,classifier=svm,test_idx=range(105,150))
plt.xlabel('petal length[standardized]')
plt.ylabel('width')
plt.legend(loc='upper left')
plt.show()
'''