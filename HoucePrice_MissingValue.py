#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


HouceData = pd.read_csv(r'train.csv')


# In[29]:


HouceData.info()


# In[3]:


HouceData.set_index('Id',inplace=True)


# In[4]:


HouceData.head()


# In[5]:


HouceData_test = pd.read_csv(r'test.csv',index_col='Id')


# In[33]:


HouceData_test.head()


# In[27]:


HouceData.info()


# In[6]:


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


# In[7]:


from sklearn.model_selection import train_test_split
X_train,X_val, Y_train, Y_val = train_test_split(X,y,train_size=0.8,
                                                 test_size=0.2,random_state=0)


# In[38]:


#you have 1168 rows and 36 columns
X_train.shape


# In[8]:


#in 3 columns, we have null value
X_train.isnull().sum()


# In[9]:


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


# In[10]:


imputed_X_train.isnull().sum()


# In[11]:


from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
myModel = RandomForestRegressor(n_estimators=300,random_state=0,criterion='mae',max_depth=13)
myModel.fit(imputed_X_train,Y_train)
print('MAE is %d' % mean_absolute_error(Y_val,myModel.predict(imputed_X_val)))


# In[13]:


myImputer1 = SimpleImputer(strategy='mean')
imputed_X_train = pd.DataFrame(myImputer1.fit_transform(X_train))
imputed_X_val = pd.DataFrame(myImputer1.transform(X_val))
imputed_X_train.columns = X_train.columns
imputed_X_val.columns = X_val.columns

myModel = RandomForestRegressor(n_estimators=300,random_state=0,criterion='mae',max_depth=13)
myModel.fit(imputed_X_train,Y_train)
print('MAE is %d' % mean_absolute_error(Y_val,myModel.predict(imputed_X_val)))


# In[25]:


#in SimpleImputer you impute MissingValue based on Single Freature,
#If you want to impute based on Multivatiate, use IterativImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

myImputer2 = IterativeImputer(random_state=0)
myImputer2.fit(X_train)

imputed_X_train = pd.DataFrame(myImputer2.fit_transform(X_train))
imputed_X_val = pd.DataFrame(myImputer2.transform(X_val))
imputed_X_train.columns = X_train.columns
imputed_X_val.columns = X_val.columns

myModel = RandomForestRegressor(n_estimators=300,random_state=0,criterion='mae',max_depth=13)
myModel.fit(imputed_X_train,Y_train)
print('MAE is %d' % mean_absolute_error(Y_val,myModel.predict(imputed_X_val)))


# In[28]:


#Imputation for completing missing values using k-Nearest Neighbors.
#Each sample’s missing values are imputed using the mean value from n_neighbors
#nearest neighbors found in the training set
from sklearn.impute import KNNImputer
myImputer3 = KNNImputer(n_neighbors=2)

imputed_X_train = pd.DataFrame(myImputer3.fit_transform(X_train))
imputed_X_val = pd.DataFrame(myImputer3.transform(X_val))
imputed_X_train.columns = X_train.columns
imputed_X_val.columns = X_val.columns

myModel.fit(imputed_X_train,Y_train)
print('MAE is %d' % mean_absolute_error(Y_val,myModel.predict(imputed_X_val)))


# In[29]:


myImputer4 = KNNImputer(n_neighbors=3)

imputed_X_train = pd.DataFrame(myImputer4.fit_transform(X_train))
imputed_X_val = pd.DataFrame(myImputer4.transform(X_val))
imputed_X_train.columns = X_train.columns
imputed_X_val.columns = X_val.columns

myModel.fit(imputed_X_train,Y_train)
print('MAE is %d' % mean_absolute_error(Y_val,myModel.predict(imputed_X_val)))


# In[ ]:




