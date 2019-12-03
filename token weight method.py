#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


data = pd.read_csv('reviews_Digital_Music.csv')


# 1. Classic Playlist

# In[4]:


rate_classic1 = np.average(data[(data.iloc[:,1]=='B0026LWUCC')].iloc[:,4])
rate_classic2 = np.average(data[(data.iloc[:,1]=='B000V66H3M')].iloc[:,4])
rate_classic3 = np.average(data[(data.iloc[:,1]=='B00137RHT6')].iloc[:,4])
rate_classic4 = np.average(data[(data.iloc[:,1]=='B001EW8BAO')].iloc[:,4])
rate_classic5 = np.average(data[(data.iloc[:,1]=='B000W239UY')].iloc[:,4])
rate_classic6 = np.average(data[(data.iloc[:,1]=='B00171I5YO')].iloc[:,4])


# In[5]:


print(rate_classic1,rate_classic2,rate_classic3,rate_classic4,rate_classic5,rate_classic6)


# In[6]:


avg_classic = (rate_classic1+rate_classic2+rate_classic3+rate_classic4+rate_classic5+rate_classic6)/6
avg_classic


# 2. Cowboy Playlist

# In[8]:


rate_cowboy1 = np.average(data[(data.iloc[:,1]=='B000V66UV6')].iloc[:,4])
rate_cowboy2 = np.average(data[(data.iloc[:,1]=='B000SZDI42')].iloc[:,4])
rate_cowboy3 = np.average(data[(data.iloc[:,1]=='B000QNU0RY')].iloc[:,4])
rate_cowboy4 = np.average(data[(data.iloc[:,1]=='B002IEW504')].iloc[:,4])
rate_cowboy5 = np.average(data[(data.iloc[:,1]=='B00123HIPY')].iloc[:,4])
rate_cowboy6 = np.average(data[(data.iloc[:,1]=='B00B13OPB0')].iloc[:,4])


# In[9]:


print(rate_cowboy1,rate_cowboy2,rate_cowboy3,rate_cowboy4,rate_cowboy5,rate_cowboy6)


# In[10]:


avg_cowboy = (rate_cowboy1+rate_cowboy2+rate_cowboy3+rate_cowboy4+rate_cowboy5+rate_cowboy6)/6
avg_cowboy


# 3. Dreamy Playlist

# In[13]:


rate_dreamy1 = np.average(data[(data.iloc[:,1]=='B000HBKCDC')].iloc[:,4])
rate_dreamy2 = np.average(data[(data.iloc[:,1]=='B00BCYR8I0')].iloc[:,4])
rate_dreamy3 = np.average(data[(data.iloc[:,1]=='B001O3WF0U')].iloc[:,4])
rate_dreamy4 = np.average(data[(data.iloc[:,1]=='B001NB6P3Q')].iloc[:,4])
rate_dreamy5 = np.average(data[(data.iloc[:,1]=='B00DYFCYSO')].iloc[:,4])
rate_dreamy6 = np.average(data[(data.iloc[:,1]=='B0000025BA')].iloc[:,4])


# In[14]:


print(rate_dreamy1,rate_dreamy2,rate_dreamy3,rate_dreamy4,rate_dreamy5,rate_dreamy6)


# In[15]:


avg_dreamy = (rate_dreamy1+rate_dreamy2+rate_dreamy3+rate_dreamy4+rate_dreamy5+rate_dreamy6)/6
avg_dreamy


# 4. Rocks Playlist

# In[18]:


rate_rock1 = np.average(data[(data.iloc[:,1]=='B00GZ962A2')].iloc[:,4])
rate_rock2 = np.average(data[(data.iloc[:,1]=='B000VMYM5Q')].iloc[:,4])
rate_rock3 = np.average(data[(data.iloc[:,1]=='B00124HEFM')].iloc[:,4])
rate_rock4 = np.average(data[(data.iloc[:,1]=='B007XEHNUQ')].iloc[:,4])
rate_rock5 = np.average(data[(data.iloc[:,1]=='B00E9OGMPA')].iloc[:,4])
rate_rock6 = np.average(data[(data.iloc[:,1]=='B00GHJ6VME')].iloc[:,4])


# In[19]:


print(rate_rock1,rate_rock2,rate_rock3,rate_rock4,rate_rock5,rate_rock6)


# In[20]:


avg_rock = (rate_rock1+rate_rock2+rate_rock3+rate_rock4+rate_rock5+rate_rock6)/6
avg_rock


# 5. Christmas Playlist

# In[4]:


rate_chris1 = np.average(data[(data.iloc[:,1]=='B0026EYVR6')].iloc[:,4])
rate_chris2 = np.average(data[(data.iloc[:,1]=='B00H38MCFS')].iloc[:,4])
rate_chris3 = np.average(data[(data.iloc[:,1]=='B00A3GQW76')].iloc[:,4])
rate_chris4 = np.average(data[(data.iloc[:,1]=='B00BDNBZXY')].iloc[:,4])
rate_chris5 = np.average(data[(data.iloc[:,1]=='B001NCRRTG')].iloc[:,4])
rate_chris6 = np.average(data[(data.iloc[:,1]=='B00005ICAW')].iloc[:,4])


# In[5]:


print(rate_chris1,rate_chris2,rate_chris3,rate_chris4,rate_chris5,rate_chris6)


# In[7]:


avg_christmas = (rate_chris1+rate_chris2+rate_chris3+rate_chris4+rate_chris5+rate_chris6)/6
avg_christmas


# In[ ]:




