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


# In[3]:


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


# In[4]:


#str.contains(pat, case=True, flags=0, na=None, regex=True)
#Test if pattern or regex is contained within a string of a Series or Index.
df_food[df_food['Restaurant Name'].str.contains("in")]


# In[6]:


#DataFrame.sort_values
#Sort by the values along either axis
df_food.sort_values(by="Total Amount", ascending=True).head(10)


# In[7]:


df_food.sort_values(by="Total Amount", ascending=False).head(10)


# In[9]:


df_food.sort_values(by=["Total Amount","Quantity"], ascending=False).head(10)


# In[11]:


df_food.sort_values(by=["Meal Ordered","Quantity"], ascending=(False,True)).head(10)


# In[18]:


df_food.head()


# In[19]:


#pandas.DataFrame.loc
#Access a group of rows and columns by label(s) or a boolean array.
df_food.loc[1,['Meal Ordered']]


# In[20]:


df_food.loc[1,:]


# In[21]:


df_food.loc[df_food['Price Per Item']>15,:]


# In[26]:


df_food.loc[df_food['Price Per Item']>15,:].sort_values(by=['Meal Ordered','Total Amount'],                                                        ascending=(True,True))


# In[27]:


#Bucketing or Binning of continuous variable in pandas python to discrete chunks is depicted
#for bucketing using loc method, first you must create column with defualt value
df_food['Amount - Bucket'] = '--out of bound--'
df_food.head()


# In[30]:


#then filter values and assign label to them
df_food.loc[(df_food['Total Amount']>0)&(df_food['Total Amount']<=20),'Amount - Bucket']='Low'
df_food.loc[(df_food['Total Amount']>20)&(df_food['Total Amount']<=40),'Amount - Bucket']='Mid'
df_food.loc[(df_food['Total Amount']>40),'Amount - Bucket']='High'


# In[31]:


df_food.head()


# In[33]:


#for bucketing you can use another way, using cau method
#pandas.cut
#Bin values into discrete intervals.Use cut when you need to segment and sort data values into bins
bin = [0,20,40,60]
df_food['Amount - Binning'] = pd.cut(df_food['Total Amount'],bin)
df_food.head()


# In[38]:


#We will be assigning label to each bin
bin_label = ['low','mid','high']
df_food['Amount - Bucketing'] = pd.cut(df_food['Total Amount'],bin,labels=bin_label)
df_food.head()


# In[40]:


#bucketing using loc method
df_food['Vegan'] = 'Not Vegan'
df_food.loc[df_food['Restaurant Name'].str.contains('Green'),'Vegan']='Vegan'
df_food.head()


# In[ ]:




