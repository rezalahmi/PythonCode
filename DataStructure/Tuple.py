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


# In[14]:


print(tuple_c[-1])
#Negative indexing means start from the end.
print(tuple_c[-2])


# In[17]:


if "ali" in tuple_c:
    print("yes")


# In[18]:


if "reza" in tuple_c:
    print("yes")


# In[19]:


#The del keyword can delete the tuple completely
del tuple_a


# In[20]:


print(tuple_a)


# In[21]:


#unpacking
#When we create a tuple, we normally assign values to it. This is called "packing" a tuple
#But, in Python, we are also allowed to extract the values back into variables.
#This is called "unpacking"
(red,blue) = tuple_b
print(red)
print(blue)


# In[22]:


#If you want to multiply the content of a tuple a given number of times, you can use the * operator
tuple_b2 = tuple_b * 2
print(tuple_b2)


# In[24]:


#The count() method returns the number of times a specified value appears in the tuple.
tuple_b2.count("eli")


# In[26]:


#The index() method finds the first occurrence of the specified value
print(tuple_c.index(59))
#if item not found in the tuple, exception occure


# In[ ]:




