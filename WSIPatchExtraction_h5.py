"""
Note: WSI Patch extraction using coordinates from h5 file 
"""

import math
import numpy as np
import slideio
from PIL import Image
import os

import pandas as pd
from matplotlib import pyplot as plt
import h5py    
import numpy as np    

"""
Read WSI file - svs file
"""

path = 'C:/Users/Andres/Desktop/C3L-00189-30/'  # Origin path
wsifile = 'C3L-00189-30.svs'                    # WSI filename
destpath = 'C:/Users/Andres/Desktop/'           # Destination folder

slide = slideio.open_slide(path+wsifile,"SVS")
wsiscene = slide.get_scene(0)

# Read block WSI
wsiblock = wsiscene.read_block()

# Conver WSI to array
wsiblock = Image.fromarray(wsiblock, 'RGB')

"""
Read h5 file - Coordinates
"""

h5file = 'C3L-00189-30.h5'
f1 = h5py.File(path + h5file ,'r+')   

# Extract and transfor coordinates from h5 file to pandas dataframe
listcoordinates = pd.DataFrame(np.array(h5py.File(path + h5file)['coords']))

# Max. number of patches
num_patches = 3

for ind in range(num_patches):
    
    indcoord = np.array(listcoordinates.loc[ind])
    
    # Top and left patch coordinates
    top = indcoord[1]
    left = indcoord[0]
    patchsize = 224
    
    # Extracting patch from original WSI
    WSIpatch=wsiblock.crop((left,top,left+patchsize,top+patchsize))
    
    # Save patch (Optional)
    savefile = "Patch_"+ str(ind).zfill(3) + '.jpg'
    WSIpatch.save(destpath + savefile)
    
    plt.figure()
    plt.imshow(WSIpatch)
    plt.axis('off')
    plt.title('H&E Patch')
    