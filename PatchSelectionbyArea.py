# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 09:58:17 2024

@author: Andres
"""

# -*- coding: utf-8 -*-
import cv2
import cv2 as cv
from skimage import color

import numpy as np
import matplotlib.pyplot as plt

from os import listdir
from PIL import Image
from tqdm import tqdm

#%%
def separatelab(lab,channel):
    
    # Normaliza min-max canal L    
    ch=0
    # ChannelL=(lab[:,:,ch]-np.min(lab[:,:,ch]))/(np.max(lab[:,:,ch])-np.min(lab[:,:,ch]))
    ChannelL = lab[:,:,ch]/100
    # Normaliza min-max canal A
    ch=1
    # ChannelA=(lab[:,:,ch]-np.min(lab[:,:,ch]))/(np.max(lab[:,:,ch])-np.min(lab[:,:,ch]))
    ChannelA = (lab[:,:,ch]+127)/255
    # ChannelA=(lab[:,:,ch]-(-128))/(127-(-128))

    # Normaliza min-max canal B
    ch=2
    ChannelB = (lab[:,:,ch]+127)/255
    # ChannelB=(lab[:,:,ch]-np.min(lab[:,:,ch]))/(np.max(lab[:,:,ch])-np.min(lab[:,:,ch]))

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


classes = ['CT','IC','MP','NE','PN','WM']
# classes = ['CT']
# for hallmark in classes:
  
for hallmark in classes:


    path = 'D:/BraTS2024_512/OriginalSamples/'
    destpath = 'D:/BraTS2024_512_Cleaned/OriginalSamples/'
    
    listfiles = listdir(path + hallmark + '/')
    listfiles.sort()
    
    for i,filename in enumerate(tqdm(listfiles)):

    # filename = 'BraTSPath_PN_0039375.png'
    
        im1 = Image.open(path + hallmark + '/' + filename)
        
        # im1 = np.asarray(im1)
        ImRgb2lab = color.rgb2lab(im1)
        
        ChL=separatelab(ImRgb2lab,channel='L')
        ChA=separatelab(ImRgb2lab,channel='A')
        ChB=separatelab(ImRgb2lab,channel='B')
        
        img = cv2.cvtColor(ChA, cv2.COLOR_BGR2GRAY)
        
        # ChB2 = (ChB).astype(np.uint8)
        
        _, binary_image = cv2.threshold(img, 0, 1, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        
        total_area = np.shape(binary_image)[0]**2
        calculated_tissue_area = np.sum(binary_image)
        
        percentage = calculated_tissue_area/total_area
        
        if percentage>=0.6:
            
            # print('It Works')
            im1.save(destpath + hallmark + '/' + filename) 



#%%

classes = ['CT','IC','MP','NE','PN','WM']
# classes = ['WM']
# for hallmark in classes:
    
    
    

for hallmark in classes:

    print(hallmark)
    path = 'D:/BraTS2024_256_Cleaned/OriginalSamples/'
    # path = 'D:/BraTS2024_256/OriginalSamples/'
    
    listfiles = listdir(path + hallmark + '/')
    listfiles.sort()
    print(len(listfiles))



# plt.imshow(binary_image)

# Display the original and segmented images
# cv2.imshow("Original Image", image)
# cv2.imshow("Segmented Image (Otsu)", binary_image)



# plt.imshow(ChB[:,:,0]/255<0.5)

#%%


im1 = Image.open("D:/BraTS2024_256_Cleaned/OriginalSamples/PN/BraTSPath_PN_0038295.png")

# im1 = np.asarray(im1)
ImRgb2lab = color.rgb2lab(im1)

ChL=separatelab(ImRgb2lab,channel='L')
ChA=separatelab(ImRgb2lab,channel='A')
ChB=separatelab(ImRgb2lab,channel='B')

img = cv2.cvtColor(ChL, cv2.COLOR_BGR2GRAY)

plt.imshow(img,)

#%%
# # D:/BraTS2024_New/AdditionalSamples/PN/
# path = 'D:/BraTS2024_New/AdditionalSamples/PN/'
# destpath = 'D:/BraTS2024_New/AdditionalSamples/PN2/'
# # path = 'D:/TCGA-GBM_Patches_PC_X/'
# # destpath = 'D:/MV/TCGA-GBM_Patches_MV_LAB/'
# # path = 'C:/Users/Andres/Desktop/patchextraction/PC_1792_raw_Jan2024/Train/PC/'
# # destpath = 'C:/Users/Andres/Desktop/patchextraction/PC_1792_ChL_Jan2024/Train/PC/'


# # Image list
# listfiles = listdir(path)
# listfiles.sort()

# #%%

# # listfiles = listfiles[:1]

# kk = np.zeros((224,224,3))

# for i,filename in enumerate(tqdm(listfiles)):

#     im1 = Image.open(path + filename)
#     im1 = np.uint16(np.asarray(im1))
#     # for j in range(3):
#     # kk[:,:,0] = im1[0:224,0:224,0]/255
#     # kk[:,:,1] = im1[0:224,0:224,1]/255
#     # kk[:,:,2] = im1[0:224,0:224,2]/255

#     kk[:,:,0] = im1[144:368,144:368,0]/255
#     kk[:,:,1] = im1[144:368,144:368,1]/255
#     kk[:,:,2] = im1[144:368,144:368,2]/255
    
#     # kk = np.uint16(kk*255).astype(np.uint8)
    
#     im = Image.fromarray((kk* 255).astype(np.uint8))
    
#     # data = Image.fromarray(kk) 
    
#     im.save(destpath+filename) 