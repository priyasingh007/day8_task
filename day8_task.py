#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[12]:


df=pd.read_csv(r"D:\Downloads\heart.csv")
df


# In[18]:


df.shape


# In[13]:


df.head()


# In[14]:


df.tail()


# In[19]:


df[df.duplicated()]


# In[20]:


df.drop_duplicates(inplace=True)
df.reset_index(drop=True, inplace=True)
df.shape


# In[21]:


df.describe()


# In[22]:


df.isnull().sum()


# In[ ]:




