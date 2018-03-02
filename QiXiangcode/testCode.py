#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 11:25:09 2017

@author: apple
"""
import pandas as pd
df=pd.read_csv('/Users/apple/Desktop/results_bo.csv',header=None)
CityData=pd.read_csv('/Users/apple/Documents/data/CityData.csv')
df.columns=['cid','date_id','time','xid','yid']
score=0
for i in range(6,11):
    for j in range(1,11):
        df1=df[df.date_id==i][df[df.date_id==i].cid==j]#取到某一天某一个城市的路径时间
        df1.index=range(0,len(df1.xid))
        #判断路径是否符合相邻要求，判断路径是否满足天气要求，判断路径终点是不是要求的终点，起点是不是要求的起点
        if df1.iloc[0,2]!="03:00":#此处时间有争议，但问题不大
            print("第"+str(i)+"天第"+str(j)+"个城市不满足起点时间要求。")
            #continue
        if df1.iloc[0,3]!=142 or df1.iloc[0,4]!=328:
            print("第"+str(i)+"天第"+str(j)+"个城市不满足起点要求。")
            #continue
        if df1.iloc[len(df1['xid'])-1,3]!=CityData.iloc[j,1] or df1.iloc[len(df1['yid'])-1,4]!=CityData.iloc[j,2]:
            print("第"+str(i)+"天第"+str(j)+"个城市不满足终点要求。")
            #continue
        for c in range(0,len(df1['xid'])-1):
            x1,y1=float(df1.iloc[c,3]),float(df1.iloc[c,4])
            x2,y2=float(df1.iloc[c+1,3]),float(df1.iloc[c+1,4])
            if (x1==x2 and y2==y1+1)or(x1==x2 and y2==y1-1) or (x2==x1+1 and y2==y1) or (x2==x1-1 and y2==y1):
                print("",end=' ')
            else:
                print(x1,y1,x2,y2)
                print("第"+str(i)+"天第"+str(j)+"个城市不满足路径中坐标要求。")
                break
        #判断天气情况是否满足
        '''
        for c in range(0,len(df1['xid'])):
            x,y=float(df1.iloc[c,3]),float(df1.iloc[c,4])
            time=df1.iloc[c,2].split(':')
            weather=pd.read_csv('/Users/apple/Desktop/TestMazeMax15/Testmaze_date'+str(i)+'_hour'+str(int(time[0]))+'.csv',header=None)
            w=weather.iloc[int(x-1),int(y-1)]
            if w==0:
                print(x,y)
                print("第"+str(i)+"天第"+str(j)+"个城市不满足路径不满足天气"+str(int(time[0])))
                break
      '''
#df10=pd.read_csv('/Users/apple/Desktop/result.csv',header=None)
#weather=pd.read_csv('/Users/apple/Desktop/TestMazeMax15/Testmaze_date'+str(i)+'_hour'+str(int(time[0]))+'.csv',header=None)
#import pandas as pd
#weather=pd.read_csv('/Users/apple/Desktop/TestMazeMax15/Testmaze_date6_hour3.csv',header=None)