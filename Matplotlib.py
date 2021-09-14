#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df_food = pd.read_csv(r'D:\Udemy\Udemy - The Python Bootcamp Data Science, Analytics & Visualisation\8. Data Visualisation - Matplotlib\2.1 Food Orders.csv')
df_food.head(5)


# In[5]:


df_food['Day'].unique()


# In[6]:


df_food['Day'].replace({'Monday':'01 - Monday','Tuesday':'02 - Tuesday','Wednesday':'03 - Wednesday'                       , 'Thursday':'04 - Thursday','Friday':'05 - Friday','Saturday':'06 - Saturday'                       , 'Sunday':'07 - Sunday'},inplace = True)


# In[7]:


df_food['Total Amount'] = df_food['Quantity'] * df_food['Price Per Item']


# In[10]:


df_food.dtypes


# In[11]:


df_food.corr()


# In[ ]:




