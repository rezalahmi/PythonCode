# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
df_football = pd.read_csv(r'38.1 Football (Soccer) Teams - Null Values.csv')
df_football.head()
#Remove missing values and return new dataframe
df_fb_without_na = df_football.dropna()
#Fill NA/NaN values using the specified method
df_football['Champions League'].fillna(df_football['Champions League'].mean(),inplace=True)
df_football['League Champions'].fillna(df_football['League Champions'].mean(),inplace=True)
##if you you want to fill NaN value manully
df_ftball = pd.read_csv(r'38.1 Football (Soccer) Teams - Null Values.csv')
df_ftball['Champions League'].fillna(1,inplace=True)
df_ftball['League Champions'].fillna(20,inplace=True)