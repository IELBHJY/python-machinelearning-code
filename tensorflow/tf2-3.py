#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 14:44:04 2018

@author: apple
"""
import tensorflow as tf
#Fetch 会话执行多个op，同时运行其结果
input1=tf.constant(3.0)
input2=tf.constant(2.0)
input3=tf.constant(5.0)
add=tf.add(input2,input3)
mul=tf.multiply(input1,add)
with tf.Session() as sess:
    print(sess.run([mul,add]))
    
    
#Feed  占位符
m1=tf.placeholder(tf.float32)
m2=tf.placeholder(tf.float32)
mul=tf.multiply(m1,m2)

with tf.Session() as sess:
    print(sess.run(mul,feed_dict={m1:[7.0],m2:[2.0]}))
    


    

