#!/usr/bin/env python
# coding: utf-8

# In[1]:


my_list = ["reza",62,"sadra",86,"raheleh",62]


# In[2]:


my_list[0]
#return first elemnt(string)


# In[3]:


my_list[0][0]
#you can manipulate elemnt


# In[4]:


my_list[1]
#retrun second elemnt


# In[5]:


my_list[0:0]
#retrun empthy list


# In[6]:


my_list[0:1]
#retrun list from zero to one


# In[7]:


my_list[1:2]


# In[8]:


my_list[1:3]


# In[9]:


my_list[2:4]


# In[10]:


my_list[:2]


# In[11]:


my_list[2:]


# In[12]:


my_list[::2]


# In[13]:


my_list[1::2]


# In[14]:


my_list[::-1]


# In[15]:


my_list.append(1389)
#add elemnt to rear of a list


# In[16]:


my_list


# In[17]:


my_list.index(1389)
#find the position of elemnt


# In[18]:


my_list.pop(6)
#remove the elemnt in the specific position and return elemnt
#this method get index of elemnt and then return that


# In[19]:


my_list


# In[25]:


my_list.insert(1,1389)
#add one elemnt to the specific position


# In[26]:


my_list


# In[27]:


my_list.remove(1389)
#this method get the elemnt from list and remove it


# In[ ]:





# In[28]:


my_list


# In[29]:


eli_list = my_list.copy()
#this method copy one list to another


# In[30]:


eli_list


# In[31]:


eli_list[0] = "eli"
eli_list[1] = 59


# In[32]:


eli_list


# In[33]:


eli_list[eli_list.index("raheleh")] = "taha"


# In[34]:


eli_list


# In[35]:


eli_list[eli_list.index(62)] = 91
eli_list


# In[36]:


my_list.reverse()
#this method reverse elemnt in the list and store on in


# In[37]:


my_list


# In[38]:


my_list.reverse()
my_list


# In[39]:


my_list.sort(reverse=True)
#if list contain only number element, you can sort it


# In[41]:


x_list = [3,5,8,1,3,3.4,4.7]
x_list.sort()
x_list


# In[42]:


x_list.sort(reverse=True)


# In[43]:


x_list


# In[44]:


nested_list = [1,2,3,my_list]


# In[45]:


nested_list


# In[47]:


nested_list[3]


# In[48]:


nested_list[3][1::2]


# In[ ]:




