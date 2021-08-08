#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
dic_1 = {"k1":1,"k2":2,"k3":3}
dic_1


# In[2]:


dic_1["k2"]


# In[4]:


dic_1["k2"]+3


# In[5]:


#changeable
dic_1["k3"]=4
dic_1["k3"]


# In[6]:


#add new key:value to dictionary
dic_1["k4"] = 4
print(dic_1)


# In[7]:


#To determine how many items a dictionary has, use the len() function
print(len(dic_1))


# In[8]:


#From Python's perspective, dictionaries are defined as objects with the data type 'dict'
type(dic_1)


# In[12]:


#The keys() method will return a list of all the keys in the dictionary.
dic_1.keys()


# In[13]:


#The values() method will return a list of all the values in the dictionary.
dic_1.values()


# In[15]:


#There is also a method called get() that will give you the same result:
dic_1.get("k1")


# In[16]:


#The items() method will return each item in a dictionary, as tuples in a list.
dic_1.items()


# In[17]:


if "k1" in dic_1:
    print("yes")


# In[18]:


#The returned list is a view of the items(key or values or key:value) of the dictionary, meaning that 
#any changes done to the dictionary will be reflected in the items list.
value_dic = dic_1.values()
print(value_dic)
dic_1["k5"]=5
print(value_dic)


# In[20]:


#The update() method will update the dictionary with the items from the given argument.
#The argument must be a dictionary, or an iterable object with key:value pairs.
dic_1.update({"k3":3})
dic_1


# In[21]:


#The pop() method removes the item with the specified key name
x = dic_1.pop("k5")
x


# In[22]:


#The popitem() method removes the last inserted item
x = dic_1.popitem()
x


# In[26]:


#The del keyword removes the item with the specified key name
del dic_1["k3"]


# In[27]:


dic_1


# In[28]:


#The clear() method empties the dictionary
dic_1.clear()
print(dic_1)


# In[29]:


#Make a copy of a dictionary with the copy() method
dic_1 = {"k1":1,"k2":2,"k3":3}
dic_2 = dic_1.copy()
dic_2


# In[31]:


#Another way to make a copy is to use the built-in function dict()
dic_3 = dict(dic_2)
dic_3


# In[32]:


#nested Dictionary:A dictionary can contain dictionaries, this is called nested dictionaries.
dic_4 = {"k1":1,"k2":2,"k3":3,"k4":{"l1":5,"l2":6}}
dic_4


# In[33]:


dic_4["k4"]


# In[34]:


dic_4["k4"]["l1"]


# In[36]:


#The fromkeys() method returns a dictionary with the specified keys and the specified value.
k = ("k1","k2","k3")
v = 1
dic_5 = dict.fromkeys(k,v)
dic_5


# In[ ]:




