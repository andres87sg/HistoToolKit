# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 17:51:19 2024

@author: Andres
"""

# -*- coding: utf-8 -*-
import cv2 as cv
from skimage import color

import numpy as np
import matplotlib.pyplot as plt

from os import listdir
from PIL import Image
from tqdm import tqdm

from PIL import PngImagePlugin
LARGE_ENOUGH_NUMBER = 100
PngImagePlugin.MAX_TEXT_CHUNK = LARGE_ENOUGH_NUMBER * (1024**2)
# D:/BraTS2024_New/AdditionalSamples/PN/
# 'C:/Users/Andres/Desktop/CT/Testing/'

path = 'D:/BraTS2024_256_Cleaned/AdditionalSamples/'
destpath = 'D:/BraTS2024_New/OriginalSamples/'

# destpath = 'D:/Users/Andres/Desktop/Eso/'
# path = 'D:/TCGA-GBM_Patches_PC_X/'
# destpath = 'D:/MV/TCGA-GBM_Patches_MV_LAB/'
# path = 'C:/Users/Andres/Desktop/patchextraction/PC_1792_raw_Jan2024/Train/PC/'
# destpath = 'C:/Users/Andres/Desktop/patchextraction/PC_1792_ChL_Jan2024/Train/PC/'

# Image list
listfiles = listdir(path)
listfiles.sort()


#%%
# listfiles = listfiles[:1]

newsize = (256,256)

classes = ['CT','IC','MP','NE','PN','WM']
# classes = ['PN','WM']
# for hallmark in classes:
    
    
    

#%%
meanlist0 = [] 
meanlist1 = []
meanlist2 = []
stdlist0 = [] 
stdlist1 = []
stdlist2 = []

for hallmark in classes:
    
    listfiles = listdir(path + hallmark + '/')
    listfiles.sort()
 
    
    for i,filename in enumerate(tqdm(listfiles)):
        
        # a=0
    
        imX = Image.open(path + hallmark + '/' + filename)
        
        # for ch in range(3):
        
        im0 = np.array(imX)[:,:,0]/255
        im1 = np.array(imX)[:,:,1]/255
        im2 = np.array(imX)[:,:,2]/255
        
        meanlist0.append(np.mean(im0))
        stdlist0.append(np.std(im0))
        
        meanlist1.append(np.mean(im1))
        stdlist1.append(np.std(im1))

        meanlist2.append(np.mean(im2))
        stdlist2.append(np.std(im2))

        
        
        
        
        # im2 = im1.resize((256,256))
        # im2 = np.uint16(np.asarray(im2))
        
        # kk = im1
        # kk = Image.fromarray(im2)
        
        # im = Image.fromarray((kk).astype(np.uint8))
        
        
        # im2.save(destpath + hallmark + '/' + filename) 
    
    
    
# NewImg = np.uint16(kk)
    # im3 = color.rgb2lab(im2)
# print('Image size: ' + str(np.shape(im1)[0]))

# ImChOut=separatelab(ImRgb2lab,channel='L')
# cv.imwrite(destpath+filename, im)