#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[28]:


#Read a comma-separated values (csv) file into DataFrame.
df_food = pd.read_csv(r'D:\Udemy\Udemy - The Python Bootcamp Data Science, Analytics & Visualisation\7. Data Analytics (Pandas)\2.1 Food Orders.csv')


# In[5]:


#Return the first n rows.
df_food.head()


# In[6]:


df_food.head(10)


# In[9]:


#Get the number of rows: len(df)
len(df_food)


# In[12]:


#Get the number of columns: len(df.columns)
len(df_food.columns)


# In[14]:


#Get the number of rows and columns: df.shape
df_food.shape


# In[15]:


df_food.info


# In[16]:


#Descriptive statistics include those that summarize the central tendency, 
#dispersion and shape of a dataset’s distribution, excluding NaN values.
df_food.describe()


# In[17]:


df_food.describe(include='all')


# In[19]:


#Return the dtypes in the DataFrame.
df_food.dtypes


# In[20]:


#Cast a pandas object to a specified dtype dtype.
df_string = df_food.astype('object')
df_string.dtypes


# In[22]:


df_float = df_string.astype({'Food Order ID':'int64','Quantity':'int64','Price Per Item':'float'})
df_float.dtypes


# In[23]:


df_food.head()


# In[24]:


df_food['Total Amount'] = df_food['Quantity'] * df_food['Price Per Item']


# In[25]:


df_food.head()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




