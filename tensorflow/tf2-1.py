#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 14:18:27 2018

@author: apple
"""
#tensorflow 2-1创建图 启动图
import tensorflow as tf
m1=tf.constant([[3,3]])
m2=tf.constant([[2],[3]])
product=tf.matmul(m1,m2)
print(product)

#with th,session() as sess:
sess=tf.Session()
result=sess.run(product)
print(result)
sess.close()

