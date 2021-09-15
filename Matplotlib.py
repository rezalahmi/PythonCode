#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


df_food = pd.read_csv(r'D:\Udemy\Udemy - The Python Bootcamp Data Science, Analytics & Visualisation\8. Data Visualisation - Matplotlib\2.1 Food Orders.csv')
df_food.head(5)


# In[5]:


df_food['Day'].unique()


# In[3]:


df_food['Day'].replace({'Monday':'01 - Monday','Tuesday':'02 - Tuesday','Wednesday':'03 - Wednesday'                       , 'Thursday':'04 - Thursday','Friday':'05 - Friday','Saturday':'06 - Saturday'                       , 'Sunday':'07 - Sunday'},inplace = True)


# In[4]:


df_food['Total Amount'] = df_food['Quantity'] * df_food['Price Per Item']


# In[10]:


df_food.dtypes


# In[11]:


df_food.corr()


# In[6]:


df_pre_agg_a = df_food[['Customer ID','Total Amount']]
df_pre_agg_a.head()


# In[15]:


df_agg = df_pre_agg_a.groupby('Customer ID',as_index = False).sum()


# In[16]:


df_agg.info()


# In[19]:


x = df_agg['Customer ID']
y = df_agg['Total Amount']
plt.bar(x,y,color='blue',edgecolor='black')
plt.title('Total Customer Spent')
plt.xlabel('Customer ID')
plt.ylabel('Total Amount')
plt.show()


# In[20]:


df_pre_agg_b = df_food[['Day','Total Amount']]
df_agg_b = df_pre_agg_b.groupby('Day',as_index=False).sum()


# In[22]:


df_agg_b


# In[37]:


#Plot y versus x as lines and/or markers.
x = df_agg_b['Day']
y = df_agg_b['Total Amount']
#for beter understand plot, use point of the line
#for squre s, for circle o and v....
#https://matplotlib.org/stable/api/markers_api.html#module-matplotlib.markers
plt.plot(x,y,marker='s')
plt.xticks(rotation='vertical')
plt.grid(alpha=0.5)
plt.xlabel('Day')
plt.ylabel('Total Amount')
plt.title('Total Amount per Day')
plt.show()


# In[40]:


df_pre_agg_c = df_food[['Restaurant Name','Total Amount']]
df_agg_c = df_pre_agg_c.groupby('Restaurant Name',as_index = False).sum()
df_agg_c


# In[44]:


x = df_agg_c['Restaurant Name']
y = df_agg_c['Total Amount']
plt.pie(y,labels = x,autopct="%1.1f%%")
#autopct show number in the chart
plt.axis('equal')
plt.show()


# In[50]:


x = df_agg_c['Restaurant Name']
y = df_agg_c['Total Amount']
plt.pie(y,labels = round(y,2),autopct="%1.1f%%")
#autopct show number in the chart
plt.legend(x,loc='center right',bbox_to_anchor=(0.7,0.3,0.5,1))
#add legend
plt.title('Restaurant and totla amount')
plt.axis('equal')
plt.show()


# In[ ]:




