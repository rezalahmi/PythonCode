#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


vector_1 = np.random.randint(1,500,5)
vector_1


# In[3]:


vector_2 = np.random.randint(1,500,5)
vector_2


# In[23]:


vector_1.dot(vector_2)


# In[24]:


#Return the dot product of two vectors.
np.vdot(vector_1,vector_2)


# In[ ]:





# In[10]:


#Generate a 2 x 2 array of ints between 0 and 9
matrix_1 = np.random.randint(10,size=(2,2))
matrix_1


# In[11]:


matrix_2 = np.random.randint(10,size=(2,2))
matrix_2


# In[12]:


matrix_1.dot(matrix_2)


# In[14]:


matrix_3 = np.matrix(np.random.randint(10,size=(3,2)))
matrix_3


# In[15]:


np.dot(matrix_3,matrix_2)


# In[17]:


#dot(a, b)[i,j,k,m] = sum(a[i,j,:] * b[k,:,m])
np.dot(matrix_3,matrix_2)[2,1]


# In[18]:


#Return the identity array.
#The identity array is a square array with ones on the main diagonal.
np.identity(4)


# In[19]:


matrix_d = np.random.randint(10,size=(4,4))
matrix_d


# In[20]:


np.dot(matrix_d,np.identity(4))


# In[21]:


#numpy.linalg.inv
#Compute the (multiplicative) inverse of a matrix.
matrix_e = np.linalg.inv(matrix_d)
matrix_e


# In[22]:


np.dot(matrix_d,matrix_e)


# In[25]:


#numpy.matmul
#If both arguments are 2-D they are multiplied like conventional matrices.
np.matmul(matrix_3,matrix_2)


# In[26]:


#the determinant is a scalar value that is a function of the entries of a square matrix. 
#It allows characterizing some properties of the matrix and the linear map represented by the matrix.
#In particular, the determinant is nonzero if and only if the matrix is invertible, 
#and the linear map represented by the matrix is an isomorphism.
#linalg.det(a)
np.linalg.det(matrix_d)

