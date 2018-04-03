#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 14:52:22 2018

@author: apple
"""
import tensorflow as tf
import numpy as np

x_data=np.random.rand(100)
y_data=x_data*0.1+0.2

b=tf.Variable(0.)
k=tf.Variable(0.)
y=k*x_data+b

#二次代价函数
loss=tf.reduce_mean(tf.square(y_data-y))

#定义梯度下降法训练优化器
optimizer=tf.train.GradientDescentOptimizer(0.2)

#定义最小化代价函数
train=optimizer.minimize(loss)

init=tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for step in range(501):
        sess.run(train)
        if step%20==0:
            print(step,sess.run([k,b]))
        
        
        
        
        
        
        
        


