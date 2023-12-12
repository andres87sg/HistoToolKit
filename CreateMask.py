# -*- coding: utf-8 -*-
"""
EN:

    Create B&W mask that fits to Patch
    
ES:
    Crea una máscara Blanca o Negra que se ajusta al tamaño del parche 

"""

import cv2 as cv
from skimage import color

import numpy as np
import matplotlib.pyplot as plt

from os import listdir
from PIL import Image

path = 'D:/TCGA-GBM_Patches/CT/WSI/'
destpath = 'D:/TCGA-GBM_Patches/CT/SG/'

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