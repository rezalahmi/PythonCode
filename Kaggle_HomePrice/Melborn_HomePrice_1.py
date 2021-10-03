#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


melborn_data = pd.read_csv(r'melb_data.csv')


# In[3]:


melborn_data.info()


# In[4]:


melborn_data.dropna(axis=0)


# In[5]:


melborn_data.dropna(axis=0,inplace=True)


# In[7]:


#first of all, you should choose the X and y columns
y = melborn_data.Price
x = melborn_data[['Rooms','Bedroom2','Bathroom','Car','YearBuilt']]


# In[9]:


#now you should Define the model
from sklearn.tree import DecisionTreeRegressor
myModel = DecisionTreeRegressor(random_state=1)
#now you can fit model based on X and y
myModel.fit(x,y)


# In[10]:


print(x.head())


# In[13]:


#in this increment, toy predict
print(myModel.predict(x))


# In[14]:


y.head(5)


# In[16]:


#for evaluation
from sklearn.metrics import mean_absolute_error
myModel_predict = myModel.predict(x)
mean_absolute_error(y,myModel_predict)


# In[ ]:




