#!/usr/bin/env python
# coding: utf-8

# In[1]:


#if you want to have iterator on list, etc, you can use enumerate function like this
my_list = ["reza","raheleh","eli","emad","sadra","taha"]
for i,item in enumerate(my_list):
    print(i,item)


# In[2]:


#if you have item like tuple with three elment in each item, you can use three iterator in the for
#like here
my_list = ("reza",62,38),("raheleh",62,38),("parisa",61,39),("eli",59,41)]
for i,j,k in my_list:
    print(i,"_",j,"_",k)


# In[5]:


#if you run one iterator on dictunary, iterator operate like keys
my_dic = {"reza":62,"raheleh":62,"parisa":61,"eli":59}
for i in my_dic:
    print(i)


# In[6]:


#if you want to access items of dictunary, use items
my_dic = {"reza":62,"raheleh":62,"parisa":61,"eli":59}
for i in my_dic.items():
    print(i)


# In[10]:


my_dic = {"reza":62,"raheleh":62,"parisa":61,"eli":59}
items = my_dic.items()
for i,j in items:
    print(i, "have", 100 - j," years old")


# In[11]:


my_dic = {"reza":62,"raheleh":62,"parisa":61,"eli":59}
for i in my_dic:
    print(i, "have", 100 - my_dic[i]," years old")


# In[13]:


#comprehension
first_list = range(0,10)
result_list = [i+1 for i in first_list]
print(result_list)


# In[15]:


my_list = [i+1 for i in range(0,10)]
print(my_list)


# In[16]:


my_list = [i+1 for i in range(0,10) if i%2 != 0]
print(my_list)


# In[17]:


dollar_list = [100,45,23,67]
riall_list = [i * 22800 for i in dollar_list]
print(riall_list)


# In[18]:


my_list = [j*2 for j in[i+1 for i in range(0,10) if i%3==0]]
print(my_list)


# In[20]:


#zip function allow you to have corresponding element in list
first_list = [1,2,3,4,5]
second_list = [10,20,30,40,50]
result = [i-j for i,j in zip(first_list,second_list)]
print(result)


# In[ ]:




