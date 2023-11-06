# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 23:20:15 2023

@author: Andres
"""

import cv2 as cv
from skimage import color

import numpy as np
import matplotlib.pyplot as plt

from os import listdir
from PIL import Image

path = 'D:/CPTAC-GBM_Patches/CT/WSI/'
destpath = 'D:/CPTAC-GBM_Patches/CT/SG/'

listfiles = listdir(path)
listfiles.sort()

for i,filename in enumerate(listfiles):
    print('Image No %i: ' %i + filename[:-4])
    # print(i)
    im1 = Image.open(path + filename)
    im1 = np.asarray(im1)
    
    # White mask
    mask = np.ones(np.shape(im1))*255
    
    #Black mask
    # mask = np.ones(np.shape(im1))*0
    
    
    
    # ImRgb2lab = color.rgb2lab(im1)
    
    # ImChOut=separatelab(ImRgb2lab,channel='L')
    cv.imwrite(destpath+'SG_'+filename, mask)