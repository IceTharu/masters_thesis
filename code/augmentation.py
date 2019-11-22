#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 11:58:27 2019

@author: thorsteinngj
"""

import numpy as np
import imgaug as ia
import imgaug.augmenters as iaa
import matplotlib.pyplot as plt
import cv2

im = cv2.imread("/home/thorsteinngj/Documents/Skoli/Thesis/Code/Mask_RCNN/samples/graves/new_dataset/train/106675864.jpg")

#images = np.random.randint(0, 255, (16, 128, 128, 3), dtype=np.uint8)

empty_mat = np.zeros((16,339,280,3),dtype=np.uint8)

for i in range(16):
    empty_mat[i,:,:,:] = im
    
#empty_mat = empty_mat.astype(int)

#sometimes = lambda aug: iaa.Sometimes(0.5,aug)
seq = iaa.Sometimes(5/6,iaa.OneOf([iaa.Fliplr(1),iaa.Flipud(1),iaa.GaussianBlur((0,0.5)),iaa.Dropout((0.05,0.1)),iaa.Grayscale(0.5),iaa.Canny(alpha=(0.1,0.3))]))

seq.show_grid([empty_mat[0]], cols=3, rows=3)
