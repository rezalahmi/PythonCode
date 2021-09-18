#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


titanic = pd.read_csv(r'titanic.csv')


# In[3]:


titanic


# In[4]:


titanic.info()


# In[5]:


titanic.describe()


# In[6]:


#if you want to desctibe just non numeric value use O in include
titanic.describe(include='O')


# In[8]:


titanic.describe(include = 'all')


# In[9]:


type(titanic)


# In[10]:


len(titanic)


# In[11]:


round(titanic,0)


# In[12]:


titanic.shape


# In[13]:


titanic.size


# In[14]:


titanic.index


# In[15]:


titanic.columns


# In[16]:


#return min values from each columns
titanic.min()


# In[17]:


titanic.max()


# In[18]:


#mean values of each columns
titanic.mean()


# In[23]:


titanic.sort_values(by='Age',ascending=False)


# In[ ]:





# In[ ]:





# In[ ]:




