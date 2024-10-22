# -*- coding: utf-8 -*-
"""
Created on Tue May 21 23:47:56 2024

@author: Andres
https://www.synapse.org/#!Synapse:syn59761935
"""

import synapseclient 
import synapseutils
# syn = synapseclient.Synapse()
# syn = synapseclient.login(authToken="eyJ0eXAiOiJKV1QiLCJraWQiOiJXN05OOldMSlQ6SjVSSzpMN1RMOlQ3TDc6M1ZYNjpKRU9VOjY0NFI6VTNJWDo1S1oyOjdaQ0s6RlBUSCIsImFsZyI6IlJTMjU2In0.eyJhY2Nlc3MiOnsic2NvcGUiOlsidmlldyIsImRvd25sb2FkIl0sIm9pZGNfY2xhaW1zIjp7fX0sInRva2VuX3R5cGUiOiJQRVJTT05BTF9BQ0NFU1NfVE9LRU4iLCJpc3MiOiJodHRwczovL3JlcG8tcHJvZC5wcm9kLnNhZ2ViYXNlLm9yZy9hdXRoL3YxIiwiYXVkIjoiMCIsIm5iZiI6MTcxNjM1NDUwMCwiaWF0IjoxNzE2MzU0NTAwLCJqdGkiOiI4MjY2Iiwic3ViIjoiMzUwNDAzNCJ9.jRhCZqRHRxUVJ4BI93HsF7CJg5gWSCGbYlv22IxpimEymJw6H13YXwENIHDYA3RDCVlEq38IWV1abK70_B4h-lzQtBC8QeNAdPmpnxgJyn0ivwev8m-Pac8mQp6IbAF_WxasqrW4YDK7nt1XUSy8P03sRmLd9RqRzVHix7f3Uz2abNnD1rWo6mUEW3wJoGo_YCziSWzw8ortZ7qcoE5me_ajmqIp3Kldh1eK1exb4YIIYZQaTcn2ytSf0hkVIT0hUf54CgcVGSOiz72RQDjxXlrOwNacf_1fugWkJlfi8b1vdTaPvxPB-KCXE4SkJRLmXd6zeryLe5Uqj8SIrUCqHQ")
# files = synapseutils.syncFromSynapse(syn, ' syn58894466')


syn = synapseclient.Synapse() 
syn.login(authToken="eyJ0eXAiOiJKV1QiLCJraWQiOiJXN05OOldMSlQ6SjVSSzpMN1RMOlQ3TDc6M1ZYNjpKRU9VOjY0NFI6VTNJWDo1S1oyOjdaQ0s6RlBUSCIsImFsZyI6IlJTMjU2In0.eyJhY2Nlc3MiOnsic2NvcGUiOlsidmlldyIsImRvd25sb2FkIl0sIm9pZGNfY2xhaW1zIjp7fX0sInRva2VuX3R5cGUiOiJQRVJTT05BTF9BQ0NFU1NfVE9LRU4iLCJpc3MiOiJodHRwczovL3JlcG8tcHJvZC5wcm9kLnNhZ2ViYXNlLm9yZy9hdXRoL3YxIiwiYXVkIjoiMCIsIm5iZiI6MTcxNjM1NDUwMCwiaWF0IjoxNzE2MzU0NTAwLCJqdGkiOiI4MjY2Iiwic3ViIjoiMzUwNDAzNCJ9.jRhCZqRHRxUVJ4BI93HsF7CJg5gWSCGbYlv22IxpimEymJw6H13YXwENIHDYA3RDCVlEq38IWV1abK70_B4h-lzQtBC8QeNAdPmpnxgJyn0ivwev8m-Pac8mQp6IbAF_WxasqrW4YDK7nt1XUSy8P03sRmLd9RqRzVHix7f3Uz2abNnD1rWo6mUEW3wJoGo_YCziSWzw8ortZ7qcoE5me_ajmqIp3Kldh1eK1exb4YIIYZQaTcn2ytSf0hkVIT0hUf54CgcVGSOiz72RQDjxXlrOwNacf_1fugWkJlfi8b1vdTaPvxPB-KCXE4SkJRLmXd6zeryLe5Uqj8SIrUCqHQ") 
files = synapseutils.syncFromSynapse(syn,'syn58894466') 

#%%

import synapseclient 
import synapseutils 

syn = synapseclient.Synapse() 
syn.login(authToken="eyJ0eXAiOiJKV1QiLCJraWQiOiJXN05OOldMSlQ6SjVSSzpMN1RMOlQ3TDc6M1ZYNjpKRU9VOjY0NFI6VTNJWDo1S1oyOjdaQ0s6RlBUSCIsImFsZyI6IlJTMjU2In0.eyJhY2Nlc3MiOnsic2NvcGUiOlsidmlldyIsImRvd25sb2FkIl0sIm9pZGNfY2xhaW1zIjp7fX0sInRva2VuX3R5cGUiOiJQRVJTT05BTF9BQ0NFU1NfVE9LRU4iLCJpc3MiOiJodHRwczovL3JlcG8tcHJvZC5wcm9kLnNhZ2ViYXNlLm9yZy9hdXRoL3YxIiwiYXVkIjoiMCIsIm5iZiI6MTcxNjM1NDUwMCwiaWF0IjoxNzE2MzU0NTAwLCJqdGkiOiI4MjY2Iiwic3ViIjoiMzUwNDAzNCJ9.jRhCZqRHRxUVJ4BI93HsF7CJg5gWSCGbYlv22IxpimEymJw6H13YXwENIHDYA3RDCVlEq38IWV1abK70_B4h-lzQtBC8QeNAdPmpnxgJyn0ivwev8m-Pac8mQp6IbAF_WxasqrW4YDK7nt1XUSy8P03sRmLd9RqRzVHix7f3Uz2abNnD1rWo6mUEW3wJoGo_YCziSWzw8ortZ7qcoE5me_ajmqIp3Kldh1eK1exb4YIIYZQaTcn2ytSf0hkVIT0hUf54CgcVGSOiz72RQDjxXlrOwNacf_1fugWkJlfi8b1vdTaPvxPB-KCXE4SkJRLmXd6zeryLe5Uqj8SIrUCqHQ") 
files = synapseutils.syncFromSynapse(syn, 'syn59761935') 



#%%
for f in files:
    print(f.path)
    
#%%

# syn.get("syn2390898", downloadLocation="C:/Users/Andres/Documents/Desktop/ABC/")    
    


#%%

project_id = project.id
fileview = EntityViewSchema(
    name='MyTable',
    parent=project_id,
    scopes=[project_id]
)
fileview_ent = syn.store(fileview)

#%%

import os
from synapseclient.models import (
    Folder,
    Project,
)
import synapseclient

syn = synapseclient.Synapse()

#%%

DIRECTORY_TO_SYNC_PROJECT_TO = os.path.expanduser("C:/Users/Andres/Desktop/CT/")
FOLDER_NAME_TO_SYNC = "experiment_notes"
DIRECTORY_TO_SYNC_FOLDER_TO = os.path.join(
    DIRECTORY_TO_SYNC_PROJECT_TO, FOLDER_NAME_TO_SYNC
)

#%%
project = Project(name="My uniquely named project about Alzheimer's Disease")

#%%

# We'll set the `if_collision` to `keep.local` so that we don't overwrite any files
project.sync_from_synapse(path=DIRECTORY_TO_SYNC_PROJECT_TO, if_collision="keep.local")

# Print out the contents of the directory where the data was synced to
# Explore the directory to see the contents have been recursively synced.
print(os.listdir(DIRECTORY_TO_SYNC_PROJECT_TO))