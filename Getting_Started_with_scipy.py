#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install scipy


# In[2]:


from scipy.spatial import distance
distance.minkowski([1, 0, 0], [0, 1, 0], 1)


# In[4]:


distance.minkowski([1, 0, 0], [0, 1, 0], 2)


# In[7]:


distance.cosine([1, 0, 0], [0, 1, 0])


# In[6]:


from scipy import stats
import numpy as np
a = np.array([0, 0, 0, 1, 1, 1, 1])
b = np.arange(7)
stats.pearsonr(a, b)


# In[ ]:




