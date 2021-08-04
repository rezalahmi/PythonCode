#!/usr/bin/env python
# coding: utf-8

# In[1]:


#tuple
tuple_a = ("reza",)


# In[2]:


type(tuple_a)


# In[3]:


tuple_b = ("reza")
type(tuple_b)
#if you want to create tuple with one elemnt, you should use comma after element


# In[4]:


tuple_a = ("reza",62,"sadra",86)


# In[5]:


tuple_a[2]


# In[6]:


tuple_a.append("taha")
#tuple object has no method for add item, because tuple orderd and unchangable


# In[7]:


#if you want to add item to tuple, do like this
print(tuple_a)
list_a = list(tuple_a)
list_a.append("raheleh")
list_a.append(62)
tuple_a = tuple(list_a)
tuple_a


# In[8]:


tuple_b = ("eli",59)
#you can combine two tuple with each other
tuple_c = tuple_a + tuple_b
tuple_c


# In[9]:


tuple_c[2:5]


# In[10]:


tuple_c[::2]


# In[11]:


len(tuple_c)


# In[ ]:




