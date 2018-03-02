# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 12:23:10 2017

@author: GeLiang
"""
import pandas as pd
import numpy as np

import os
import csv
import pylab as plt
import numpy as np
import pandas as pd
import os
import matplotlib.cm as cm
from matplotlib.colors import LogNorm


#trainFile = "H:\算法\飞行器路线优化\ForecastDataforTraining\ForecastDataforTraining.csv"
for date in range(5):
    file='testday'+str(date+6)+'_windall.csv'
    trainFile = 'H://算法//飞行器路线优化new//testdata'+'//'+file

    pwd = os.getcwd()
    os.chdir(os.path.dirname(trainFile))
    trainData = pd.read_csv(os.path.basename(trainFile),iterator=True)
    os.chdir(pwd)
    '''try:
        df = trainData.get_chunk(100000000)
        except StopIteration:
    print("Iteration is stopped.")'''


    loop = True
    chunkSize = 1000000
    chunks = []
    while loop:
        try:
            chunk = trainData.get_chunk(chunkSize)
            chunks.append(chunk)
        except StopIteration:
            loop = False
            print("Iteration is stopped.")
    df = pd.concat(chunks, ignore_index=True)
    df1=df.iloc[:,5:8]
    df1.insert(3,'wind6',df['wind6'].values)
    df1.insert(4,'wind8',df['wind8'].values)
    df1.insert(5,'wind10',df['wind10'].values)
    
    df.insert(17,'wind_max2',df1.iloc[:,:].max(1).values)
    df.insert(18,'wind_avg2',df1.iloc[:,:].mean(1).values)
    df.insert(19,'wind_min2',df1.iloc[:,:].min(1).values)
    filename='testday'+str(date+6)+'_wind.csv'
    df.to_csv('H://算法//飞行器路线优化new//testdata//testday_model2346810'+'//'+filename,index=False)
    
    
    windmax=[[0]*421 for i in range(548)]
    mazemax=[[0]*421 for i in range(548)]
    windmin=[[0]*421 for i in range(548)]
    mazemin=[[0]*421 for i in range(548)]
    windavg=[[0]*421 for i in range(548)]
    mazeavg=[[0]*421 for i in range(548)]
    for i in range(18):
        dfmax=df[df.hour==i+3]
        x,y,z = dfmax['xid'].values,dfmax['yid'].values,dfmax['wind_max2'].values
        z = z.reshape(548, 421)
        fig=plt.figure(figsize=(12,8))
        plt.text(142,328,'o',fontdict={'size':20,'color':'k'})
        plt.text(84,202,'x1',fontdict={'size':16,'color':'r'})
        plt.text(199,371,'x2',fontdict={'size':16,'color':'r'})
        plt.text(140,234,'x3',fontdict={'size':16,'color':'r'})
        plt.text(236,241,'x4',fontdict={'size':16,'color':'r'})
        plt.text(315,281,'x5',fontdict={'size':16,'color':'r'})
        plt.text(358,207,'x6',fontdict={'size':16,'color':'r'})
        plt.text(363,237,'x7',fontdict={'size':16,'color':'r'})
        plt.text(423,266,'x8',fontdict={'size':16,'color':'r'})
        plt.text(125,375,'x9',fontdict={'size':16,'color':'r'})
        plt.text(189,274,'x10',fontdict={'size':16,'color':'r'})
        titleStr='TestWindMax: date='+str(date+6)+',hour='+str(i+3)
        plt.title(titleStr)
        plt.imshow(z, extent=(np.amin(x), np.amax(x), np.amin(y), np.amax(y)),
                   cmap=cm.jet,aspect='auto', vmin=0,vmax=30)
        plt.colorbar()
        figname='TestWindMax_date'+str(date+6)+'_hour'+str(i+3)+'.jpg'
        plt.savefig('H://算法//飞行器路线优化new//testdata//testday_model2346810//Figures//Fig_windmax'+'//'+figname)
        plt.show()
        
        x,y,z = dfmax['xid'].values,dfmax['yid'].values,dfmax['wind_avg2'].values
        z = z.reshape(548, 421)
        fig=plt.figure(figsize=(12,8))
        plt.text(142,328,'o',fontdict={'size':20,'color':'k'})
        plt.text(84,202,'x1',fontdict={'size':16,'color':'r'})
        plt.text(199,371,'x2',fontdict={'size':16,'color':'r'})
        plt.text(140,234,'x3',fontdict={'size':16,'color':'r'})
        plt.text(236,241,'x4',fontdict={'size':16,'color':'r'})
        plt.text(315,281,'x5',fontdict={'size':16,'color':'r'})
        plt.text(358,207,'x6',fontdict={'size':16,'color':'r'})
        plt.text(363,237,'x7',fontdict={'size':16,'color':'r'})
        plt.text(423,266,'x8',fontdict={'size':16,'color':'r'})
        plt.text(125,375,'x9',fontdict={'size':16,'color':'r'})
        plt.text(189,274,'x10',fontdict={'size':16,'color':'r'})
        titleStr='TestWindAvg: date='+str(date+6)+',hour='+str(i+3)
        plt.title(titleStr)
        plt.imshow(z, extent=(np.amin(x), np.amax(x), np.amin(y), np.amax(y)),
                   cmap=cm.jet,aspect='auto', vmin=0,vmax=30)
        plt.colorbar()
        figname='TestWindAvg_date'+str(date+6)+'_hour'+str(i+3)+'.jpg'
        plt.savefig('H://算法//飞行器路线优化new//testdata//testday_model2346810//Figures//Fig_windavg'+'//'+figname)
        plt.show()
        x,y,z = dfmax['xid'].values,dfmax['yid'].values,dfmax['wind_min2'].values
        z = z.reshape(548, 421)
        fig=plt.figure(figsize=(12,8))
        plt.text(142,328,'o',fontdict={'size':20,'color':'k'})
        plt.text(84,202,'x1',fontdict={'size':16,'color':'r'})
        plt.text(199,371,'x2',fontdict={'size':16,'color':'r'})
        plt.text(140,234,'x3',fontdict={'size':16,'color':'r'})
        plt.text(236,241,'x4',fontdict={'size':16,'color':'r'})
        plt.text(315,281,'x5',fontdict={'size':16,'color':'r'})
        plt.text(358,207,'x6',fontdict={'size':16,'color':'r'})
        plt.text(363,237,'x7',fontdict={'size':16,'color':'r'})
        plt.text(423,266,'x8',fontdict={'size':16,'color':'r'})
        plt.text(125,375,'x9',fontdict={'size':16,'color':'r'})
        plt.text(189,274,'x10',fontdict={'size':16,'color':'r'})
        titleStr='TestWindMin: date='+str(date+6)+',hour='+str(i+3)
        plt.title(titleStr)
        plt.imshow(z, extent=(np.amin(x), np.amax(x), np.amin(y), np.amax(y)),
                   cmap=cm.jet,aspect='auto', vmin=0,vmax=30)
        plt.colorbar()
        figname='TestWindMin_date'+str(date+6)+'_hour'+str(i+3)+'.jpg'
        plt.savefig('H://算法//飞行器路线优化new//testdata//testday_model2346810//Figures//Fig_windmin'+'//'+figname)
        plt.show()
        for j in range(548):
            for k in range(421):
                xid=df.iloc[j*421+k,0]
                yid=df.iloc[j*421+k,1]
                wind_max=df.iloc[j*421+k,17]
                windmax[xid-1][yid-1]=wind_max
                wind_avg=df.iloc[j*421+k,18]
                windavg[xid-1][yid-1]=wind_avg
                wind_min=df.iloc[j*421+k,19]
                windmin[xid-1][yid-1]=wind_min
                if wind_max<15:
                    mazemax[xid-1][yid-1]=1
                if wind_avg<15:
                    mazeavg[xid-1][yid-1]=1
                if wind_min<15:
                    mazemin[xid-1][yid-1]=1
        filenamem='Testwind_date'+str(date+6)+'_hour'+str(i+3)+'.csv'
        with open('H://算法//飞行器路线优化new//testdata//testday_model2346810//TestData_windmax'+'//'+filenamem,'w',newline='') as csvfilem:
            writer=csv.writer(csvfilem)
            writer.writerows(windmax)
        filename2m='Testmaze_date'+str(date+6)+'_hour'+str(i+3)+'.csv'
        with open('H://算法//飞行器路线优化new//testdata//testday_model2346810//TestData_mazemax'+'//'+filename2m,'w',newline='') as csvfile2m:
            writer=csv.writer(csvfile2m)
            writer.writerows(mazemax)
            
        filename='Testwind_date'+str(date+6)+'_hour'+str(i+3)+'.csv'
        with open('H://算法//飞行器路线优化new//testdata//testday_model2346810//TestData_windavg'+'//'+filename,'w',newline='') as csvfile:
            writer=csv.writer(csvfile)
            writer.writerows(windavg)
        filename2='Testmaze_date'+str(date+6)+'_hour'+str(i+3)+'.csv'
        with open('H://算法//飞行器路线优化new//testdata//testday_model2346810//TestData_mazeavg'+'//'+filename2,'w',newline='') as csvfile2:
            writer=csv.writer(csvfile2)
            writer.writerows(mazeavg)
            
        filename3='Testwind_date'+str(date+6)+'_hour'+str(i+3)+'.csv'
        with open('H://算法//飞行器路线优化new//testdata//testday_model2346810//TestData_windmin'+'//'+filename3,'w',newline='') as csvfile3:
            writer=csv.writer(csvfile3)
            writer.writerows(windmin)
        filename4='Testmaze_date'+str(date+6)+'_hour'+str(i+3)+'.csv'
        with open('H://算法//飞行器路线优化new//testdata//testday_model2346810//TestData_mazemin'+'//'+filename4,'w',newline='') as csvfile4:
            writer=csv.writer(csvfile4)
            writer.writerows(mazemin)




