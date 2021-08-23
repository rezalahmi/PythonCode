#!/usr/bin/env python
# coding: utf-8

# In[1]:


my_list = ["reza","eli","sadra","taha","raheleh"]
for x in my_list:
    print(x)


# In[2]:


#Looping Through a String
for x in "raheleh":
    print(x)


# In[5]:


#The range() function returns a sequence of numbers, starting from 0 by default, 
#and increments by 1 (by default), 
#and ends at a specified number.
list(range(5))


# In[4]:


list(range(0,10,2))


# In[6]:


number = list(range(10))
sum = 0;
for x in number:
    sum += x
print(sum)


# In[15]:


#the modulo operator is used to determine the remainder of the divide between two number
print(7%2)


# In[30]:


x = int(input("please enter number :"))
check_number = list(range(2,int(x/2+1)))
for i in check_number:
    if(x % i == 0):
        print(x," isn't the prime number")
        break
else:
    print(x," is the prime number")
    


# In[ ]:





# In[ ]:




