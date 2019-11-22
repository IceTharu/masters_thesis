#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 13:24:09 2019

@author: thorsteinngj
"""

import pandas as pd
import os
from tqdm import tqdm
import shutil

df = pd.read_csv('/home/thorsteinngj/Documents/Skoli/Thesis/copenhagen_export_graves.csv')


def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

pics = []
for file in files("/home/thorsteinngj/Documents/Skoli/Thesis/Code/Pictures/"):
    pics.append(file)
    #print (file)
    

#%%

sep = '.'
#rest = int(pics[0].split(sep,1)[0])
new_pics = []
for i in range(len(pics)):
    pics[i] = pics[i].split(sep,1)[0]
    pics[i] = int(pics[i])
    i +=1

#%%
my_df = []
for i in tqdm(range(len(pics))):
    for j in range(len(df)):
        if pics[i] == df['graveid'][j]:
            my_df.append(df.iloc[j])
    
my_df = pd.DataFrame(my_df)

#%%

#Crosses
for j in range(len(df)):
    if df['dove'][j] == 1:
        shutil.copy("/home/thorsteinngj/Documents/Skoli/Thesis/Code/Pictures/"+str(int(df['graveid'][j]))+".jpg", "/home/thorsteinngj/Documents/Skoli/Thesis/Code/Pictures/Dove/"+str(int(df['graveid'][j]))+".jpg")
        #os.rename("/home/thorsteinngj/Documents/Skoli/Thesis/Code/Pictures/"+str(int(df['graveid'][j])+".jpg"), "/home/thorsteinngj/Documents/Skoli/Thesis/Code/Pictures/Cross"+str(int(df['graveid'][j])+".jpg"))