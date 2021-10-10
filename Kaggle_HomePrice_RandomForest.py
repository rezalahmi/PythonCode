#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
X_full = pd.read_csv(r'train.csv')
X_test_full = pd.read_csv(r'test.csv')
y = X_full.SalePrice
features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = X_full[features].copy()
X_test = X_test_full[features].copy()

from sklearn.model_selection import train_test_split
X_train, X_valid, y_train, y_valid = train_test_split(X,y,train_size=0.8,test_size=0.2,random_state=1)


# In[36]:


from sklearn.ensemble import RandomForestRegressor
myModel1 = RandomForestRegressor(n_estimators=50,random_state=0)
myModel2 = RandomForestRegressor(n_estimators=100,random_state=0)
myModel3 = RandomForestRegressor(n_estimators=100,criterion='mae',random_state=0)
myModel4 = RandomForestRegressor(n_estimators=200,min_samples_split=20,random_state=0)
myModel5 = RandomForestRegressor(n_estimators=100,max_depth=7,random_state=0)
myModel6 = RandomForestRegressor(n_estimators=300,random_state=0,criterion='mae',max_depth=13)
models = [myModel1,myModel2,myModel3,myModel4,myModel5,myModel6]


# In[37]:


from sklearn.metrics import mean_absolute_error
def score_model(model, X_t=X_train, X_v=X_valid, y_t=y_train, y_v=y_valid):
    model.fit(X_t, y_t)
    preds = model.predict(X_v)
    return mean_absolute_error(y_v, preds)
for i in range(0, len(models)):
    mae = score_model(models[i])
    print("Model %d MAE: %d" % (i+1, mae))


# In[41]:


myModel6 = RandomForestRegressor(n_estimators=300,random_state=0,criterion='mae',max_depth=13)
myModel6.fit(X_train,y_train)
preds = myModel6.predict(X_valid)
print("Model MAE is : %d"%mean_absolute_error(y_valid,preds))


# In[ ]:




