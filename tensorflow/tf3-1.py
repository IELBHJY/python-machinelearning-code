#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 15:10:14 2018

@author: apple
"""
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

x_data=np.linspace(-0.5,0.5,200)[:,np.newaxis]
noise=np.random.normal(0,0.02,x_data.shape)
y_data=np.square(x_data)+noise

x=tf.placeholder(tf.float32,[None,1])
y=tf.placeholder(tf.float32,[None,1])

weight1=tf.Variable(tf.random_normal([1,10]))
biases1=tf.Variable(tf.zeros([1,10]))
w_plus_b=tf.matmul(x,weight1)+biases1

#激活函数
l1=tf.nn.tanh(w_plus_b)

#定义输出层
weight2=tf.Variable(tf.random_normal([10,1]))
biases2=tf.Variable(tf.zeros([1,1]))
w_plus_b2=tf.matmul(l1,weight2)+biases2
predict=tf.nn.tanh(w_plus_b2)

loss=tf.reduce_mean(tf.square(predict-y))
train=tf.train.GradientDescentOptimizer(0.1)
optimizer=train.minimize(loss)
init=tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    for _ in range(2000):
        sess.run(optimizer,feed_dict={x:x_data,y:y_data})
    
    prediction=sess.run(predict,feed_dict={x:x_data})
    plt.figure()
    plt.scatter(x_data,y_data)
    plt.plot(x_data,prediction,'r-',lw=5)
    plt.show()




