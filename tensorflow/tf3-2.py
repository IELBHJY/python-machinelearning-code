#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 15:30:20 2018

@author: apple
"""
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist=input_data.read_data_sets('MNIST_data',one_hot=True)

#每个批次的大小
batch_size=100
n_batch=mnist.train.num_examples

x=tf.placeholder(tf.float32,[None,784])
y=tf.placeholder(tf.float32,[None,10])
keep_prob=tf.placeholder(tf.float32)
#nn
#w=tf.Variable(tf.zeros([784,10]))
#b=tf.Variable(tf.zeros([10]))
#prediction=tf.nn.softmax(tf.matmul(x,w)+b)
# w,b的初始化
W1=tf.Variable(tf.truncated_normal([784,2000],stddev=0.1))
b1=tf.Variable(tf.zeros([2000])+0.1)

L1=tf.nn.tanh(tf.matmul(x,W1)+b1)
L1_drop=tf.nn.dropout(L1,keep_prob)

loss=tf.reduce_mean(tf.square(y-prediction))
#交叉熵
#loss=tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y,logits=prediction))
train=tf.train.GradientDescentOptimizer(0.2).minimize(loss)
#tf.train.AdamOptimizer(1e-2).minimize(loss)
init=tf.global_variables_initializer()

#argmax返回一维张量中最大值所在的位置
correct_prediction=tf.equal(tf.arg_max(y,1),tf.arg_max(prediction,1))
accuracy=tf.reduce_mean(tf.cast(correct_prediction,tf.float32))

with tf.Session() as sess:
    sess.run(init)
    for epoch in range(11):
        for batch in range(n_batch):
            batch_x,batch_y=mnist.train.next_batch(batch_size)
            sess.run(train,feed_dict={x:batch_x,y:batch_y})
        acc=sess.run(accuracy,feed_dict={x:mnist.test.images,y:mnist.test.labels})
        print("iter"+str(epoch)+"test accuracy"+str(acc))