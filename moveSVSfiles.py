# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 11:19:44 2024

@author: Andres
"""
import cv2 as cv
from skimage import color

import numpy as np
import matplotlib.pyplot as plt

from os import listdir
from PIL import Image

import pandas as pd

sheetpath = 'C:/Users/Andres/Downloads/TCGA_Glioblastoma_WHO21_WSI_3.xlsx'

GBtable = pd.read_excel(sheetpath,sheet_name='GB_WT')


path = 'D:/HistoGBM/TCGA/wsi/'

downloadedfiles_list = listdir(path)
new_downloadedfiles_list = []


for filename in downloadedfiles_list:
    if filename[-3:]=='svs':
        print(filename)
        case = filename[:-15]
        new_downloadedfiles_list.append(case) 
        # print(case)
    #%%
    # print(case)

path2 = 'D:/HistoGBM/Discarted TCGA/WSI/'

downloadedfiles_list = listdir(path2)
new_downloadedfiles_list2 = []


for filename in downloadedfiles_list:
    if filename[-3:]=='svs':
        # print(filename)
        case = filename[:-15]
        new_downloadedfiles_list2.append(case) 
        # print(case)



downloadedfiles_list = new_downloadedfiles_list + new_downloadedfiles_list2
#%%

list_GBwt = list(GBtable.PatientID)

downloaded_yes_no = []
downloaded_disc = []

for GBTW in list_GBwt :
    
    if GBTW in downloadedfiles_list: 
        status = 'yes'
        print('yes')
    
    else:
        status = 'no'
        print('no')
        
    downloaded_yes_no.append(status)
    
for GBTW in list_GBwt :
        
    if GBTW in new_downloadedfiles_list2: 
        disc = 'yes'
        print('yes')
    
    else:
        disc = 'no'
        print('no')
        
    
    downloaded_disc.append(disc)
    
#%%

sheetpath2 = 'C:/Users/Andres/Downloads/TCGA_Glioblastoma_WHO21_WSI.xlsx'

GBtable.insert(2,"Downloaded", downloaded_yes_no, True)
GBtable.insert(3,"Discarted", downloaded_disc, True)

# GBtable.to_excel(sheetpath2, sheet_name='Available')


#%%
path = 'D:/HistoGBM/TCGA/mask/'

new_downloadedfiles_list = listdir(path)

#%%
new_downloadedfiles_list2 = []
new_downloadedfiles_list3 = []

for filename in new_downloadedfiles_list:
    # print(filename)
    if filename[-3:]=='png':
        # print(filename)
        case = filename[:-15]
        new_downloadedfiles_list2.append(case) 
        case2 = filename
        new_downloadedfiles_list3.append(case2) 

#%%
downloaded_list = [] 
listpatientID = list(GBtable['PatientID'])

for patientID in new_downloadedfiles_list2:
    
    if patientID in listpatientID: 
        disc = 1
        print('yes')
    
    else:
        disc = 0
        print('no')
        
    
    downloaded_list.append(disc)
    
    # print(patientID)
#%%
import shutil

# new = 'D:/HistoGBM/TCGA/wsi2/'+new_downloadedfiles_list3[i]
# old = 'D:/HistoGBM/TCGA/wsi/'+new_downloadedfiles_list3[i]

for i in range(len(downloaded_list)):

    if downloaded_list[i]==1:
        new = 'D:/HistoGBM/TCGA/mask2/'+new_downloadedfiles_list3[i]
        old = 'D:/HistoGBM/TCGA/mask/'+new_downloadedfiles_list3[i]
        shutil.move(old, new)
        


#%%


shutil.move("archivo.txt", "Documentos/archivo.txt")




