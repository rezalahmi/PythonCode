#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
df_housePrice = pd.read_csv('d:\housePrice.csv')
df_housePrice.head()


# In[4]:


df_housePrice.info()


# In[7]:


df_housePrice[df_housePrice.duplicated()]


# In[8]:


df_housePrice.drop_duplicates(inplace = True)


# In[10]:


df_housePrice[df_housePrice.duplicated()]


# In[11]:


df_housePrice.corr()


# In[ ]:




