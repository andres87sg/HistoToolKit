# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 19:37:53 2021

@author: Andres
"""

import cv2 as cv
from skimage import color

import numpy as np
import matplotlib.pyplot as plt

from os import listdir
from PIL import Image

from tqdm import tqdm


# Función para generar una imagen correspondiente al Canal A del espacio LAB
#%%

def separatelab(lab, channel):
    # Normalize channel L
    ChannelL = lab[:, :, 0] / 100
    
    # Normalize channel A
    # ChannelA = (lab[:, :, 1] + 86.185) / 184.439
    ChannelA = (lab[:, :, 1] + 127) / 255
    
    # Normalize channel B
    ChannelB = (lab[:, :, 2] - lab[:, :, 2].min()) / (lab[:, :, 2].max() - lab[:, :, 2].min())
    
    # Create a new image matrix
    NewImg = np.zeros_like(lab)
    
    # Assign the selected channel to all layers
    if channel == 'L':
        NewImg[:, :, :] = ChannelL[:, :, None]
    elif channel == 'A':
        NewImg[:, :, :] = ChannelA[:, :, None]
    elif channel == 'B':
        NewImg[:, :, :] = ChannelB[:, :, None]
    
    # Scale the new image to 0-255 and convert to uint16
    NewImg = np.uint16(NewImg * 255)
    
    return NewImg

#%%

#
# def separatelab(lab,channel):
    
#     # Normaliza min-max canal L    
#     ch=0
#     # ChannelL=(lab[:,:,ch]-np.min(lab[:,:,ch]))/(np.max(lab[:,:,ch])-np.min(lab[:,:,ch]))
#     ChannelL = lab[:,:,ch]/100
#     # Normaliza min-max canal A
#     ch=1
#     # ChannelA=(lab[:,:,ch]-np.min(lab[:,:,ch]))/(np.max(lab[:,:,ch])-np.min(lab[:,:,ch]))
#     ChannelA = (lab[:,:,ch]+86.185)/184.439
#     # ChannelA=(lab[:,:,ch]-(-128))/(127-(-128))

#     # Normaliza min-max canal B
#     ch=2
#     ChannelB=(lab[:,:,ch]-np.min(lab[:,:,ch]))/(np.max(lab[:,:,ch])-np.min(lab[:,:,ch]))

#     # Crea una matriz del tamaño de la imagen de entrada lab
#     NewImg=np.zeros(np.shape(lab))
#     for i in range(3):
#         # Guarda en la matríz NewImg el Canal A
#         if channel == 'L':
#             NewImg[:,:,i]=ChannelL
#         if channel == 'A':
#             NewImg[:,:,i]=ChannelA
#         if channel == 'B':
#             NewImg[:,:,i]=ChannelB
    
#     NewImg= np.uint16(NewImg*255)

#     return NewImg

#%%
# D:/JournalExperiments/PC/TCGA2/PC_1792_raw/Train/PC/
# path = 'D:/GBM_Project/Current_Experiments/MV_Patches/MV_896_raw_TCGA/MV/'
# destpath = 'D:/GBM_Project/Current_Experiments/MV_Patches/MV_896_TCGA_ChA/'

# D:/GBM_Project/Current_Experiments/MV_Patches/MV_896_raw_Aug2023/Training/MV/
# path = 'D:/GBM_Project/Current_Experiments/MV_Patches/MV_896_raw_Aug2023/Training/MV/'
# destpath = 'D:/GBM_Project/Current_Experiments/MV_Patches/MV_896_ChA_Aug2023/Training/MV/'
# path = 'D:/GBM_Project/Current_Experiments/PC_Patches/PC_1792_raw_Aug2023/Testing/PC/'
# destpath = 'D:/GBM_Project/Current_Experiments/PC_Patches/PC_1792_ChL_Aug2023/Testing/PC/'
# path = 'D:/MV/TCGA-GBM_Patches_MV/'
# path = 'D:/JournalExperiments/PC/TCGA_Redist/PC_1792_raw/Test/PC/'
# destpath = 'D:/JournalExperiments/PC/TCGA_Redist/PC_1792_ChL/Test/PC/'
# path = 'D:/TCGA-GBM_Patches_PC_X/'
# destpath = 'D:/MV/TCGA-GBM_Patches_MV_LAB/'
# path = 'C:/Users/Andres/Desktop/patchextraction/PC_1792_raw_Jan2024/Train/PC/'
# destpath = 'C:/Users/Andres/Desktop/patchextraction/PC_1792_ChL_Jan2024/Train/PC/'

path = 'D:/TCGA PC Patches/PC_IvyGap/PC/'
destpath = 'D:/TCGA PC Patches/PC_IvyGap/PC_patches_LAB/'



# Image list
listfiles = listdir(path)
listfiles.sort()

#%%
# Convert RGB images to LAB space (Channel A)
for i,filename in enumerate(tqdm(listfiles)):
    # print('Image No %i: ' %i + filename[:-4])
    # print(i)
    im1 = Image.open(path + filename)
    im1 = np.asarray(im1)
    ImRgb2lab = color.rgb2lab(im1)
    # print('Image size: ' + str(np.shape(im1)[0]))
    
    ImChOut=separatelab(ImRgb2lab,channel='L')
    # cv.imwrite(destpath+filename, ImChOut)
    
    # im = Image.fromarray((ImChOut* 255).astype(np.uint8))
    im = Image.fromarray((ImChOut).astype(np.uint8))
    im.save(destpath+filename) 
    
#%%

showfigure = False
    
if showfigure==True:

    plt.figure(1)
    plt.subplot(1,2,1)
    plt.title("H&E")
    plt.imshow(im1)
    plt.axis('off')
    plt.subplot(1,2,2)
    plt.imshow(ImChOut)
    plt.title("Channel A")
    plt.axis('off')

#%%
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