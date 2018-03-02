# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 13:42:26 2017

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

from sklearn.ensemble import RandomForestClassifier
forest=RandomForestClassifier(criterion='entropy',n_estimators=10,random_state=1,n_jobs=2)
forest.fit(X_train_std,y_train)

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
plot_decision_regions(X=X_combined_std,y=y_combined_std,classifier=forest,test_idx=range(105,150))
plt.xlabel('petal length[standardized]')
plt.ylabel('width')
plt.legend(loc='upper left')
plt.show()
