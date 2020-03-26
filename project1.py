#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import pandas as pd
a="mukesh"
a


# In[7]:


a1=pd.Series([98,100],['maths','science'])
a1


# In[8]:


b="rupesh"
b


# In[9]:


b1=pd.Series([99,99],['maths','science'])
b1


# In[10]:


c="akash"
c


# In[11]:


c1=pd.Series([12,13],['maths','science'])
c1


# In[18]:


d=np.array([(98,100),(99,99),(12,13)])
df=pd.DataFrame(d,[a,b,c],['maths','science'])
df


# In[14]:


"passed students :"


# In[15]:


df.head(2)


# In[16]:


"failed student :"


# In[19]:


df.tail(1)


# In[ ]:




