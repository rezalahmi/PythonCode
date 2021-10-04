#!/usr/bin/env python
# coding: utf-8

# In[1]:


#with this command, you can open the file
with open('titanic.csv') as f:
    text = f.readlines()


# In[2]:


text


# In[3]:


import pandas as pd


# In[4]:


pd.read_csv(r'titanic.csv')


# In[5]:


#if you want to add index to data frame, you can use index_col to define them
pd.read_csv(r'titanic.csv', index_col='pclass')


# In[7]:


#pandas by defual read the first row as a Header, 
#you can change it by header parameter
pd.read_csv(r'titanic.csv', header=None)


# In[10]:


#if you want to rename the names of columnm use the names parameters
pd.read_csv(r'titanic.csv',names=['alive','class','gender'                                  ,'age','sibsp','parch','price','emb','deck'])


# In[11]:


#with the usecols parameters, you can select columns to add to the data frames
pd.read_csv(r'titanic.csv',usecols=['survived','sex','pclass'])


# In[12]:


pd.read_csv(r'titanic_raw.csv')


# In[16]:


#if you consider the raw data set,
#you have metha data in first and end of the data set, 
#so you can don't read them with skiprow and skipfooter
pd.read_csv(r'titanic_raw.csv',skiprows=3,skipfooter=2)


# In[18]:


#we don't have header, so
pd.read_csv(r'titanic_raw.csv',skiprows=3,skipfooter=2,header=None)


# In[19]:


col_names = ['alive','class','gender','age','sibsp','parch','price','emb','deck']
pd.read_csv(r'titanic_raw.csv',skiprows=3,skipfooter=2,header=None,names=col_names)


# In[20]:


titanic = pd.read_csv(r'titanic_raw.csv',skiprows=3,skipfooter=2,header=None,names=col_names)


# In[21]:


titanic.head()


# In[22]:


#after you clean unstructed data set, then you can save it
titanic.to_csv('titanic_clean.csv')


# In[25]:


new_titanic = pd.read_csv(r'titanic_clean.csv')

new_titanic


# In[26]:


#you can see the index of data fream saved as a new columns,
# for removeing it, use
titanic.to_csv('titanic_clean.csv',index=False)


# In[27]:


new_titanic = pd.read_csv(r'titanic_clean.csv')

new_titanic


# In[ ]:




