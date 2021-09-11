# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 05:30:20 2021

@author: FourR
"""
##################################################
def check_NaN(df):
    #this function, check NaN value in the data frame and 
    #replace that with mean of column
    for col in df.columns:
        if any(df[col].isna()):
            df[col].fillna(df[col].mean(),inplace=True)
    return df
##################################################
def check_duplicate(df):
    #this function check duplicate value in dataframe and 
    #remove them
    if any(df.duplicated()):
        return df.drop_duplicates(df.columns)
##################################################
def append_data_frame(list_df):
    #in this function, we get list of data frame
    # and want to append them together
    import pandas as pd
    appended = pd.DataFrame()
    for df in list_df:
        appended= appended.append(df,ignore_index = True)
    return appended
##################################################