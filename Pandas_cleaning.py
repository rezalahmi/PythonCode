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


# In[10]:


summer.rename(columns={'Athlete Name':'Athlete_Name'},inplace=True)


# In[28]:


summer.info()


# In[29]:


summer.head(20)
#you can see only Gold Medal, have Medal postfix


# In[8]:


summer.Medal.value_counts()


# In[5]:


summer.Medal.replace(to_replace='Gold Medal',value='Gold',inplace=True)


# In[24]:


summer.head(20)


# In[10]:


titanic.head()


# In[12]:


titanic.Fare.dtype
#you can see the Fare feature store as Object


# In[6]:


titanic.Fare.str.replace("$","")
#you can use str.replace function to remove $ sign


# In[7]:


titanic.Fare = titanic.Fare.str.replace("$","")


# In[18]:


titanic.Fare.dtype
#now you can change the type of the feature


# In[8]:


titanic.Fare = pd.to_numeric(titanic.Fare)


# In[12]:


titanic.Fare.dtype


# In[20]:


summer.head()
#you can see the Athlete_Name have different format(uppercase or title)


# In[9]:


summer.Athlete_Name.str.title()


# In[11]:


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


# In[12]:


#for removing space from String
summer.Athlete_Name = summer.Athlete_Name.str.strip(to_strip=' ')


# In[13]:


#now you can run this code
summer.loc[summer.Athlete_Name=='Hajos, Alfred']


# In[23]:


titanic.info()


# In[14]:


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


# In[15]:


titanic.isna().sum(axis=0)


# In[35]:


titanic.isna().any()


# In[16]:


titanic[titanic.isna().any(axis=1)]


# In[17]:


titanic.notna().sum()


# In[42]:


titanic.notna().all(axis=1)


# In[18]:


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


# In[19]:


import numpy as np


# In[20]:


titanic.Age.replace(to_replace='Missing Data',value=np.nan,inplace=True)


# In[21]:


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


# In[22]:


#you can see you don't miss data if you drop Deck column
titanic.dropna(axis=1,how='any',thresh=500,inplace=True)


# In[23]:


titanic.info()


# In[24]:


#some feature is very important and should considered
titanic.dropna(axis=0,how='any',subset=['Survived','Class','Gender','Age']               ,thresh=4).shape


# In[39]:


summer.info()


# In[25]:


summer.dropna().shape


# In[26]:


summer[summer.isna().any(axis=1)]


# In[27]:


#in this case you can drop nan, you do'nt loss more data
summer.dropna(inplace=True)


# In[28]:


summer.info()


# In[29]:


#we have 173 sample with duplicate
titanic.duplicated(keep=False).sum()


# In[31]:


#if don't consider the one of two duplicated sample, we have 114 duplicated sapmle
titanic.duplicated(keep='first').sum()


# In[32]:


#for drop duplicate use drop_duplicate metho
titanic.drop_duplicates(ignore_index=True).info()


# In[33]:


#if you set ignore_index=False it don't reset the index
#index between 0 to 890, but you have 780 entries
titanic.drop_duplicates(ignore_index=False).info()


# In[35]:


titanic.info()


# In[39]:


titanic.Age = titanic.Age.astype('float')


# In[40]:


titanic.info()


# In[41]:


titanic.describe()


# In[44]:


titanic.boxplot('Age',figsize=(12,6))


# In[46]:


titanic.Age.plot()
# you can see you have index label on X axie and Age on Y axie


# In[49]:


titanic.loc[titanic.Age > 90]


# In[50]:


age_outlaier_index = titanic.loc[titanic.Age > 90].index


# In[51]:


age_outlaier_index


# In[52]:


titanic.Age[age_outlaier_index] = titanic.Age[age_outlaier_index]/10


# In[55]:


titanic.loc[age_outlaier_index]


# In[56]:


titanic.info()
#please see the memoty usage of data set


# In[58]:


titanic.describe(include='object')


# In[59]:


#you can change the Gender and Emb feature to category to reduce the memory usage
titanic.Gender = titanic.Gender.astype('category')


# In[62]:


titanic.Gender.dtype


# In[63]:


titanic.Emb = titanic.Emb.astype('category')


# In[66]:


titanic.info()
#you reduce the size of the data set


# In[67]:


summer.info()


# In[69]:


summer.describe(include='object')


# In[70]:


summer.Gender = summer.Gender.astype('category')
summer.Medal = summer.Medal.astype('category')


# In[71]:


summer.info()


# In[72]:


pd.NA


# In[ ]:




