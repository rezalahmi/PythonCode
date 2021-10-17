#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.model_selection import train_test_split
#read data set
X = pd.read_csv(r'train.csv')
X_test = pd.read_csv(r'test.csv')
#remove data with missing target, seperate target from pridector
X.dropna(axis=0,subset=['SalePrice'],inplace=True)
y = X.SalePrice
X.drop(['SalePrice'],axis=1,inplace=True)
#remove columns with missing value
cols_with_missing = [col for col in X.columns if X[col].isnull().any()]
X.drop(cols_with_missing,axis=1,inplace=True)
X_test.drop(cols_with_missing,axis=1,inplace=True)
#Break off validation set from training data
X_train, X_valid, y_train, y_valid = train_test_split(X,y,test_size=0.2,
                                                     train_size=0.8,
                                                     random_state=0)


# In[4]:


X_train.head()


# In[5]:


X_train.describe(include='object')


# In[6]:


X_train.describe()


# In[7]:


X_train['Condition2'].unique()


# In[8]:


X_valid['Condition2'].unique()


# In[2]:


#This is a common problem that you'll encounter with real-world data, 
#and there are many approaches to fixing this issue. 
#For instance, you can write a custom label encoder to deal with new categories.
#The simplest approach, however, is to drop the problematic categorical columns.
#Run the code cell below to save the problematic columns to a Python list 
#bad_label_cols. 
#Likewise, columns that can be safely label encoded are stored in 
#good_label_cols.
object_cols = [col for col in X_train.columns if X_train[col].dtype=='object']
good_label_cols = [col for col in object_cols
                  if set(X_train[col])==set(X_valid[col])]
bad_label_cols = list(set(object_cols)-set(good_label_cols))


# In[20]:


print(good_label_cols)
print(bad_label_cols)


# In[3]:


#drop bad label col
label_X_train = X_train.drop(bad_label_cols,axis=1)
label_X_valid = X_valid.drop(bad_label_cols,axis=1)


# In[4]:


from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
for col in set(good_label_cols):
    label_X_train[col] = label_encoder.fit_transform(X_train[col])
    label_X_valid[col] = label_encoder.transform(X_valid[col])


# In[5]:


from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
myModel = RandomForestRegressor(n_estimators=300,random_state=0,criterion='mae',max_depth=13)
myModel.fit(label_X_train,y_train)
print('MAE is %d' % mean_absolute_error(y_valid,myModel.predict(label_X_valid)))


# In[6]:


from sklearn.preprocessing import OrdinalEncoder
ordinal_encoder = OrdinalEncoder()


# In[7]:


olabel_X_train = X_train.drop(bad_label_cols,axis=1)
olabel_X_valid = X_valid.drop(bad_label_cols,axis=1)
olabel_X_train = ordinal_encoder.fit_transform(X_train[good_label_cols])
olabel_X_valid = ordinal_encoder.transform(X_valid[good_label_cols])


# In[8]:


myModel.fit(label_X_train,y_train)
print('MAE is %d' % mean_absolute_error(y_valid,myModel.predict(label_X_valid)))


# In[9]:


# Get number of unique entries in each column with categorical data
object_nunique = list(map(lambda col: X_train[col].nunique(), object_cols))
d = dict(zip(object_cols, object_nunique))

# Print number of unique entries by column, in ascending order
sorted(d.items(), key=lambda x: x[1])


# In[10]:


X_train.describe(include='object')


# In[12]:


low_cardinality_col = [col for col in X_train.columns
                       if X_train[col].nunique()<10]
high_cardinality_col = set(object_cols) - set(low_cardinality_col)


# In[15]:


from sklearn.preprocessing import OneHotEncoder
oneHotEncoder = OneHotEncoder(handle_unknown='ignore',sparse=False)
#create new dataframe based X_train[low_calrdinality_col] onehot encoding
OH_cols_train = pd.DataFrame(oneHotEncoder.fit_transform(X_train[low_cardinality_col]))
OH_cols_valid = pd.DataFrame(oneHotEncoder.transform(X_valid[low_cardinality_col]))
#oneHot remove index
OH_cols_train.index = X_train.index
OH_cols_valid.index = X_valid.index
#remove object from tain and valid
num_X_train = X_train.drop(object_cols,axis=1)
num_X_valid = X_valid.drop(object_cols,axis=1)
#now you should merge two data set
OH_X_train = pd.concat([num_X_train,OH_cols_train],axis=1)
OH_X_valid = pd.concat([num_X_valid,OH_cols_valid],axis=1)


# In[17]:


myModel.fit(OH_X_train,y_train)
print('MAE is %d' % mean_absolute_error(y_valid,myModel.predict(OH_X_valid)))


# In[ ]:




