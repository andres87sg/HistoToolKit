# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 19:37:53 2021

@author: Andres
"""

# import cv2 as cv
# from skimage import io, color
# import numpy as np
import matplotlib.pyplot as plt

# D:/GBM_Project/Current_Experiments/MV_Patches/MV_896_ChA/Testing/

# Source Folder
img_path = 'D:/JournalExperiments/PC/TCGA/PC_1792_raw/Train2/PC/'
mask_path = 'D:/JournalExperiments/PC/TCGA/PC_1792_raw/Train2/PC_SG/'

# Destination folder
img_pathdest = 'C:/Users/Andres/Desktop/transformedimages/PC/'
mask_pathdest = 'C:/Users/Andres/Desktop/transformedimages/PC_SG/'

# Number of images to be created
num_imgs_augmented = 300

# Show images
showimage = False

# Image size
imsize = 224*8


import albumentations as A
from keras.preprocessing.image import ImageDataGenerator

def transform(image):
    transform = A.Compose([
        # A.HueSaturationValue (hue_shift_limit=0.01, sat_shift_limit=0.010, val_shift_limit=0.010, always_apply=True, p=0.5)
        # A.ColorJitter(brightness=2, contrast=0.02, saturation=0.02, hue=0.02, always_apply=True, p=0.5)
        # A.Normalize (max_pixel_value=1, always_apply=False, p=1.0)
        
        A.ToFloat(max_value=255,always_apply=True,p=1.0),
        # A.RandomContrast(always_apply=True, p=0.5, limit=1/255),
        A.RGBShift(always_apply=True, p=0.5, r_shift_limit=(0/255,70/255), g_shift_limit=(0,10/255), b_shift_limit=(10/255,100/255)),   
        # A.RandomBrightness (limit=(-10,50), always_apply=True, p=0.5)
        # A.HueSaturationValue(always_apply=True, p=0.7, hue_shift_limit=(-10,10), sat_shift_limit=(-5, 5), val_shift_limit=(-3, 3)),
        # A.RandomGamma(always_apply=True, p=0.5, gamma_limit=(100, 150), eps=1e-07), 
        # A.Blur(always_apply=False, p=0.5, blur_limit=(2, 4)),
        # A.RandomBrightnessContrast(always_apply=True, p=0.2, brightness_limit=(-2, 2), contrast_limit=(-2, 2), brightness_by_max=False),  
        # A.ChannelShuffle(always_apply=True, p=0.5),       
        # A.Rotate(always_apply=False, p=1.0, limit=(-90, 90), interpolation=4, border_mode=4, value=(0, 0, 0), mask_value=None),
        # A.VerticalFlip(always_apply=False, p=0.5),
        # A.HorizontalFlip(always_apply=False, p=0.5),
        #A.Downscale(always_apply=False, p=0.5, scale_min=0.5, scale_max=0.8999999761581421, interpolation=0),
    ])
    return transform(image=image)['image']




datagen = ImageDataGenerator(
                            # rescale=1./255,
                            preprocessing_function=transform,
                            
                            horizontal_flip=True,
                            vertical_flip=True,
                            rotation_range=45,
                            fill_mode='reflect',
                            
                                # preprocessing_function=transform 
                             )

datagen2 = ImageDataGenerator(
                            # rescale=1./255,
                            horizontal_flip=True,
                            vertical_flip=True,
                            rotation_range=45,
                            fill_mode='reflect', 
                             )

img_iterator = datagen.flow_from_directory(
                                        img_path,
                                        batch_size=1,
                                        target_size=(imsize , imsize),
                                        seed=1,
                                        # class_mode=None,
                                        save_to_dir=img_pathdest,
                                        save_prefix="DataAug",
                                        save_format='jpg',
                                    )

mask_iterator = datagen2.flow_from_directory(
                                        mask_path,
                                        batch_size=1,
                                        target_size=(imsize , imsize ),
                                        seed=1,
                                        # class_mode=None,
                                        save_to_dir= mask_pathdest,
                                        save_prefix="SG_DataAug",
                                        save_format='jpg',
                                    )

#%%

# print('Image No %i: ' %i + filename[:-4])
for i in range(num_imgs_augmented):
    print(f"Creating image image No {i+1} of {num_imgs_augmented}")
    
    img, label = img_iterator.next()
    mask, label2 = mask_iterator.next()    
    plt.figure()
    img_aux = img[0,:,:,:]
    if showimage == True:
        # plt.show()
        plt.subplot(1,2,1)
        plt.imshow(img_aux)
        plt.axis('off')
        plt.subplot(1,2,2)
        plt.imshow(mask[0])
        plt.axis('off')