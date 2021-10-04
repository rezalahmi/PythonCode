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


# In[34]:


allModel = {}
for num in range(10,100):
    myModel = DecisionTreeRegressor(max_leaf_nodes=num,random_state=1)
    myModel.fit(train_X,train_y)
    myModel_predict = myModel.predict(val_X)
    allModel[num] = mean_absolute_error(val_y,myModel_predict)
min(allModel,key=allModel.get)


# In[35]:


from sklearn.tree import DecisionTreeRegressor
myModel = DecisionTreeRegressor(max_leaf_nodes=42, random_state=1)
myModel.fit(train_X,train_y)


# In[36]:


from sklearn.metrics import mean_absolute_error
myModel_predict = myModel.predict(val_X)
mean_absolute_error(val_y,myModel_predict)


# In[ ]:




