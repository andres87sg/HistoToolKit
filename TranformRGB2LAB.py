# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 19:37:53 2021

@author: Andres
"""

import cv2 as cv
from skimage import color
# from skimage import io, color
import numpy as np
import matplotlib.pyplot as plt

from os import listdir
from PIL import Image

# from skimage.color import rgb2hed, hed2rgb

#%% Función para generar una imagen correspondiente al Canal A del espacio LAB

def separatelab(lab,channel):
    
    # Normaliza min-max canal L    
    ch=0
    ChannelL=(lab[:,:,ch]-np.min(lab[:,:,ch]))/(np.max(lab[:,:,ch])-np.min(lab[:,:,ch]))
    
    # Normaliza min-max canal A
    ch=1
    # ChannelA=(lab[:,:,ch]-np.min(lab[:,:,ch]))/(np.max(lab[:,:,ch])-np.min(lab[:,:,ch]))
    ChannelA = (lab[:,:,ch]+86.185)/184.439
    # ChannelA=(lab[:,:,ch]-(-128))/(127-(-128))

    # Normaliza min-max canal B
    ch=2
    ChannelB=(lab[:,:,ch]-np.min(lab[:,:,ch]))/(np.max(lab[:,:,ch])-np.min(lab[:,:,ch]))

    # Crea una matriz del tamaño de la imagen de entrada lab
    NewImg=np.zeros(np.shape(lab))
    for i in range(3):
        # Guarda en la matríz NewImg el Canal A
        if channel == 'L':
            NewImg[:,:,i]=ChannelL
        if channel == 'A':
            NewImg[:,:,i]=ChannelA
        if channel == 'B':
            NewImg[:,:,i]=ChannelB
    
    NewImg= np.uint16(NewImg*255)

    return NewImg


path = 'D:/GBM_Project/Current_Experiments/MV_Patches/MV_896_raw_TCGA/MV/'
destpath = 'D:/GBM_Project/Current_Experiments/MV_Patches/MV_896_TCGA_ChA/'

# Image list
listfiles = listdir(path)
listfiles.sort()

# Convert RGB images to LAB space (Channel A)
for filename in listfiles:
    print(filename)
    im1 = Image.open(path + filename)
    im1 = np.asarray(im1)
    ImRgb2lab = color.rgb2lab(im1)
    
    ImChOut=separatelab(ImRgb2lab,channel='A')
    cv.imwrite(destpath+filename, ImChOut)


plt.figure(1)
plt.subplot(1,2,1)
plt.imshow(im1)
plt.axis('off')
plt.subplot(1,2,2)
plt.imshow(ImChOut)
plt.axis('off')


"""
# Convierte las imágenes originales en imagenes en el canal A
for filename in listfiles:
    print(filename)
    im1 = Image.open(path + filename)
    im1 = np.asarray(im1)
    # im1 = img_as_ubyte(im1)
    # matched = match_histograms(im1, reference, channel_axis=-1)
    # fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(8, 3),
    #                                 sharex=True, sharey=True)
    # for aa in (ax1, ax2, ax3):
    #     aa.set_axis_off()
    
    # ax1.imshow(im1)
    # ax1.set_title('Source')
    # ax2.imshow(reference)
    # ax2.set_title('Reference')
    # ax3.imshow(matched)
    # ax3.set_title('Matched')
    
    # plt.tight_layout()
    # plt.show()
    
    
    # ihc_hed = rgb2hed(im1)
    # null = np.zeros_like(ihc_hed[:, :, 0])
    # ihc_h = hed2rgb(np.stack((ihc_hed[:, :, 0], null, null), axis=-1))
    # ihc_e = hed2rgb(np.stack((null, ihc_hed[:, :, 1], null), axis=-1))
    # ihc_d = hed2rgb(np.stack((null, null, ihc_hed[:, :, 2]), axis=-1))
    # im1 = ihc_e.copy()
    
    # ImRgb2lab = color.rgb2lab(matched)
    ImRgb2lab = color.rgb2lab(im1)
    # footprint = disk(50)
    # img_eq = rank.equalize(im1[:,:,0], footprint=footprint)
    
    ImChOut=separatelab(ImRgb2lab,channel='A')
    cv.imwrite(destpath+filename, ImChOut)

"""