#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np


# In[4]:


data = pd.read_csv('reviews_Digital_Music.csv')


# 1.1.1 Random Pick

# In[6]:


random_subset = data.sample(n=6)
random_subset


# 1.1.2 Rating

# In[14]:


random_song1 = data[(data.iloc[:,1]=='B0011Z3DN4')]
rating_random_song1= np.average(random_song1.iloc[:,4])
rating_random_song1


# In[15]:


random_song2 = data[(data.iloc[:,1]=='B009D9L77Y')]
rating_random_song2= np.average(random_song2.iloc[:,4])
rating_random_song2


# In[16]:


random_song3 = data[(data.iloc[:,1]=='B007DIQAXI')]
rating_random_song3= np.average(random_song3.iloc[:,4])
rating_random_song3


# In[17]:


random_song4 = data[(data.iloc[:,1]=='B001AJFE5G')]
rating_random_song4= np.average(random_song4.iloc[:,4])
rating_random_song4


# In[18]:


random_song5 = data[(data.iloc[:,1]=='B00CAZOHDO')]
rating_random_song5= np.average(random_song5.iloc[:,4])
rating_random_song5


# In[19]:


random_song6 = data[(data.iloc[:,1]=='B007B6VOKQ')]
rating_random_song6= np.average(random_song6.iloc[:,4])
rating_random_song6


# In[22]:


rating_of_random_playlist = (rating_random_song1+rating_random_song2+rating_random_song3+rating_random_song4+rating_random_song5+rating_random_song6)/6


# In[24]:


print('Average rating of ramdom playlist is', rating_of_random_playlist)


# 1.1.3 Get Category

# In[ ]:


# Category of B007DIQAXI is Rock.
# Category of B00CAZOHDO is Rock.


# 1.2.1 Random Pick

# In[84]:


random_subset2 = data.sample(n=6)
random_subset2


# 1.2.2 Rating

# In[10]:


random2_song1 = data[(data.iloc[:,1]=='B00136LUKO')]
rating_random2_song1= np.average(random2_song1.iloc[:,4])
random2_song2 = data[(data.iloc[:,1]=='B008FOQH6Y')]
rating_random2_song2= np.average(random2_song2.iloc[:,4])
random2_song3 = data[(data.iloc[:,1]=='B008CWEPDG')]
rating_random2_song3= np.average(random2_song3.iloc[:,4])
random2_song4 = data[(data.iloc[:,1]=='B00GD2L59O')]
rating_random2_song4= np.average(random2_song4.iloc[:,4])
random2_song5 = data[(data.iloc[:,1]=='B001G93Z5Q')]
rating_random2_song5= np.average(random2_song5.iloc[:,4])
random2_song6 = data[(data.iloc[:,1]=='B00005A8MT')]
rating_random2_song6= np.average(random2_song6.iloc[:,4])
rating_of_random_playlist2 = (rating_random2_song1+rating_random2_song2+rating_random2_song3+rating_random2_song4+rating_random2_song5+rating_random2_song6)/6
print('Average rating of ramdom playlist2 is', rating_of_random_playlist2)
print(rating_random2_song1,rating_random2_song2,rating_random2_song3,rating_random2_song4,rating_random2_song5,rating_random2_song6)


# 1.3.1 Random Pick

# In[86]:


random_subset3 = data.sample(n=6)
random_subset3


# 1.3.2 Rating

# In[11]:


random3_song1 = data[(data.iloc[:,1]=='B000005AM7')]
rating_random3_song1= np.average(random3_song1.iloc[:,4])
random3_song2 = data[(data.iloc[:,1]=='B008P5MLL8')]
rating_random3_song2= np.average(random3_song2.iloc[:,4])
random3_song3 = data[(data.iloc[:,1]=='B004H6QJVC')]
rating_random3_song3= np.average(random3_song3.iloc[:,4])
random3_song4 = data[(data.iloc[:,1]=='B0027WNRNQ')]
rating_random3_song4= np.average(random3_song4.iloc[:,4])
random3_song5 = data[(data.iloc[:,1]=='B00E9E4EC8')]
rating_random3_song5= np.average(random3_song5.iloc[:,4])
random3_song6 = data[(data.iloc[:,1]=='B0000026WD')]
rating_random3_song6= np.average(random3_song6.iloc[:,4])
rating_of_random_playlist3 = (rating_random3_song1+rating_random3_song2+rating_random3_song3+rating_random3_song4+rating_random3_song5+rating_random3_song6)/6
print('Average rating of ramdom playlist3 is', rating_of_random_playlist3)
print(rating_random3_song1,rating_random3_song2,rating_random3_song3,rating_random3_song4,rating_random3_song5,rating_random3_song6)


# 1.3.3 Get Category

# In[7]:


# Category of B000005AM7 is Dance & Electronic.
# Category of B0027WNRNQ is Dance Pop.
# Category of B00E9E4EC8 is Country Music.
# Category of B0000026WD is Blues.


# 1.4.1 Random Pick

# In[90]:


random_subset4 = data.sample(n=6)
random_subset4


# 1.4.2 Rating

# In[12]:


random4_song1 = data[(data.iloc[:,1]=='B0092YPJDI')]
rating_random4_song1= np.average(random4_song1.iloc[:,4])
random4_song2 = data[(data.iloc[:,1]=='B0002W4T4O')]
rating_random4_song2= np.average(random4_song2.iloc[:,4])
random4_song3 = data[(data.iloc[:,1]=='B000VT7AF8')]
rating_random4_song3= np.average(random4_song3.iloc[:,4])
random4_song4 = data[(data.iloc[:,1]=='B00005ICAW')]
rating_random4_song4= np.average(random4_song4.iloc[:,4])
random4_song5 = data[(data.iloc[:,1]=='B00A0A5A6Y')]
rating_random4_song5= np.average(random4_song5.iloc[:,4])
random4_song6 = data[(data.iloc[:,1]=='B0006ZQ9BS')]
rating_random4_song6= np.average(random4_song6.iloc[:,4])
rating_of_random_playlist4 = (rating_random4_song1+rating_random4_song2+rating_random4_song3+rating_random4_song4+rating_random4_song5+rating_random4_song6)/6
print('Average rating of ramdom playlist4 is', rating_of_random_playlist4)
print(rating_random4_song1,rating_random4_song2,rating_random4_song3,rating_random4_song4,rating_random4_song5,rating_random4_song6)


# 1.4.3 Get Category

# In[8]:


# Category of B0002W4T4O is Pop Music.
# Category of B00005ICAW is Hardcore & Punk.


# 1.5.1 Random Pick

# In[93]:


random_subset5 = data.sample(n=6)
random_subset5


# 1.5.2 Rating

# In[14]:


random5_song1 = data[(data.iloc[:,1]=='B00000AGMC')]
rating_random5_song1= np.average(random5_song1.iloc[:,4])
random5_song2 = data[(data.iloc[:,1]=='B003U7V8PG')]
rating_random5_song2= np.average(random5_song2.iloc[:,4])
random5_song3 = data[(data.iloc[:,1]=='B00123HPUC')]
rating_random5_song3= np.average(random5_song3.iloc[:,4])
random5_song4 = data[(data.iloc[:,1]=='B00014TQ7S')]
rating_random5_song4= np.average(random5_song4.iloc[:,4])
random5_song5 = data[(data.iloc[:,1]=='B000W1MDAM')]
rating_random5_song5= np.average(random5_song5.iloc[:,4])
random5_song6 = data[(data.iloc[:,1]=='B008K9SG9K')]
rating_random5_song6= np.average(random5_song6.iloc[:,4])
rating_of_random_playlist5 = (rating_random5_song1+rating_random5_song2+rating_random5_song3+rating_random5_song4+rating_random5_song5+rating_random5_song6)/6
print('Average rating of ramdom playlist5 is', rating_of_random_playlist5)
print(rating_random5_song1,rating_random5_song2,rating_random5_song3,rating_random5_song4,rating_random5_song5,rating_random5_song6)


# In[ ]:




