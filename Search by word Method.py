#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


data = pd.read_csv('reviews_Digital_Music.csv')


# In[3]:


data[:5]


# 1.Classic Playlist

# In[4]:


search_classic = data[data.iloc[:,3].str.contains('classic')==True]


# In[5]:


random_classic = search_classic.sample(n=6)
random_classic


# In[6]:


classic_song1 = data[(data.iloc[:,1]=='B000X9O7IE')]
rating_classic_song1= np.average(classic_song1.iloc[:,4])
classic_song2 = data[(data.iloc[:,1]=='B000002KH3')]
rating_classic_song2= np.average(classic_song2.iloc[:,4])
classic_song3 = data[(data.iloc[:,1]=='B000002KYU')]
rating_classic_song3= np.average(classic_song3.iloc[:,4])
classic_song4 = data[(data.iloc[:,1]=='B0000024IE')]
rating_classic_song4= np.average(classic_song4.iloc[:,4])
classic_song5 = data[(data.iloc[:,1]=='B004YMS6QU')]
rating_classic_song5= np.average(classic_song5.iloc[:,4])
classic_song6 = data[(data.iloc[:,1]=='B0013832A8')]
rating_classic_song6= np.average(classic_song6.iloc[:,4])
rating_of_classic_playlist = (rating_classic_song1+rating_classic_song2+rating_classic_song3+rating_classic_song4+rating_classic_song5+rating_classic_song6)/6
print('Average rating of classic playlist is', rating_of_classic_playlist)


# In[7]:


print(rating_classic_song1,rating_classic_song2,rating_classic_song3,rating_classic_song4,rating_classic_song5,rating_classic_song6)


# 2.Cowboy

# In[12]:


search_cowboy = data[data.iloc[:,3].str.contains('cowboy')==True]
random_cowboy = search_cowboy.sample(n=6)
random_cowboy


# In[8]:


cowboy_song1 = data[(data.iloc[:,1]=='B000002W7W')]
rating_cowboy_song1= np.average(cowboy_song1.iloc[:,4])
cowboy_song2 = data[(data.iloc[:,1]=='B0015AEKGE')]
rating_cowboy_song2= np.average(cowboy_song2.iloc[:,4])
cowboy_song3 = data[(data.iloc[:,1]=='B004BUFJS8')]
rating_cowboy_song3= np.average(cowboy_song3.iloc[:,4])
cowboy_song4 = data[(data.iloc[:,1]=='B005QJZ5FA')]
rating_cowboy_song4= np.average(cowboy_song4.iloc[:,4])
cowboy_song5 = data[(data.iloc[:,1]=='B002REWLV8')]
rating_cowboy_song5= np.average(cowboy_song5.iloc[:,4])
cowboy_song6 = data[(data.iloc[:,1]=='B00949YGM6')]
rating_cowboy_song6= np.average(cowboy_song6.iloc[:,4])
rating_of_cowboy_playlist = (rating_cowboy_song1+rating_cowboy_song2+rating_cowboy_song3+rating_cowboy_song4+rating_cowboy_song5+rating_cowboy_song6)/6
print('Average rating of cowboy playlist is', rating_of_cowboy_playlist)


# In[9]:


print(rating_cowboy_song1,rating_cowboy_song2,rating_cowboy_song3,rating_cowboy_song4,rating_cowboy_song5,rating_cowboy_song6)


# 3.Dreamy

# In[15]:


search_dreamy = data[data.iloc[:,3].str.contains('dreamy')==True]
random_dreamy = search_dreamy.sample(n=6)
random_dreamy


# In[10]:


dreamy_song1 = data[(data.iloc[:,1]=='B00006L852')]
rating_dreamy_song1= np.average(dreamy_song1.iloc[:,4])
dreamy_song2 = data[(data.iloc[:,1]=='B005QJZ5FA')]
rating_dreamy_song2= np.average(dreamy_song2.iloc[:,4])
dreamy_song3 = data[(data.iloc[:,1]=='B00001OH7M')]
rating_dreamy_song3= np.average(dreamy_song3.iloc[:,4])
dreamy_song4 = data[(data.iloc[:,1]=='B0007TFI56')]
rating_dreamy_song4= np.average(dreamy_song4.iloc[:,4])
dreamy_song5 = data[(data.iloc[:,1]=='B000058DXH')]
rating_dreamy_song5= np.average(dreamy_song5.iloc[:,4])
dreamy_song6 = data[(data.iloc[:,1]=='B002Q11RJO')]
rating_dreamy_song6= np.average(dreamy_song6.iloc[:,4])
rating_of_dreamy_playlist = (rating_dreamy_song1+rating_dreamy_song2+rating_dreamy_song3+rating_dreamy_song4+rating_dreamy_song5+rating_dreamy_song6)/6
print('Average rating of dreamy playlist is', rating_of_dreamy_playlist)


# In[11]:


print(rating_dreamy_song1,rating_dreamy_song2,rating_dreamy_song3,rating_dreamy_song4,rating_dreamy_song5,rating_dreamy_song6)


# 4.Rocks

# In[18]:


search_rocks = data[data.iloc[:,3].str.contains('rocks')==True]
random_rocks = search_rocks.sample(n=6)
random_rocks


# In[12]:


rocks_song1 = data[(data.iloc[:,1]=='B000WCDI5K')]
rating_rocks_song1= np.average(rocks_song1.iloc[:,4])
rocks_song2 = data[(data.iloc[:,1]=='B0000026CZ')]
rating_rocks_song2= np.average(rocks_song2.iloc[:,4])
rocks_song3 = data[(data.iloc[:,1]=='B006PZA7XY')]
rating_rocks_song3= np.average(rocks_song3.iloc[:,4])
rocks_song4 = data[(data.iloc[:,1]=='B005OH1IZ0')]
rating_rocks_song4= np.average(rocks_song4.iloc[:,4])
rocks_song5 = data[(data.iloc[:,1]=='B00137MM8W')]
rating_rocks_song5= np.average(rocks_song5.iloc[:,4])
rocks_song6 = data[(data.iloc[:,1]=='B00GTZ6O2S')]
rating_rocks_song6= np.average(rocks_song6.iloc[:,4])
rating_of_rocks_playlist = (rating_rocks_song1+rating_rocks_song2+rating_rocks_song3+rating_rocks_song4+rating_rocks_song5+rating_rocks_song6)/6
print('Average rating of rocks playlist is', rating_of_rocks_playlist)


# In[13]:


print(rating_rocks_song1,rating_rocks_song2,rating_rocks_song3,rating_rocks_song4,rating_rocks_song5,rating_rocks_song6)


# 5.Christmas

# In[20]:


search_christmas = data[data.iloc[:,3].str.contains('christmas ')==True]
random_christmas  = search_christmas.sample(n=6)
random_christmas 


# In[14]:


christmas_song1 = data[(data.iloc[:,1]=='B000QPLFZ8')]
rating_christmas_song1= np.average(christmas_song1.iloc[:,4])
christmas_song2 = data[(data.iloc[:,1]=='B006NO2WJ4')]
rating_christmas_song2= np.average(christmas_song2.iloc[:,4])
christmas_song3 = data[(data.iloc[:,1]=='B006NF68FC')]
rating_christmas_song3= np.average(christmas_song3.iloc[:,4])
christmas_song4 = data[(data.iloc[:,1]=='B00123D0CE')]
rating_christmas_song4= np.average(christmas_song4.iloc[:,4])
christmas_song5 = data[(data.iloc[:,1]=='B00A70VWVE')]
rating_christmas_song5= np.average(christmas_song5.iloc[:,4])
christmas_song6 = data[(data.iloc[:,1]=='B00065BYAY')]
rating_christmas_song6= np.average(christmas_song6.iloc[:,4])
rating_of_christmas_playlist = (rating_christmas_song1+rating_christmas_song2+rating_christmas_song3+rating_christmas_song4+rating_christmas_song5+rating_christmas_song6)/6
print('Average rating of christmas playlist is', rating_of_christmas_playlist)


# In[15]:


print(rating_christmas_song1,rating_christmas_song2,rating_christmas_song3,rating_christmas_song4,rating_christmas_song5,rating_christmas_song6)


# In[ ]:




