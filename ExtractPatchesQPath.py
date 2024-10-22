# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 16:51:36 2024

@author: Andres
"""

import numpy as np
import pandas as pd
import slideio
from PIL import Image
import tqdm 

# Allow processing of very large images by setting the maximum image pixels to None
Image.MAX_IMAGE_PIXELS = None

# Set the patch size
patch_size = 1024

# Define the Whole Slide Image (WSI) name
WSI_name = 'TCGA-06-0138-01Z-00-DX1'
print(WSI_name)

# Define the path to the WSI file
WSI_path = 'D:/HistoGBM/TCGA/wsi2/' + WSI_name + '.svs'

# Define the path to the annotations file
Annotation_path = 'D:/TCGA MV Patches/MV_CoordSegm_TCGA/' + WSI_name + '.geojson'

# Define the destination path for saving patches
Destination_path ='C:/Users/Andres/Desktop/Prueba_MV3/'

# Import the WSI using the slideio library
slide = slideio.open_slide(WSI_path,"SVS")
wsiscene = slide.get_scene(0)
wsiblock = wsiscene.read_block()
wsiblock = Image.fromarray(wsiblock, 'RGB')

# Find the position of the magnification information in the metadata
findmagpos = slide.raw_metadata.find('AppMag =')

# Extract the magnification value from the metadata
magnification = int(slide.raw_metadata[findmagpos+9:findmagpos+11])

# Print the magnification value
print('Magnification: ' + str(magnification) +'X')

# Adjust the patch size if the magnification is 40X
if magnification == 40:
    # print('magnification at 40X')
    patch_size = patch_size*2

#%%

# Import data from the GeoJSON annotations file
data = pd.read_json(Annotation_path)
corners = []

# Extract the corner coordinates of each annotation
for i in range(len(data)):
    
    first_point = data['features'][i]['geometry']
    coordinates = first_point['coordinates'][0]
    corner = coordinates[0]
    corners.append(corner)
    
print('Number of patches: ' + str(i+1))

#%%

# Iterate through each corner to create and save image patches
for i,corner in  enumerate(corners):
    # Define the bounding box for the cropped image (left, top, right, bottom)
    print(corner)
    patch = wsiblock.crop((corner[0],                 # Left
                           corner[1],                 # Top
                           corner[0] + patch_size,    # Right
                           corner[1] + patch_size))   # Bottom
    
    # Resize the patch if the magnification is 40X
    if magnification == 40:
        # print('magnification at 40X')
        newsize = (patch_size//2,patch_size//2)
        patch = patch.resize(newsize)
        
    # Save the patch as a PNG file
    patch.save(Destination_path + WSI_name + '_' +str(i).zfill(3) + '.png',format="PNG") 
