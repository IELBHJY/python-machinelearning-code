# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 16:02:17 2017

@author: DELL
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_excel('C://Users//DELL//Desktop//ltb.xls')
X=df.drop(['所用时间','提交答卷时间', '来自IP', '来源', '来源详情', '第12题(两人相互吸引)', '第12题(相爱（没订婚）)', '第12题(确定关系（订婚）)', '第12题(无所谓啦~)','11、您和交往对象最深层次的交往是','7、您的家庭人均年收入大约是','16、您的出生年份是'],axis=1)
y=df['11、您和交往对象最深层次的交往是']
y_mapping={'同居':1,'(跳过)':1,'性*交':1,'接吻':0,'性爱抚':0,'约会':0,'一般朋友':0}
y=y.map(y_mapping)

sex_mapping={'男':1,'女':-1}
X['1、您的性别是']=X['1、您的性别是'].map(sex_mapping)
grade_mapping={'大一':1,'大二':2,'大三':3,'大四':4,'大五':5,'研一':6,'研二':7,'研三':8,'博士及以上':9}
X['2、您的所属年级是']=X['2、您的所属年级是'].map(grade_mapping)
df=pd.get_dummies(X[['3、您的家乡属于哪个地区', '4、您是否为独生子女',
       '5、您来自城市还是农村', '6、您的宗教信仰情况是', '8、您的家庭的户主所接受的教育水平为',
       '9、您的性取向是', '10、您的感情经历是', '13、您是否能接受您的交往对象在您之前和别人有过性行为',
       '14、您对“约炮”（不涉及金钱买卖的性行为）的看法是']])
df['序号']=X['序号']
X=pd.merge(X,df)
X=X.drop(['3、您的家乡属于哪个地区', '4、您是否为独生子女',
       '5、您来自城市还是农村', '6、您的宗教信仰情况是', '8、您的家庭的户主所接受的教育水平为', '9、您的性取向是',
       '10、您的感情经历是', '13、您是否能接受您的交往对象在您之前和别人有过性行为',
       '14、您对“约炮”（不涉及金钱买卖的性行为）的看法是'],axis=1)

from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)
from sklearn.ensemble import RandomForestClassifier
forest=RandomForestClassifier(n_estimators=10000,random_state=0,n_jobs=-1)
feat_labels=X.columns[0:]
forest.fit(X_train,y_train)
importances=forest.feature_importances_
indices=np.argsort(importances)[::-1]
for f in range(X_train.shape[1]):
    print(feat_labels[f],importances[f])
'''
plt.title("特征重要程度")
plt.bar(range(X_train.shape[1]),importances[indices],color='lightblue',align='center')
plt.xticks(range(X.shape[1]),feat_labels,rotation=90)
plt.xlim([-1,X_train.shape[1]])
plt.tight_layout()
plt.show()
'''
