# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 15:43:58 2024

@author: Andres
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt

from os import listdir

# Load images as greyscale but make main RGB so we can annotate in colour
seg  = cv2.imread('D:/JournalExperiments/PC/TCGA/PC_1792_raw/Test/PC_SG/SG_TCGA-02-0015_001.jpg',cv2.IMREAD_GRAYSCALE)
main = cv2.imread('D:/JournalExperiments/PC/TCGA/PC_1792_raw/Test/PC/TCGA-02-0015_001.jpg',cv2.IMREAD_COLOR)
# main = cv2.cvtColor(main,cv2.COLOR_GRAY2BGR)

# main = cv2.cvtColor(main, cv2.COLOR_BGR2RGB)

# from skimage import color
# result_image = color.label2rgb(seg, main,bg_color=(0,255,255))

from skimage import segmentation
result_image = segmentation.mark_boundaries(main, seg, mode='thick',color=(1,0,0),outline_color=(1,0,0))


font = cv2.FONT_HERSHEY_SIMPLEX 
  
# org 
org = (100, 100) 
  
# fontScale 
fontScale = 2
   
# Blue color in BGR 
color = (0, 0, 0) 
  
# Line thickness of 2 px 
thickness = 8
   
# Using cv2.putText() method 
zz = cv2.putText(result_image, 'Eso', org, font,  
                   fontScale, color,thickness, cv2.FILLED) 




plt.imshow(zz)
plt.axis('off')
# from PIL import Image
# img = Image.fromarray(result_image,'RGB')
# img = Image.fromarray(data, 'RGB')
# img.save('C:/Users/Andres/Desktop/MVPatches/result.png')

# kk = np.uint8(np.round(result_image*255))

result_image = np.uint8(np.round(zz*255))
# result_image = cv2.putText(result_image, 'OpenCV', cv2.LINE_AA) 

cv2.imwrite('C:/Users/Andres/Desktop/MVPatches/result.png',result_image) 

#%%
from skimage import segmentation
path = 'D:/JournalExperiments/PC/TCGA/PC_1792_raw/Train/PC/'

files = listdir(path)

for file in files:
    seg  = cv2.imread('D:/JournalExperiments/PC/TCGA/PC_1792_raw/Train/'+'PC_SG/'+'SG_'+file,cv2.IMREAD_GRAYSCALE)
    main = cv2.imread('D:/JournalExperiments/PC/TCGA/PC_1792_raw/Train/'+'PC/'+file,cv2.IMREAD_COLOR)
    result_image = segmentation.mark_boundaries(main, seg, mode='thick',color=(1,0,0),outline_color=(1,0,0))
    
    filename = file[:-4]
    
    zz = cv2.putText(result_image, filename, org, font,  
                       fontScale, color,thickness, cv2.LINE_AA) 
    
    # plt.figure()
    # plt.imshow(result_image)
    result_image = np.uint8(np.round(zz*255))
    cv2.imwrite('D:/X/'+'NSG_'+file,result_image) 
    

#%%
# # Dictionary giving RGB colour for label (segment label) - label 1 in red, label 2 in yellow
# RGBforLabel = { 1:(0,0,255), 2:(0,255,255) }

# # Find external contours
# contours,_ = cv2.findContours(seg,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

# #%%


# #%%

# # Iterate over all contours
# for i,c in enumerate(contours):
#     # Find mean colour inside this contour by doing a masked mean
#     mask = np.zeros(seg.shape, np.uint8)
#     cv2.drawContours(mask,[c],-1,255, -1)
#     # DEBUG: cv2.imwrite(f"mask-{i}.png",mask)
#     mean,_,_,_ = cv2.mean(seg, mask=mask)
#     # DEBUG: print(f"i: {i}, mean: {mean}")

#     # Get appropriate colour for this label
#     label = 2 if mean > 1.0 else 1
#     colour = RGBforLabel.get(label)
#     # DEBUG: print(f"Colour: {colour}")

#     # Outline contour in that colour on main image, line thickness=1
#     cv2.drawContours(main,[c],-1,colour,1)
    
    
# cv2.imwrite('C:/Users/Andres/Desktop/MVPatches/result.png',main) 