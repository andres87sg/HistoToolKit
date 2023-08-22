# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 19:37:53 2021

@author: Andres
"""

import cv2 as cv
from skimage import io, color
import numpy as np
import matplotlib.pyplot as plt

from tqdm import tqdm
from os import listdir
from os.path import join
from PIL import Image

from skimage.color import rgb2hed, hed2rgb

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

#%%
# from skimage.filters import rank
# from skimage.morphology import disk
# from skimage.util import img_as_ubyte
from skimage.exposure import match_histograms
from skimage import data

path = 'D:/GBM_Project/Current_Experiments/MV_Patches/MV_896_raw_TCGA/MV/'
# path = 'C:/Users/Andres/Desktop/transformedimages/MV/'
# Directorio de destino
destpath = 'D:/GBM_Project/Current_Experiments/MV_Patches/MV_896_TCGA_ChA/'

# Lista de imagenes en el directorio
listfiles = listdir(path)
listfiles.sort()
#%%
# Referece patch for match histograms
# refpathc = False

# if refpatch == True:
#     refpath = 'D:/GBM_Project/Current_Experiments/MV_Patches/MV_896_raw/Testing/MV/W9-1-1-K.2.01_0004_MV.jpg'
#     reference = Image.open(refpath)
#     reference = np.asarray(reference)


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

# plt.imshow(ImChOut)

#%%

plt.figure(1)
plt.subplot(1,2,1)
plt.imshow(im1)
plt.axis('off')
plt.subplot(1,2,2)
plt.imshow(ImChOut)
plt.axis('off')
    
#%%


"""








#filename = 'C:/Users/Andres/Desktop/destino 11/Testing/PC/'
#name = 'W32-1-1-E.03_0000_PC.jpg'

#filename = 'C:/Users/Andres/Desktop/'

filename = 'C:/Users/Andres/Desktop/destino 16/MV/'
name = 'W5-1-1-K.2.06_0002_MV.jpg'


#img = cv.imread(filename)

rgb = io.imread(filename+name)
lab = color.rgb2lab(rgb)


red_ch = np.copy(rgb)
green_ch = np.copy(rgb)
blue_ch = np.copy(rgb)


L_ch = np.copy(lab)
A_ch = np.copy(lab)
B_ch = np.copy(lab)



red_ch[:,:,1]=0
red_ch[:,:,2]=0

green_ch[:,:,0]=0
green_ch[:,:,2]=0

blue_ch[:,:,0]=0
blue_ch[:,:,1]=0


plt.figure(1)
plt.subplot(2,3,1)
plt.imshow(red_ch)
plt.axis('off')
plt.subplot(2,3,2)
plt.imshow(green_ch)
plt.axis('off')
plt.subplot(2,3,3)
plt.imshow(blue_ch)
plt.axis('off')
           

plt.subplot(2,3,4), plt.title('L')
plt.axis('off')
plt.imshow(lab[:,:,0],cmap='gray')
plt.subplot(2,3,5), plt.title('A')
plt.axis('off')
plt.imshow(lab[:,:,1],cmap='gray')
plt.subplot(2,3,6), plt.title('B')
plt.axis('off')
plt.imshow(lab[:,:,2],cmap='gray')

#%%

plt.figure()
plt.imshow(lab[:,:,0],cmap='gray')
plt.axis('off')
plt.title('L*')

plt.figure()
plt.imshow(lab[:,:,1],cmap='gray')
plt.axis('off')
plt.title('A*')

plt.figure()
plt.imshow(lab[:,:,2],cmap='gray')
plt.axis('off')
plt.title('B*')


#%%
ch=0
pp=(lab[:,:,ch]-np.min(lab[:,:,ch]))/(np.max(lab[:,:,ch])-np.min(lab[:,:,ch]))

ch=1
qq=(lab[:,:,ch]-np.min(lab[:,:,ch]))/(np.max(lab[:,:,ch])-np.min(lab[:,:,ch]))

ch=2
rr=(lab[:,:,ch]-np.min(lab[:,:,ch]))/(np.max(lab[:,:,ch])-np.min(lab[:,:,ch]))




kk=np.zeros(np.shape(L_ch))
for i in range(3):
    kk[:,:,i]=qq


kk[:,:,2]=pp

ll=np.zeros(np.shape(kk[:,:,0]))



plt.imshow(kk)

#%%

from PIL import Image

data = np.uint16(kk*255)

img = Image.fromarray(data, 'RGB')

img.save('my.png')



#%%

import cv2         
import numpy as np  

imit= cv2.imread('kkz.jpg')


#%%

ret2,th2 = cv2.threshold(imit,0,255,cv2.THRESH_OTSU)


#%%

from skimage import data
from skimage.morphology import disk
from skimage.filters import threshold_otsu, rank
from skimage.util import img_as_ubyte

radius = 15
selem = disk(radius)

local_otsu = rank.otsu(img, selem)
threshold_global_otsu = threshold_otsu(img)
global_otsu = img >= threshold_global_otsu

#%%







# plt.imshow(nn)
# cv2.imwrite('kkz.jpg', nn)

"""


