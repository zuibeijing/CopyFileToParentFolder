#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/6/10 23:20
# @Author  : Victor (weigang) QIU
# @web     : http://www.weigang.com
# @Software: PyCharm

import os
import sys
import getpass
import shutil


'''
用于把文件夹里面的文件copy到外面的小程序
原来的文件都是刚在类似
D:\Python video\7.1 python3英文视频教程(全87集)\python3英文视频教程－1\python3英文视频教程－1.mp4
通过这个程序，把需要的文件统一放到父目录
'''

# 文件的拷贝用shutil.copyfile(srcFilePath,dstFilePath)

for i in range(1,88):
    os.chdir('D:\\Python video\\7.1 python3英文视频教程(全87集)\\python3英文视频教程－%d\\' % i)
    print(os.getcwd())


    shutil.copyfile("python3英文视频教程－%d.mp4" % i, "../python3英文视频教程－%d.mp4" % i)

# srcFilePath = 'D:\\Python video\\7.1 python3英文视频教程(全87集)\\python3英文视频教程－1\\'
# dstFilePath = 'D:\\Python video\\7.1 python3英文视频教程(全87集)\\'
# shutil.copyfile(srcFilePath,dstFilePath)
