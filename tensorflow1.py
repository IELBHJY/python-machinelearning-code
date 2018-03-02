#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 22:14:33 2018

@author: apple
"""
import tensorflow as tf
import numpy as np
from PIL import Image
from IPython.display import Image as IPythonImage, display
R=6 #有限半径
ITER_NUM=100 #迭代次数
def get_color(ratio1, ratio2, ratio3):
    def color(z, i):
        if abs(z) < R:
            return 0, 0, 0
        #属于Mandelbrot集合的点标记为黑色
        v = np.log2(i + R - np.log2(np.log2(abs(z)))) / 5
        #定义发散速度
        if v < 1.0:
            return v**4, v**2.5, v ** 1
        else:
            v = max(0, 1 - v)
            return v**ratio1, v**ratio2, v**ratio3
        #按照发散速度的不同，对于不属于Mandelbrot集合的点，定义不同的颜色
    return color
def gen_mandelbrot(Z, ratio1, ratio2, ratio3):
    xs = tf.constant(Z.astype(np.complex64)) #常量，复平面的每一个点，相当于公式中的初始值C
    zs = tf.Variable(xs) #变量
    ns = tf.Variable(tf.zeros_like(xs, tf.float32)) #发散的标记
    print(xs,zs,ns)
    with tf.Session():
        tf.global_variables_initializer().run()
        #print(ns.eval())
        zs_ = tf.where(tf.abs(zs) < R, zs**2 + xs, zs)#迭代
        #print(zs_.eval())
        not_diverged = tf.abs(zs_) < R #判断迭代之后是否发散
        step = tf.group(
            zs.assign(zs_),
            ns.assign_add(tf.cast(not_diverged, tf.float32))
        )
        for i in range(ITER_NUM):
            #迭代100次
            #print(not_diverged.eval())
            #print(i)
            step.run()
        final_step = ns.eval()
        final_z = zs_.eval()
    r, g, b = np.frompyfunc(get_color(ratio1, ratio2, ratio3), 2, 3)(final_z, final_step)
    img_array = np.dstack((r, g, b))
    return Image.fromarray(np.uint8(img_array * 255))
start_x = -2.5  # x range
end_x = 1
start_y = -1.2  # y rangea
end_y = 1.2
width = 1000 #图片的像素

step = (end_x - start_x) / width
Y, X = np.mgrid[start_y:end_y:step, start_x:end_x:step]
Z = X + 1j * Y
img = gen_mandelbrot(Z, 1, 1.5, 3)
img.save('mandelbrot.png')
display(img)
