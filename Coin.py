#!/usr/bin/env python
# coding: utf-8

# In[2]:


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start': '1',
    'limit': '5000',
    'convert': 'USD'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '1caae7dd-57b6-40b4-89a6-05971ebdc0ee',
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    # data is a dictionary
    #data_df = pd.DataFrame.from_dict(data=data, orient='index')
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)


# In[3]:


type(data)


# In[4]:


len(data)


# In[7]:


data.keys()


# In[8]:


data['status']


# In[10]:


data['data'][0]


# In[11]:


type(data['data'][0])


# In[12]:


Bitcoin = data['data'][0]


# In[13]:


Bitcoin.keys()


# In[14]:


Bitcoin['quote']


# In[15]:


type(Bitcoin['quote'])


# In[16]:


Bitcoin['quote'].keys()


# In[17]:


Bitcoin['quote']['USD']


# In[18]:


Bitcoin['quote']['USD']['price']


# In[22]:


data['data'][0]['quote']['USD']['price']


# In[23]:


len(data['data'])


# In[29]:


type(data['data'])


# In[33]:


data['data'][1]


# In[38]:


pd.DataFrame.from_dict(data['data'][0]['quote']['USD'],orient='index')


# In[39]:


with open('convert.txt', 'w') as convert_file:
     convert_file.write(json.dumps(data))


# In[ ]:




