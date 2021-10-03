#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
melborn_data = pd.read_csv(r'melb_data.csv')
melborn_data.dropna(axis=0,inplace=True)


# In[2]:


from sklearn.model_selection import train_test_split


# In[3]:


y = melborn_data.Price
x = melborn_data[['Rooms','Bedroom2','Bathroom','Car','YearBuilt']]


# In[4]:


train_X, val_X, train_y, val_y = train_test_split(x,y,random_state=1)


# In[5]:


from sklearn.tree import DecisionTreeRegressor
myModel = DecisionTreeRegressor(random_state=1)
myModel.fit(train_X,train_y)


# In[6]:


from sklearn.metrics import mean_absolute_error
myModel_predict = myModel.predict(val_X)
mean_absolute_error(val_y,myModel_predict)


# In[ ]:




