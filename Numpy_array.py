#!/usr/bin/env python
# coding: utf-8

# In[2]:


#NumPy is a Python library used for working with arrays.
#It also has functions for working in domain of linear algebra, fourier transform, and matrices.
#NumPy stands for Numerical Python.
import numpy as np


# In[9]:


print(np.__version__)


# In[3]:


array1 = np.array([1,2,3,4,5,6])


# In[4]:


array1


# In[5]:


#You can access an array element by referring to its index number.
#The indexes in NumPy arrays start with 0, 
#meaning that the first element has index 0, and the second has index 1 etc.
array1[0]


# In[6]:


array1.size


# In[7]:


array1.ndim


# In[8]:


array1.shape


# In[10]:


print(type(array1))


# In[11]:


#To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, 
#and it will be converted into an ndarray
array2 = np.array((9,8,7,6,5,4))


# In[12]:


array2


# In[14]:


array1+array2


# In[15]:


array1*array2


# In[16]:


#Getting some elements out of an existing array and 
#creating a new array out of them is called filtering
#In NumPy, you filter an array using a boolean index list.
array2 > 7


# In[17]:


array2[array2>7]


# In[18]:


array2[array2<7]


# In[19]:


array2 % 2 == 0


# In[20]:


array2[array2 % 2 == 0]


# In[21]:


#numpy.where(condition[, x, y])
#An array with elements from x where condition is True, and elements from y elsewhere.
np.where(array1==3)


# In[22]:


np.where(array1 >=3)


# In[23]:


np.where(array1 >=3,array1/3,array1)


# In[25]:


np.where(array1==3,array1/3,array1*2)


# In[32]:


#we use & when working with numpy array insted of and
array1[(array1>2) & (array1<6)]


# In[27]:


#Compute the truth value of x1 AND x2 element-wise.
#umpy.logical_and(x1, x2)
np.logical_and(array1>2,array1<6)


# In[28]:


array1[np.logical_and(array1>2,array1<6)]


# In[33]:


array1[(array1>2) & (array1<6) & (array1 % 2 != 0)]


# In[34]:


np.logical_or(array1%2==0,array1==3)


# In[35]:


array1[np.logical_or(array1%2==0,array1==3)]


# In[37]:


#be carefull just like and, we use | for logical or
array1[(array1%2==0)|(array1==3)]


# In[1]:


import numpy as np


# In[2]:


array_1 = np.array(["reza","raheleh","hadi","eli","reza"])
print(array_1)


# In[3]:


array_1_clean = np.unique(array_1)


# In[4]:


print(array_1_clean)


# In[5]:


#if you want to know is there an entry on the one direction array, use in1d method
np.in1d("reza",array_1)


# In[6]:


np.in1d("ali",array_1)


# In[3]:


#two dimension
array_2 = np.array(([1,2,3],[2,3,4],[3,4,5],[4,5,6]))
array_2


# In[9]:


array_2[1]


# In[20]:


array_2[1,1]


# In[11]:


array_2.ndim


# In[12]:


array_2.shape


# In[13]:


array_2.size


# In[15]:


#In this array the innermost dimension (5th dim) has 4 elements, 
#the 4th dim has 1 element that is the vector, 
#the 3rd dim has 1 element that is the matrix with the vector, 
#the 2nd dim has 1 element that is 3D array and 1st dim has 1 element that is a 4D array.
array_3 = np.array([1,2,3,4],ndmin=5)
array_3


# In[16]:


print(array_3)


# In[17]:


array_3.ndim


# In[19]:


array_3[0]


# In[22]:


array_3[0,0,0,0,2]


# In[23]:


array_2


# In[24]:


#Use negative indexing to access an array from the end.
array_2[1,-1]


# In[35]:


#Slicing in python means taking elements from one given index to another given index
#We pass slice instead of index like this: [start:end].
#We can also define the step, like this: [start:end:step].
array_4 = np.array([1, 2, 3, 4, 5, 6, 7])

print(array_4[1:5])
print(array_4[2:])
print(array_4[:2])
print(array_4[-3:-1])
print(array_4[1:5:2])
print(array_4[::2])


# In[41]:


array_5 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(array_5)
print(array_5[1, 1:4])
print(array_5[0:2,2])
print(array_5[0:2,2:4])


# In[42]:


#The best way to change the data type of an existing array, 
#is to make a copy of the array with the astype() method.
array_6 = np.array([1.1,2.1,3.1])
array_6


# In[43]:


new_array_6 = array_6.astype(int)
new_array_6


# In[44]:


#The copy owns the data and any changes made to the copy will not affect original array,
#and any changes made to the original array will not affect the copy.
array_7 = array_6.copy()
print(array_7)
array_7[0] = 37
print(array_6)
print(array_7)


# In[46]:


array_7 = array_6.view()
print(array_7)
array_7[0] = 37
print(array_6)
print(array_7)
array_6[1] = 73
print(array_6)
print(array_7)


# In[47]:


#Every NumPy array has the attribute base that returns None if the array owns the data.
#Otherwise, the base  attribute refers to the original object.
print(array_6.base)
print(array_7.base)


# In[48]:


#The shape of an array is the number of elements in each dimension.
#By reshaping we can add or remove dimensions or change number of elements in each dimension.
array_6 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
array_6.shape


# In[49]:


array_6.reshape(2,6)


# In[50]:


array_6.reshape(6,2)


# In[53]:


array_6.reshape(2,2,3)


# In[54]:


print(array_6.reshape(2,2,3).base)


# In[56]:


#You are allowed to have one "unknown" dimension.
#Meaning that you do not have to specify an exact number for one of 
#the dimensions in the reshape method.
#Pass -1 as the value, and NumPy will calculate this number for you.
array_6.reshape(2,1,-1)


# In[59]:


array_6.reshape(-1,1,4)


# In[60]:


#Flattening array means converting a multidimensional array into a 1D array.
#We can use reshape(-1) to do this.
print(array_5)
new_array_5 = array_5.reshape(-1)
print(new_array_5)


# In[9]:


#Iterating means going through elements one by one.
for x in array_1:
    print(x)


# In[5]:


for x in array_2:
    print(x)


# In[6]:


for x in array_2:
    for y in x:
        print(y)


# In[7]:


#The function nditer() is a helping function that can be used from 
#very basic to very advanced iterations
#In basic for loops, iterating through each scalar of an array we need to use n for 
#loops which can be difficult to write for arrays with very high dimensionality.
for x in np.nditer(array_2):
    print(x)


# In[11]:


#Enumeration means mentioning sequence number of somethings one by one.
#Sometimes we require corresponding index of the element while iterating, 
#the ndenumerate() method can be used for those usecases.
for i,x in np.ndenumerate(array_2):
    print(i,x)


# In[13]:


#Joining means putting contents of two or more arrays in a single array.
#In SQL we join tables based on a key, whereas in NumPy we join arrays by axes.
#We pass a sequence of arrays that we want to join to the concatenate() function, 
#along with the axis
array_1 = np.array([1,2,3])
array_2 = np.array([4,5,6])
array_3 = np.concatenate((array_1,array_2))
print(array_3)


# In[14]:


arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=0)
print(arr)


# In[15]:


arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)
print(arr)


# In[20]:


#Splitting is reverse operation of Joining.
#Joining merges multiple arrays into one and Splitting breaks one array into multiple.
#We use array_split() for splitting arrays, 
#we pass it the array we want to split and the number of splits.
arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)


# In[21]:


newarr = np.array_split(arr, 4)

print(newarr)


# In[22]:


#If the array has less elements than required, it will adjust from the end accordingly.
newarr = np.array_split(arr, 7)

print(newarr)


# In[23]:


#The return value of the array_split() 
#method is an array containing each of the split as an array.
newarr = np.array_split(arr, 3)

print(newarr[0])
print(newarr[1])
print(newarr[2])


# In[26]:


#You can search an array for a certain value, and return the indexes that get a match.
#To search an array, use the where() method.
array_1 = np.array([1,2,3,4,2,3,6,7])
x = np.where(array_1==3)
type(x)


# In[28]:


for i in np.where(array_1==3):
    print(i)


# In[29]:


for i in np.where(array_1%2==0):
    print(i)


# In[30]:


#There is a method called searchsorted() which performs a binary search in the array, and returns 
#the index where the specified value would be inserted to maintain the search order.
#The searchsorted() method is assumed to be used on sorted arrays.
array_1 = np.array([1,2,3,4,5,6,7,8,9])
x = np.searchsorted(array_1,2)
print(x)


# In[31]:


x = np.searchsorted(array_1,[2,6,9])
print(x)


# In[32]:


#Sorting means putting elements in an ordered sequence.
#Ordered sequence is any sequence that has an order corresponding to elements, 
#like numeric or alphabetical, ascending or descending.
#The NumPy ndarray object has a function called sort(), that will sort a specified array.
array_1 = np.array([3,5,7,1,5,9,8,3,0,1,2])
new_array_1 = np.sort(array_1)
print(new_array_1)


# In[ ]:




