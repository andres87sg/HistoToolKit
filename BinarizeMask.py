# -*- coding: utf-8 -*-
"""
Binarize Mask

@author: Andres
"""

import cv2 as cv
from skimage import color

import numpy as np
import matplotlib.pyplot as plt

from os import listdir
from PIL import Image

path = 'D:/JournalExperiments/PC/TCGA/PC_1792_ChL/Train/PC_SG/'
destpath = 'D:/JournalExperiments/PC/TCGA/PC_1792_ChL/Train/PC_SG/'

listfiles = listdir(path)
listfiles.sort()

for i,filename in enumerate(listfiles):
    print('Image No %i: ' %i + filename[:-4])
    # print(i)
    im1 = Image.open(path + filename)
    im1 = np.asarray(im1)
    th, im_th = cv.threshold(im1, 128, 255, cv.THRESH_BINARY)
    mask = np.uint16(im_th)
    
    cv.imwrite(destpath+filename, mask)