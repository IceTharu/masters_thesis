#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 14:58:45 2019

@author: thorsteinngj
"""

import pandas as pd
from collections import Counter
import numpy as np

df = pd.read_csv('/home/thorsteinngj/Documents/Skoli/Thesis/Dataframes/df_all_c_fips.csv')
df = df.drop(["Unnamed: 0","Unnamed: 0.1"],axis=1)
df_2 = df[pd.notnull(df.cem_country)]

df_two = pd.read_csv('/home/thorsteinngj/Documents/Skoli/Thesis/Dataframes/all_symbols.csv')
df_two = df_two.drop(["Unnamed: 0"],axis=1)
df_two = df_two.drop(["time_elapsed"],axis=1)
df5 = df_two.drop_duplicates(subset='grave_id', keep='first', inplace=False)

df3 = pd.merge(df_2,df5,on="grave_id")

df_2 = df3

df_usa = df_2[df_2.cem_country == 'USA']
df_row = df_2[df_2.cem_country != 'USA']

#%%

# Need to fix the missing FIPS values here. And also get a geojson map of Puerto Rico.

df_usa = df_usa[pd.notnull(df.fips)]
df_usa.fips = df_usa.fips.astype(int)

fips_codes = Counter(df_usa.fips)
countries = Counter(df_row.cem_country)

#%%

df_usa_2 = pd.DataFrame.from_dict(fips_codes, orient='index').reset_index()
df_usa_2 = df_usa_2.rename(columns={'index':'fips', 0:'number_of_people'})
df_usa_2["mean_age"] = float(0)

for i in range(len(df_usa_2)):
    df_usa_2.mean_age[i] = df_usa.age[df_usa.fips ==df_usa_2.fips[i]].mean()

#%%
df_row_2 = pd.DataFrame.from_dict(countries, orient='index').reset_index()
df_row_2 = df_row_2.rename(columns={'index':'cem_country', 0:'number_of_people'}) 
df_row_2["mean_age"] = float(0)

for i in range(len(df_row_2)):
    df_row_2.mean_age[i] = df_row.age[df_row.cem_country ==df_row_2.cem_country[i]].mean()   

    
#%%


df_2 = df.cem_country.dropna()
df_3 = df.fips.dropna()

countries = Counter(df_2)
fips = Counter(df_3)



df_new = pd.DataFrame.from_dict(countries, orient='index').reset_index()
df_new = df_new.rename(columns={'index':'country', 0:'count'})
df_fips_new = pd.DataFrame.from_dict(fips, orient='index').reset_index()
df_fips_new = df_fips_new.rename(columns={'index':'fips', 0:'count'})


df_fips_new.fips = df_fips_new.fips.astype(int)

#%%

countries = np.unique(df_2)

df_new["number_of_people"] = 0
df_new["mean_age"] = float(0)

for i in range(len(countries)):
    df_new.mean_age[i] = df.age[df_new.country ==countries[i]].mean()
