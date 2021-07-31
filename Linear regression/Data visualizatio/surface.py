#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np

# In[13]:


a=np.arange(-1,1,0.02)
b=a


# In[14]:


a,b=np.meshgrid(a,b)


# In[15]:


fig=plt.figure()
axes=fig.gca(projection='3d')
axes.plot_surface(a,b,a**2 +b**2,cmap='rainbow')
plt.show()
print('run')

# In[ ]:




