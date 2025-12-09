# -*- coding: utf-8 -*-
# """
# Created on Thu Mar 13 04:51:31 2025

# @author: Andres
# """
# import matplotlib.pyplot as plt

# cero=sorted_unlabeledpool_df[sorted_unlabeledpool_df['label']==5]

# # Example data
# # classes = ['Class 1', 'Class 2', 'Class 3', 'Class 4', 'Class 5', 'Class 6']
# # entropy_values = [0.5, 0.7, 0.2, 0.9, 0.4, 0.6]
# x=cero['max_pred']
# y=cero['Score']
# # Create scatter plot
# plt.scatter(x, y,marker='.')
# plt.xlabel('Max_pred')
# plt.ylabel('Entropy')
# plt.title('Entropy of Six Classes')
# plt.show()

#%%

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# np.random.seed(1974)

# Generate Data
# num = 20
sorted_unlabeledpool_df2=sorted_unlabeledpool_df[sorted_unlabeledpool_df['Score']>0]

x=sorted_unlabeledpool_df2['max_pred']
y=sorted_unlabeledpool_df2['Score']
labels = sorted_unlabeledpool_df['label']
# x, y = np.random.random((2, num))
# labels = np.random.choice(['a', 'b', 'c'], num)
df = pd.DataFrame(dict(x=x, y=y, label=labels))

groups = df.groupby('label')

# Plot
fig, ax = plt.subplots()
ax.margins(0.05) # Optional, just adds 5% padding to the autoscaling

i=0

for name, group in groups:
    
    color=['g','b','r','k','#80BFFF','darkorange']
    print(color[i])
    ax.plot(group.x, group.y, marker='.',color =color[i] ,linestyle='', ms=3, label=name)
    i=i+1
ax.legend()

plt.ylabel('Entropy')
plt.xlabel('Predicted output')
plt.show()

#%%

import matplotlib.pyplot as plt

# Example data
classes = ['Class 1', 'Class 2', 'Class 3', 'Class 4', 'Class 5', 'Class 6']
entropy_values = [0.5, 0.7, 0.2, 0.9, 0.4, 0.6]
clusters = ['Cluster A', 'Cluster B', 'Cluster A', 'Cluster B', 'Cluster A', 'Cluster B']

# Assign colors to clusters
colors = {'Cluster A': 'blue', 'Cluster B': 'green'}

# Create scatter plot
plt.scatter(classes, entropy_values, c=[colors[cluster] for cluster in clusters])
for i, txt in enumerate(clusters):
    plt.annotate(txt, (classes[i], entropy_values[i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.xlabel('Classes')
plt.ylabel('Entropy')
plt.title('Entropy of Six Classes with Cluster Labels')
plt.show()

#%%

import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

# Example data
classes = ['Class 1', 'Class 2', 'Class 3', 'Class 4', 'Class 5', 'Class 6']
entropy_values = [0.5, 0.7, 0.2, 0.9, 0.4, 0.6]

# Combine classes and entropy values into a single array
data = np.array(entropy_values).reshape(-1, 1)

#%%

tsne = TSNE(n_components=2, random_state=0)
tsne_results = tsne.fit_transform(data)

#%%

import numpy as np

# Example data
data = np.array([
    [2.5, 2.4, 1.2],
    [0.5, 0.7, 0.8],
    [2.2, 2.9, 1.5],
    [1.9, 2.2, 1.1],
    [3.1, 3.0, 2.0],
    [2.3, 2.7, 1.3],
    [2.0, 1.6, 1.0],
    [1.0, 1.1, 0.5],
    [1.5, 1.6, 0.8],
    [1.1, 0.9, 0.4]
])

#%%
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
standardized_data = scaler.fit_transform(data)

#%%

from sklearn.decomposition import PCA

pca = PCA(n_components=2)  # Reduce to 2 components for visualization
pca_results = pca.fit_transform(standardized_data)

import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))
plt.scatter(pca_results[:, 0], pca_results[:, 1])

plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA Visualization')
plt.show()

#%%


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_excel('D:/tabla.xlsx')

#%%

df['Score'].to_list()

#%%
data = {
    'Class': df['label'].to_list(),
    'Value': df['Score'].to_list()
}
df = pd.DataFrame(data)

#%%

plt.figure(figsize=(10, 6))
sns.boxplot(x='Class', y='Value', data=df)
plt.title('Boxplot of Three Different Classes')
plt.show()

#%%

# # plot
# sns.set_style('ticks')
# fig, ax = plt.subplots()
# # the size of A4 paper
# fig.set_size_inches(11.7, 8.27)
# sns.violinplot(data=df, inner="points")    
# sns.despine()

#%%
# plt.figure(figsize=(20, 25))
plt.figure(figsize=(5, 7))
custom_palette = sns.color_palette(['g','b','r','#484848','#80BFFF','darkorange'])

sns.violinplot(data=df, x="Class", y="Value", inner="point",
               palette=custom_palette,
               width=0.8,linewidth=0.2)
plt.xticks(ticks=[0, 1, 2,3,4,5], labels=['CT', 'PN', 'MV','NE','IC','WM'])
plt.xlabel('')
plt.ylabel('Entropy')


plt.savefig('D:/boxplot.png') 