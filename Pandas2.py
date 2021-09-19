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


# In[6]:


type(titanic['Age'])


# In[7]:


type(titanic[['Age']])


# In[ ]:


#if you want to select one column 
#from data frame you should decide which output is benefical, data frame or data seires.


# In[8]:


#also you can use dot notation
titanic.Age


# In[9]:


olympics = pd.read_csv(r'athlete_events.csv')


# In[10]:


olympics.info()


# In[11]:


olympics.describe()


# In[12]:


olympics.head()


# In[14]:


olympics = pd.read_csv(r'athlete_events.csv',index_col = 'ID')
#index_col:Column(s) to use as the row labels of the DataFrame, either given as string name or column index.


# In[15]:


olympics


# In[16]:


olympics.iloc[0]


# In[18]:


type(olympics.iloc[0])


# In[20]:


olympics.iloc[-1]


# In[23]:


olympics.iloc[[0,1,2]]


# In[24]:


olympics.iloc[0:5]


# In[25]:


olympics.iloc[-5:]


# In[26]:


olympics.iloc[[4,67,123]]


# In[28]:


#with iloc, you can get two index and return the cell of data frame
olympics.iloc[0,1]


# In[30]:


olympics.iloc[0,0:5]


# In[31]:


olympics.iloc[0:3,0:5]


# In[33]:


#.loc[] is primarily label based, but may also be used with a boolean array.
olympics.loc[3]


# In[34]:


olympics.loc[3,'Medal']


# In[35]:


olympics.loc[3,['Medal','Year']]


# In[36]:


olympics.loc[[3,4],['Medal','Year']]


# In[37]:


olympics.loc[1:5,'Name':'Team']


# In[38]:


olympics.loc[5]


# In[ ]:




