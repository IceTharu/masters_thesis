#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 22:17:59 2019

@author: thorsteinngj
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import seaborn as sn

df_g = pd.read_csv('/home/thorsteinngj/Documents/Skoli/Thesis/Dataframes/df_germany_interest.csv')
df_g["sign"] = 0
df_g["no_sign"] = 0

for i in range(len(df_g)):
    if df_g.bible[i] == 1 or df_g.dove[i] == 1 or df_g.praying[i] == 1 or df_g.cross[i] == 1 or df_g.angel[i] == 1 or df_g.fish[i] == 1 or df_g.lamb[i] == 1 or df_g.verbal_relig[i] or df_g.other_religious[i]:
        df_g.sign[i] = 1
        df_g.no_sign[i] = 0
    else:
        df_g.sign[i] = 0
        df_g.no_sign[i] = 1
    
df_g.fips = df_g.fips.astype(int)
#%%

def new_dataframe_maker(df5):
    from collections import Counter
    
    df_three = pd.read_csv('/home/thorsteinngj/Documents/Skoli/Thesis/Dataframes/county_reladh_copenhagen.csv')

    
    fips_codes = np.unique(df5.fips)
    numb_fips = Counter(df5.fips)
    
    df_new = pd.DataFrame(np.unique(df5.fips), columns = ['fips'])
    df_new["number_of_people"] = 0
    df_new["mean_age"] = float(0)
    df_new["number_sign"] = 0
    df_new["median_sign"] = float(0)
    df_new["number_nosign"] = 0
    df_new["median_nosign"] = float(0)
    df_new["pct_symbol"] = float(0)
    df_new["pct_group_rel"] = 0
    df_new["pct_group_sym"] = 0
    df_new["rel_adh"] = float(0)
    
    for i in range(len(fips_codes)):
        df_new.number_of_people[i] = list(numb_fips.values())[i]
        df_new.mean_age[i] = df5.age[df5.fips ==fips_codes[i]].mean()
        df_new.median_sign[i] = df5.age[(df5.fips == fips_codes[i]) & (df5.sign == 1)].median()
        df_new.number_sign[i] = len(df5.age[(df5.fips == fips_codes[i]) & (df5.sign == 1)])
        df_new.median_nosign[i] = df5.age[(df5.fips == fips_codes[i]) & (df5.no_sign == 1)].median()
        df_new.number_nosign[i] = len(df5.age[(df5.fips == fips_codes[i]) & (df5.no_sign == 1)])
        df_new.rel_adh[i] = df_three.rel_adh[df_three.fip == df_new.fips[i]]
    
            
    for i in range(len(df_new)):
        df_new.number_of_people[i] = df_new.number_sign[i]+df_new.number_nosign[i]
        df_new.pct_symbol[i] = df_new.number_sign[i]/df_new.number_of_people[i]
    
    
    for i in range(len(df_new)):
        for j in np.arange(0,140,10):
            if df_new.rel_adh[i] >= j:
                df_new.pct_group_rel[i] =  int(j)
                
    for i in range(len(df_new)):
        for j in np.arange(0,140,10):
            if df_new.pct_symbol[i] >= j/100:
                df_new.pct_group_sym[i] =  int(j)
                
    
    return df_new

df_new_g = new_dataframe_maker(df_g)

#%%

def old_df_group_adding(df5,df_new):
    df6 = df5
    df6["group_rel"] = 0
    df6["group_sym"] = 0
    for i in range(len(df6)):
        df6.group_rel[i] = df_new.pct_group_rel[df_new.fips == df5.fips[i]]
    for i in range(len(df6)):
        df6.group_sym[i] = df_new.pct_group_sym[df_new.fips == df5.fips[i]]    
    
    df7 = df6[df6.sign == 1]
    df8 = df6[df6.no_sign == 1]
    
    return df7, df8

df7_g,df8_g = old_df_group_adding(df_g,df_new_g)

#%%

df7_g.boxplot(column='age',by='group_rel')
plt.title('Age reached for gravestones which have religious symbols, done by hand')
plt.ylabel('Age')
plt.xlabel('Religious adherency percentage')
plt.suptitle('')
plt.show()
df8_g.boxplot(column='age',by='group_rel')
plt.title('Age reached by for gravestones which don\'t have religious symbols, done by hand')
plt.ylabel('Age')
plt.xlabel('Religious adherency percentage')
plt.suptitle('')
plt.show()

#%%

df7_g.boxplot(column='age',by='group_sym')
plt.title('Age reached for gravestones which have religious symbols, done by hand')
plt.ylabel('Age')
plt.xlabel('Symbol percentage')
plt.suptitle('')
plt.show()
df8_g.boxplot(column='age',by='group_sym')
plt.title('Age reached by for gravestones which don\'t have religious symbols, done by hand')
plt.ylabel('Age')
plt.xlabel('Symbol percentage')
plt.suptitle('')
plt.show()