#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("welcome to \nThis course")


# In[2]:


name = "rezaLahmi"


# In[3]:


name[4]


# In[4]:


name[1]


# In[5]:


name[0]


# In[6]:


len(name)


# In[8]:


name[8]


# In[9]:


name[len(name)-1]


# In[10]:


name[4:]


# In[11]:


name[:4]


# In[12]:


name[::2]


# In[13]:


name[::3]


# In[14]:


name[::4]


# In[15]:


name[::5]


# In[16]:


name[::-1]


# In[17]:


name[::-2]


# In[18]:


name[2:4]


# In[19]:


name="MohammadrezaLahmi"


# In[20]:


name.find("reza")


# In[24]:


name.find("Lahmi")


# In[ ]:





# In[25]:


name[name.find("reza"):name.find("Lahmi")]


# In[26]:


name[name.find("reza"):name.find("reza")+len("reza")]


# In[27]:


search = "reza"


# In[28]:


print("The",search,"is in the name variable in",name.find(search))


# In[33]:


print(name[name.find(search):name.find(search)+len(search)])


# In[36]:


search = input("please enter the name: ")
print("The",search,"is in the name variable in",name.find(search))


# In[ ]:





# In[ ]:




