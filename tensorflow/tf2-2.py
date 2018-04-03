#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 14:31:15 2018

@author: apple
"""
import tensorflow as tf
x=tf.Variable([1,2])
a=tf.constant([3,3])
sub=tf.subtract(x,a)
add=tf.add(x,sub)
init=tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(sub))
    print(sess.run(add))
    

state=tf.Variable(0,name='counter')
new_value=tf.add(state,1)
#付值op，把后边的值付给前面的
update=tf.assign(state,new_value)
init=tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(state))
    for _ in range(100):
        print(sess.run(update))
    