# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:30:08 2024

@author: Andres
"""
path = '/home/andres87sg/HD-GLIO/hd_glio/PruebaMRI2/' 
destpath = '/home/andres87sg/HD-GLIO/hd_glio/PruebaMRI2/'

filename_t1  = 'RAD-AI-CNS-TUMOR-0012_T1_SRI24_BiasCorrect.nii.gz'
filename_t1c = 'RAD-AI-CNS-TUMOR-0012_T1c_SRI24_SkullS_BiasCorrect.nii.gz'
filename_t2  = 'RAD-AI-CNS-TUMOR-0012_T2_SRI24_BiasCorrect.nii.gz'
filename_fl  = 'RAD-AI-CNS-TUMOR-0012_FLAIR_SRI24_BiasCorrect.nii.gz'

output_filename = 'Segmentation2.nii.gz'

a = 'hd_glio_predict '
b = ' -t1 '  + path + filename_t1 
c = ' -t1c ' + path + filename_t1c
d = ' -t2 ' + path + filename_t2
e = ' -flair ' + path + filename_fl
f = ' -o '
g = destpath + output_filename

print(a + b + c + d + e + f + g)

#%%
# perform brain extraction using HD-BET 

f = ' -o '


# print('hd-bet -i ' + path + filename_t1 + f + destpath + filename_t1)
# print('hd-bet -i ' + path + filename_t1c + f + destpath + filename_t1c)
# print('hd-bet -i ' + path + filename_t2 + f + destpath + filename_t2)
# print('hd-bet -i ' + path + filename_fl + f + destpath + filename_fl)
print('hd-bet -i ' + path + filename_t1)
print('hd-bet -i ' + path + filename_t1c)
print('hd-bet -i ' + path + filename_t2)
print('hd-bet -i ' + path + filename_fl)

#%%

## fsl5.0-flirt -in CT1_reorient_bet.nii.gz -ref T1_reorient_bet.nii.gz -out CT1_reorient_bet_reg.nii.gz -dof 6 -interp spline

print('fsl5.0-flirt -in' + path + filename_t2 + '-ref' + )

