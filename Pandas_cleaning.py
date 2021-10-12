#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


titanic = pd.read_csv(r'titanic_imp.csv')


# In[3]:


titanic.head()


# In[4]:


titanic.info()
#you can see, some numerical columns have object data type


# In[5]:


titanic.describe()


# In[7]:


titanic.describe(include='object')
#there is some un normaly in the Survived column


# In[8]:


titanic.Survived.unique()


# In[9]:


titanic.Survived.value_counts()


# In[13]:


titanic.Survived.replace(to_replace=['1','0','yes','no'],value=[1,0,1,0],inplace=True)


# In[14]:


titanic.Survived.unique()


# In[15]:


titanic.describe(include='object')


# In[26]:


summer = pd.read_csv(r'summer_imp.csv')


# In[18]:


summer.head()


# In[19]:


summer.info()
#you can see we have one column name with space between them
#Athlete Name


# In[27]:


summer.rename(columns={'Athlete Name':'Athlete_Name'},inplace=True)


# In[28]:


summer.info()


# In[29]:


summer.head(20)
#you can see only Gold Medal, have Medal postfix


# In[30]:


summer.Medal.value_counts()


# In[31]:


summer.Medal.replace(to_replace='Gold Medal',value='Gold',inplace=True)


# In[24]:


summer.head(20)


# In[ ]:




