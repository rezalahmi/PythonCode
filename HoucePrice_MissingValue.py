#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[28]:


HouceData = pd.read_csv(r'train.csv')


# In[29]:


HouceData.info()


# In[30]:


HouceData.set_index('Id',inplace=True)


# In[31]:


HouceData.head()


# In[32]:


HouceData_test = pd.read_csv(r'test.csv',index_col='Id')


# In[33]:


HouceData_test.head()


# In[27]:


HouceData.info()


# In[34]:


#first of all remove missing value from target
HouceData.dropna(axis=0, subset=['SalePrice'], inplace=True)
#with this code, All rows with NaN value for SalePrice dropped
#then we set Y
y = HouceData.SalePrice
#remove Target from training data
HouceData.drop(['SalePrice'], axis=1, inplace=True)
#some columns are Object, for simplicity remove them
X = HouceData.select_dtypes(exclude=['object'])
X_test = HouceData_test.select_dtypes(exclude=['object'])


# In[35]:


X.head()


# In[36]:


y.head()


# In[37]:


from sklearn.model_selection import train_test_split
X_train,X_val, Y_train, Y_val = train_test_split(X,y,train_size=0.8,
                                                 test_size=0.2,random_state=0)


# In[38]:


#you have 1168 rows and 36 columns
X_train.shape


# In[18]:


#in 3 columns, we have null value
X_train.isnull().sum()


# In[39]:


#Missing Value 
from sklearn.impute import SimpleImputer
myImputer = SimpleImputer(strategy='median')
#Fit to data, then transform it.
#this method, based on X_train dataset, train herself and then impute values
#for missing values
imputed_X_train = pd.DataFrame(myImputer.fit_transform(X_train))
#now myImputer has trained and can impute value for X_valid
imputed_X_val = pd.DataFrame(myImputer.transform(X_val))
# Fill in the lines below: imputation removed column names; put them back
imputed_X_train.columns = X_train.columns
imputed_X_val.columns = X_val.columns


# In[41]:


imputed_X_train.isnull().sum()


# In[42]:


from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
myModel = RandomForestRegressor(n_estimators=300,random_state=0,criterion='mae',max_depth=13)
myModel.fit(imputed_X_train,Y_train)
print('MAE is %d' % mean_absolute_error(Y_val,myModel.predict(imputed_X_val)))


# In[43]:


myImputer1 = SimpleImputer(strategy='mean')
imputed_X_train = pd.DataFrame(myImputer1.fit_transform(X_train))
imputed_X_val = pd.DataFrame(myImputer1.transform(X_val))
imputed_X_train.columns = X_train.columns
imputed_X_val.columns = X_val.columns


# In[44]:


myModel = RandomForestRegressor(n_estimators=300,random_state=0,criterion='mae',max_depth=13)
myModel.fit(imputed_X_train,Y_train)
print('MAE is %d' % mean_absolute_error(Y_val,myModel.predict(imputed_X_val)))


# In[ ]:




