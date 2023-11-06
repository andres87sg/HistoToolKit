# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 10:44:15 2023

@author: Andres

EN: Copy patches randomly

ES: Copia los parches aleatoriamente

"""

import cv2 as cv
from skimage import color

import numpy as np
import matplotlib.pyplot as plt

from os import listdir
from PIL import Image
import random
import shutil

path = 'C:/Users/Andres/Desktop/PatchExtractionCT_CPTAC/NE/'
destpath = 'C:/Users/Andres/Desktop/PatchExtractionCT_CPTAC/Testing/NE/'
# destpath2 = 'D:/TCGA-GBM_Patches/NE/SG/'


listfiles = listdir(path)
listfiles_orig = listfiles.copy()
listfiles.sort()
random.shuffle(listfiles)

for ind in range(2000):
    src = path + listfiles[ind]
    dst = destpath + listfiles[ind]
    shutil.copyfile(src, dst)



