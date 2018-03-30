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

#nn
w=tf.Variable(tf.zeros([784,10]))
b=tf.Variable(tf.zeros([10]))
prediction=tf.nn.softmax(tf.matmul(x,w)+b)

loss=tf.reduce_mean(tf.square(y-prediction))

train=tf.train.GradientDescentOptimizer(0.2).minimize(loss)

init=tf.global_variables_initializer()

#argmax返回一维张量中最大值所在的位置
correct_prediction=tf.equal(tf.arg_max(y,1),tf.arg_max(prediction,1))
accuracy=tf.reduce_mean(tf.cast(correct_prediction,tf.float32))

with tf.Session() as sess:
    sess.run(init)
    for epoch in range(21):
        for batch in range(n_batch):
            batch_x,batch_y=mnist.train.next_batch(batch_size)
            sess.run(train,feed_dict={x:batch_x,y:batch_y})
        acc=sess.run(accuracy,feed_dict={x:mnist.test.images,y:mnist.test.labels})
        print("iter"+str(epoch)+"test accuracy"+str(acc))