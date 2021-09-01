#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


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


# In[3]:


df_food.head()


# In[5]:


df_food[['Food Order ID','Customer ID','Restaurant Name','Meal Ordered','Quantity','Price Per Item']].head()


# In[7]:


df_food['totla amount'] = df_food['Quantity'] * df_food['Price Per Item']
df_food.head()


# In[8]:


#if you want to determined the row situation which saticfy condition or not, use filter like this
df_food['Restaurant Name'] == "Oasis Seafood"


# In[9]:


df_food[df_food['Restaurant Name'] == "Oasis Seafood"]


# In[14]:


df_food[df_food['totla amount'] > 50]


# In[15]:


#you can combine filter with logical operator & , |
df_food[(df_food['Quantity']>2)|(df_food['totla amount']>40)]


# In[16]:


df_food[(df_food['Quantity']>2)&(df_food['totla amount']>40)]


# In[19]:


df_food[((df_food['Quantity']>2)|(df_food['totla amount']>40))&(df_food['Day']=="Friday")]


# In[24]:


#Whether each element in the DataFrame is contained in values.
df_food[df_food['Customer ID'].isin(['A','B'])]


# In[25]:


df_food[(df_food['Customer ID'].isin(['A','B']))&(df_food['totla amount']>30)]


# In[31]:


#est if the start of each string element matches a pattern.
#str.startswith
df_food[df_food['Day'].str.startswith('W')]


# In[32]:


df_food[df_food['Day'].str.startswith('S')]


# In[35]:


#endswith(pat, na=None)
#Test if the end of each string element matches a pattern.
df_food[df_food['Meal Ordered'].str.endswith("er")]


# In[37]:


#str.contains(pat, case=True, flags=0, na=None, regex=True)
#Test if pattern or regex is contained within a string of a Series or Index.
df_food[df_food['Restaurant Name'].str.contains("in")]


# In[ ]:





# In[ ]:




