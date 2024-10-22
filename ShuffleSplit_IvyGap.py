# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 16:06:38 2024

@author: Andres

Stratified Shuffle Split
https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedShuffleSplit.html

"""
import cv2 as cv
from skimage import color

import numpy as np
import matplotlib.pyplot as plt

from os import listdir
from PIL import Image

import pandas as pd

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

import sklearn
from sklearn.model_selection import (
    GroupKFold,
    GroupShuffleSplit,
    KFold,
    ShuffleSplit,
    StratifiedGroupKFold,
    StratifiedKFold,
    StratifiedShuffleSplit,
    TimeSeriesSplit,
)


sheetpath = 'C:/Users/Andres/Desktop/DataPartition.xlsx'

# GBtable = pd.read_excel(sheetpath,sheet_name='GB_WT_Clinical')
GBtable = pd.read_excel(sheetpath,sheet_name='CT_NE')

patient = GBtable['PatientID']
age = GBtable['Age']
wsi = GBtable['AvailableWSI']
#site = GBtable['Tissue Source Site']
#gender = GBtable['gender']

#data = {'Patient': patient, 'Age': age,'Gender': gender, 'Site':site}
data = {'Patient': patient, 'Age': age,'AvailableWSI':wsi}
df = pd.DataFrame(data=data)

#%%
agelist = []

for zz in age:
    agelist.append(zz) 
    
availablewsilist = []

for zz in wsi:
    availablewsilist.append(zz)

X = np.array(agelist,dtype=np.int16)
Y = np.array(availablewsilist,dtype=np.int16)


#%%

split = 0.80
StratifiedGroupKFold
sss= sklearn.model_selection.StratifiedShuffleSplit(n_splits=1, test_size=1-split, train_size=split, random_state=0)

#%%

ttt = sss.get_n_splits(X,Y)

# lll = sss.split(X, y)

#%%

for i, (train_index, test_index) in enumerate(sss.split(X, Y)):
    print(f"Fold {i}:")
    print(f"  Train: index={train_index}")
    print(f"  Test:  index={test_index}")


train = df.loc[train_index]
test = df.loc[test_index]

print('Train')
print(f"Median: {np.median(train['Age'])}")
print(f"Mean: {np.mean(train['Age'])}")
print(f"Std: {np.std(train['Age'])}")

print('Test')
print(f"Median: {np.median(test['Age'])}")
print(f"Mean: {np.mean(test['Age'])}")
print(f"Std: {np.std(test['Age'])}")

#$
#%%
import numpy as np  
from scipy import stats  

t_stat, p_val = stats.ttest_ind(test['Age'], train['Age'])  
# print("t-statistic = " + str(t_stat))  
print(f"p-value = {p_val}")
print(f"p-value = {t_stat}")


#%%
"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

from sklearn.model_selection import (
    GroupKFold,
    GroupShuffleSplit,
    KFold,
    ShuffleSplit,
    StratifiedGroupKFold,
    StratifiedKFold,
    StratifiedShuffleSplit,
    TimeSeriesSplit,
)

rng = np.random.RandomState(1338)
cmap_data = plt.cm.Paired
cmap_cv = plt.cm.coolwarm
n_splits = 4



#%%
# Generate the class/group data
n_points = 100
X = rng.randn(100, 10)

percentiles_classes = [0.1, 0.3, 0.6]
y = np.hstack([[ii] * int(100 * perc) for ii, perc in enumerate(percentiles_classes)])

# Generate uneven groups
group_prior = rng.dirichlet([2] * 10)
groups = np.repeat(np.arange(10), rng.multinomial(100, group_prior))


def visualize_groups(classes, groups, name):
    # Visualize dataset groups
    fig, ax = plt.subplots()
    ax.scatter(
        range(len(groups)),
        [0.5] * len(groups),
        c=groups,
        marker="_",
        lw=50,
        cmap=cmap_data,
    )
    ax.scatter(
        range(len(groups)),
        [3.5] * len(groups),
        c=classes,
        marker="_",
        lw=50,
        cmap=cmap_data,
    )
    ax.set(
        ylim=[-1, 5],
        yticks=[0.5, 3.5],
        yticklabels=["Data\ngroup", "Data\nclass"],
        xlabel="Sample index",
    )


visualize_groups(y, groups, "no groups")


#%%
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

from sklearn.model_selection import (
    GroupKFold,
    GroupShuffleSplit,
    KFold,
    ShuffleSplit,
    StratifiedGroupKFold,
    StratifiedKFold,
    StratifiedShuffleSplit,
    TimeSeriesSplit,
)

rng = np.random.RandomState(1338)
cmap_data = plt.cm.Paired
cmap_cv = plt.cm.coolwarm
n_splits = 4
# Generate the class/group data
n_points = 100
X = rng.randn(100, 10)

percentiles_classes = [0.1, 0.3, 0.6]
y1 = np.hstack([[ii] * int(100 * perc) for ii, perc in enumerate(percentiles_classes)])

#%%
sss = StratifiedShuffleSplit(n_splits=5, test_size=0.5, random_state=0)
sss.get_n_splits(X, y)

#%%

print(sss)
for i, (train_index, test_index) in enumerate(sss.split(X, y)):
    print(f"Fold {i}:")
    print(f"  Train: index={train_index}")
    print(f"  Test:  index={test_index}")


#%%

import matplotlib.pyplot as plt
import numpy as np

plt.hist(train['Age'], bins=10, color='skyblue', edgecolor='black')
 
# Adding labels and title
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Basic Histogram')
 
# Display the plot
plt.show()

#%%
print('Train')
print(f"Median: {np.median(train['Age'])}")
print(f"Mean: {np.mean(train['Age'])}")
print(f"Std: {np.std(train['Age'])}")

print('Test')
print(f"Median: {np.median(test['Age'])}")
print(f"Mean: {np.mean(test['Age'])}")
print(f"Std: {np.std(test['Age'])}")



# np.mean(test['Age'])
# np.std(train['Age'])



# print('Test')

# np.median(test['Age'])
# np.mean(train['Age'])
# np.std(test['Age'])
"""

