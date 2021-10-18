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


# In[3]:


titanic.Survived.replace(to_replace=['1','0','yes','no'],value=[1,0,1,0],inplace=True)


# In[4]:


titanic.Survived.unique()


# In[5]:


titanic.describe(include='object')


# In[4]:


summer = pd.read_csv(r'summer_imp.csv')


# In[18]:


summer.head()


# In[19]:


summer.info()
#you can see we have one column name with space between them
#Athlete Name


# In[5]:


summer.rename(columns={'Athlete Name':'Athlete_Name'},inplace=True)


# In[28]:


summer.info()


# In[29]:


summer.head(20)
#you can see only Gold Medal, have Medal postfix


# In[8]:


summer.Medal.value_counts()


# In[6]:


summer.Medal.replace(to_replace='Gold Medal',value='Gold',inplace=True)


# In[24]:


summer.head(20)


# In[10]:


titanic.head()


# In[12]:


titanic.Fare.dtype
#you can see the Fare feature store as Object


# In[7]:


titanic.Fare.str.replace("$","")
#you can use str.replace function to remove $ sign


# In[8]:


titanic.Fare = titanic.Fare.str.replace("$","")


# In[18]:


titanic.Fare.dtype
#now you can change the type of the feature


# In[9]:


titanic.Fare = pd.to_numeric(titanic.Fare)


# In[12]:


titanic.Fare.dtype


# In[20]:


summer.head()
#you can see the Athlete_Name have different format(uppercase or title)


# In[21]:


summer.Athlete_Name.str.title()


# In[10]:


summer.Athlete_Name = summer.Athlete_Name.str.title()


# In[23]:


summer.head(10)


# In[14]:


summer.loc[summer.Athlete_Name=='Hajos, Alfred']


# In[16]:


#you can see there isn't Athlete with name Hajos, Alfred
summer.loc[0,]


# In[17]:


summer.iloc[0,4]
#the resoun is space before and after Hajos, Alfred


# In[19]:


#for doing somethings like that, do like this
summer.loc[summer.Athlete_Name.str.contains('Hajos, Alfred')]


# In[11]:


#for removing space from String
summer.Athlete_Name = summer.Athlete_Name.str.strip(to_strip=' ')


# In[22]:


#now you can run this code
summer.loc[summer.Athlete_Name=='Hajos, Alfred']


# In[23]:


titanic.info()


# In[12]:


#for change the type of coulmns
titanic.Survived = titanic.Survived.astype('int')


# In[27]:


titanic.info()
#there is missing values in Age feature


# In[13]:


#because of missing values in Age columns, you can't change the type
titanic.Age.astype('int')


# In[29]:


titanic.info()


# In[31]:


titanic.isna()


# In[34]:


titanic.isna().sum(axis=0)


# In[35]:


titanic.isna().any()


# In[36]:


titanic[titanic.isna().any(axis=1)]


# In[37]:


titanic.notna().sum()


# In[42]:


titanic.notna().all(axis=1)


# In[41]:


titanic[titanic.notna().all(axis=1)]


# In[14]:


#for see the missing values in graph, use code like this
import matplotlib as plt
import seaborn as sns


# In[15]:


#the dark line show the null values
sns.heatmap(titanic.notna())
#you can see the Deck have more nan values


# In[47]:


titanic.Age.value_counts(dropna=False)


# In[17]:


import numpy as np


# In[18]:


titanic.Age.replace(to_replace='Missing Data',value=np.nan,inplace=True)


# In[19]:


titanic.Age.value_counts(dropna=False)


# In[51]:


sns.heatmap(titanic.notna())


# In[20]:


titanic.Age.astype('float')


# In[22]:


titanic.shape


# In[26]:


titanic[titanic.isna().any(axis=1)].shape


# In[28]:


titanic[titanic.notna().all(axis=1)].shape


# In[29]:


#before you creating model, it's too important to process your data
titanic.dropna(axis=0,how='any').shape


# In[32]:


#the code above show that you have just 182 clean sample
#if you want to set treshold for how=any properties
titanic.dropna(axis=0,how='any',thresh=8).shape
#thresh parameter define the not null value in row or column


# In[33]:


titanic.dropna(axis=1,how='any',thresh=500).shape


# In[34]:


#you can see you don't miss data if you drop Deck column
titanic.dropna(axis=1,how='any',thresh=500,inplace=True)


# In[35]:


titanic.info()


# In[37]:


#some feature is very important and should considered
titanic.dropna(axis=0,how='any',subset=['Survived','Class','Gender','Age']               ,thresh=4).shape


# In[39]:


summer.info()


# In[40]:


summer.dropna().shape


# In[50]:


summer[summer.isna().any(axis=1)]


# In[51]:


#in this case you can drop nan, you do'nt loss more data
summer.dropna(inplace=True)


# In[52]:


summer.info()


# In[ ]:




