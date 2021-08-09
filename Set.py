#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Sets are used to store multiple items in a single variable
#A set is a collection which is both unordered and unindexed
#Set items are unordered, unchangeable, and do not allow duplicate values.
set_1 = {1,1,1,2,3,3,3,4,5,5,6,6}
set_1


# In[4]:


#if you want to list without any duplicate, use set like this
list_1 = [1,1,1,2,3,3,3,4,5,5,6,6]
print(list_1)
set_01 = set(list_1)
list_1 = list(set_01)
print(list_1)


# In[5]:


set_2 = {2,4,7,7,7,8,8,8,9,9}
set_2


# In[6]:


#you can retrive comman item of both set
set_1 & set_2


# In[7]:


#you can also create union of two set, but duplicate values are removed
set_3 = set_1.union(set_2)
print(set_3)


# In[8]:


#To determine how many items a set has, use the len() method.
len(set_3)


# In[9]:


#A set can contain different data types
set_4 = {"reza",1,"ali",2,"eli",3.14}
print(set_4)


# In[10]:


#From Python's perspective, sets are defined as objects with the data type 'set'
type(set_4)


# In[11]:


#You cannot access items in a set by referring to an index or a key
print("reza" in set_4)


# In[12]:


"raheleh" in set_4


# In[13]:


#Once a set is created, you cannot change its items, but you can add new items.
#To add one item to a set use the add() method.
set_4.add("raheleh")
"raheleh" in set_4


# In[17]:


#To add items from another set into the current set, use the update() method
set_4.update(set_3)
print(set_4)
#Both union() and update() will exclude any duplicate items.


# In[18]:


#To remove an item in a set, use the remove(), or the discard() method.
set_4.remove("ali")
"ali" in set_4


# In[19]:


set_4.discard(9)
9 in set_4
#If the item to remove does not exist, discard() will NOT raise an error.


# In[20]:


#The clear() method empties the set
set_4.clear()
print(set_4)


# In[21]:


#The del keyword will delete the set completely
del set_4
print(set_4)


# In[22]:


#The intersection_update() method will keep only the items that are present in both sets.
set_1.intersection_update(set_2)
print(set_1)


# In[26]:


#The intersection() method will return a new set, 
#that only contains the items that are present in both sets
set_1 = {1,2,3}
set_2 = {1,2,4}
set_3 = set_1.intersection(set_2)
set_1.intersection_update(set_2)
print("set1: ",set_1)
print("set3: ",set_3)
#intersection_update don't return any set


# In[28]:


#The symmetric_difference_update() method will keep only 
#the elements that are NOT present in both sets.
print(set_1)
print(set_2)
set_2.symmetric_difference_update(set_1)
print(set_2)


# In[29]:


#The symmetric_difference() method will return a new set, 
#that contains only the elements that are NOT present in both sets.
print(set_1)
print(set_2)
set_3 = set_1.symmetric_difference(set_2)
print(set_3)


# In[30]:


set_2 = set_1
print(set_2)


# In[31]:


set_2 = set_3.copy()
print(set_2)


# In[32]:


#Return a set that contains the items that only exist in set x, and not in set y:
x = {1,2,3}
y = {-1,0,1}

z = x.difference(y)

print(z)


# In[34]:


#The isdisjoint() method returns True if none of the items are present in both sets, 
#otherwise it returns False.
x = {1,2,3}
y = {-1,-2,-3}

z = x.isdisjoint(y)

print(z)


# In[37]:


#The issubset() method returns True if all items in the set exists in the specified set, 
#otherwise it retuns False.
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

print(z)
#The issuperset() method returns True if all items in the specified set exists in the original set, 
#otherwise it retuns False.
z = y.issuperset(x)

print(z)

