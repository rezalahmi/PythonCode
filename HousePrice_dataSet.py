#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df_housePrice = pd.read_csv('d:\housePrice.csv')
df_housePrice.head()


# In[2]:


df_housePrice.info()


# In[2]:


df_housePrice[df_housePrice.duplicated()]


# In[3]:


df_housePrice.drop_duplicates(inplace = True)


# In[4]:


df_housePrice[df_housePrice.duplicated()]


# In[6]:


df_housePrice.corr()


# In[5]:


df_housePrice.groupby(['Address']).mean()


# In[6]:


Address_meanPrice = df_housePrice.groupby(['Address'])['Price'].mean()
Address_meanPrice['Shahran']


# In[24]:


df_housePrice.head()


# In[7]:


df_housePrice['Address - MeanPrice'] = df_housePrice.groupby('Address')['Price'].transform('mean')


# In[8]:


df_housePrice.head()


# In[ ]:




