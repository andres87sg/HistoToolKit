# -*- coding: utf-8 -*-
import cv2 as cv
from skimage import color

import numpy as np
import matplotlib.pyplot as plt

from os import listdir
from PIL import Image
from tqdm import tqdm

# D:/BraTS2024_New/AdditionalSamples/PN/
path = 'D:/BraTS2024_New/AdditionalSamples/PN/'
destpath = 'D:/BraTS2024_New/AdditionalSamples/PN2/'
# path = 'D:/TCGA-GBM_Patches_PC_X/'
# destpath = 'D:/MV/TCGA-GBM_Patches_MV_LAB/'
# path = 'C:/Users/Andres/Desktop/patchextraction/PC_1792_raw_Jan2024/Train/PC/'
# destpath = 'C:/Users/Andres/Desktop/patchextraction/PC_1792_ChL_Jan2024/Train/PC/'


# Image list
listfiles = listdir(path)
listfiles.sort()

# listfiles = listfiles[:1]

kk = np.zeros((224,224,3))

for i,filename in enumerate(tqdm(listfiles)):

    im1 = Image.open(path + filename)
    im1 = np.uint16(np.asarray(im1))
    # for j in range(3):
    # kk[:,:,0] = im1[0:224,0:224,0]/255
    # kk[:,:,1] = im1[0:224,0:224,1]/255
    # kk[:,:,2] = im1[0:224,0:224,2]/255

    kk[:,:,0] = im1[144:368,144:368,0]/255
    kk[:,:,1] = im1[144:368,144:368,1]/255
    kk[:,:,2] = im1[144:368,144:368,2]/255
    
    # kk = np.uint16(kk*255).astype(np.uint8)
    
    im = Image.fromarray((kk* 255).astype(np.uint8))
    
    # data = Image.fromarray(kk) 
    
    im.save(destpath+filename) 
    
    
    
# NewImg = np.uint16(kk)
    # im3 = color.rgb2lab(im2)
# print('Image size: ' + str(np.shape(im1)[0]))

# ImChOut=separatelab(ImRgb2lab,channel='L')
# cv.imwrite(destpath+filename, im)