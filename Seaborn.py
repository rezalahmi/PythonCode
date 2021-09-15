#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns; sns.set()


# In[2]:


df_salary = pd.read_csv(r'D:\Udemy\Udemy - The Python Bootcamp Data Science, Analytics & Visualisation\9. Data Visualisation - Seaborn\1.1 Salary.csv')
df_salary.head()


# In[3]:


df_salary.info()


# In[6]:


df_salary.describe()


# In[8]:


#seaborn.scatterplot
sns.scatterplot(x=df_salary['Years at Firm'],y=df_salary['Base Salary'])


# In[9]:


sns.scatterplot(x=df_salary['Years at Firm'],y=df_salary['Base Salary'],hue=df_salary['Position'])
#hue:Grouping variable that will produce points with different colors. 
#Can be either categorical or numeric, 
#although color mapping will behave differently in latter case.


# In[10]:


#data:Input data structure. 
#Either a long-form collection of vectors that can be assigned to named variables or 
#a wide-form dataset that will be internally reshaped.
sns.scatterplot(x='Years at Firm',y='Base Salary',data=df_salary)


# In[13]:


#seaborn.lmplot
sns.lmplot(x='Years at Firm',y='Base Salary',data=df_salary)


# In[14]:


sns.lmplot(x='Years at Firm',y='Base Salary',data=df_salary,hue='Position')


# In[15]:


#seaborn.distplot
sns.distplot(df_salary['Predicted Score'],bins=10)
#bin:Specification of hist bins. 
#If unspecified, as reference rule is used that tries to find a useful default.


# In[16]:


#hist:Whether to plot a (normed) histogram.
#kde:Whether to plot a gaussian kernel density estimate
sns.distplot(df_salary['Predicted Score'],bins=10,hist=False,kde=True)


# In[18]:


#seaborn.kdeplot
sns.kdeplot(df_salary['Predicted Score'],shade=True)
#shade:Alias for fill. Using fill is recommended.


# In[19]:


sns.kdeplot(df_salary['Predicted Score'],shade=False)


# In[ ]:




