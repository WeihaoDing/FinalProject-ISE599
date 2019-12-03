#!/usr/bin/env python
# coding: utf-8

# In[48]:


import pandas as pd
import numpy as np


# In[49]:


data = pd.read_csv('reviews_Digital_Music.csv')


# In[50]:


data[:5]


# 1.Classic Playlist

# In[51]:


search_classic = data[data[" reviewText"].str.contains('classic')==True]


# In[52]:


search_classic[:5]


# In[53]:


rating_by_overall=search_classic.groupby([' asin']).aggregate({" overall":"mean"})


# In[54]:


rating_by_overall[:10]


# In[55]:


rating_by_overall.sort_values(by=[' overall'], ascending=False)[0:3]


# In[56]:


# also bought B0030G731A: 'B001DADZTE', 'B001NB1P7W', 'B001NB6NO2', 'B0030DHBWE', 'B001NB1M7A', 'B001NB8LV0', 'B00137IL5U'


# In[57]:


rating_song1 = np.average(data[(data.iloc[:,1]=='B001DADZTE')].iloc[:,4])
rating_song2 = np.average(data[(data.iloc[:,1]=='B001NB1P7W')].iloc[:,4])
rating_song3 = np.average(data[(data.iloc[:,1]=='B001NB6NO2')].iloc[:,4])
rating_song4 = np.average(data[(data.iloc[:,1]=='B0030DHBWE')].iloc[:,4])
rating_song5 = np.average(data[(data.iloc[:,1]=='B001NB1M7A')].iloc[:,4])
rating_song6 = np.average(data[(data.iloc[:,1]=='B001NB8LV0')].iloc[:,4])
rating_song7 = np.average(data[(data.iloc[:,1]=='B00137IL5U')].iloc[:,4])

list_of_rating = [rating_song1,rating_song2,rating_song3,rating_song4,rating_song5,rating_song6,rating_song7]
print(list_of_rating)


# Choose high rating songs to create classical playlist:
#     B0030G731A, B00137IL5U, B001NB1M7A, B001NB6NO2, B001NB8LV0, B001NB1P7W

# In[58]:


avg_rating_classic = (5.0+5.0+4.909090909090909+4.888888888888889+4.571428571428571+4.333333333333333)/6
print(avg_rating_classic)


# 2.Cowboy List

# In[59]:


search_cowboy = data[data[" reviewText"].str.contains('cowboy')==True]
rating_by_overall=search_cowboy.groupby([' asin']).aggregate({" overall":"mean"})
rating_by_overall.sort_values(by=[' overall'], ascending=False)[0:3]


# In[60]:


# also bought B001NCINQW: 'B00449PNXM', 'B0035QF02E', 'B002FVMARS', 'B0035QF0A6', 'B001NB1JA0', 'B0066D91S2', 'B005XVBJHO'


# In[61]:


rating_songc1 = np.average(data[(data.iloc[:,1]=='B00449PNXM')].iloc[:,4])
rating_songc2 = np.average(data[(data.iloc[:,1]=='B0035QF02E')].iloc[:,4])
rating_songc3 = np.average(data[(data.iloc[:,1]=='B002FVMARS')].iloc[:,4])
rating_songc4 = np.average(data[(data.iloc[:,1]=='B0035QF0A6')].iloc[:,4])
rating_songc5 = np.average(data[(data.iloc[:,1]=='B001NB1JA0')].iloc[:,4])
rating_songc6 = np.average(data[(data.iloc[:,1]=='B0066D91S2')].iloc[:,4])
rating_songc7 = np.average(data[(data.iloc[:,1]=='B005XVBJHO')].iloc[:,4])

list_of_ratingc = [rating_songc1,rating_songc2,rating_songc3,rating_songc4,rating_songc5,rating_songc6,rating_songc7]
print(list_of_ratingc)


# Choose high rating songs to create cowboy playlist:
#     B001NCINQW, B005XVBJHO, B001NB1JA0, B00449PNXM, B0035QF0A6, B0035QF02E

# In[62]:


avg_rating_cowboy = (5.0+5.0+5.0+4.9375+4.375+4.0)/6
print(avg_rating_cowboy)


# 3.Dreamy List

# In[63]:


search_dreamy = data[data[" reviewText"].str.contains('dreamy')==True]
rating_by_overall3=search_dreamy.groupby([' asin']).aggregate({" overall":"mean"})
rating_by_overall3.sort_values(by=[' overall'], ascending=False)[0:7]


# In[64]:


# also bought B0050CJNJ2: 'B002WIDRM6', 'B0014CBXOK', 'B00BPWDMP2', 'B0097RFAJI', 'B00FMVV326', 'B003ZDZ1WG', 'B00BD4K1PQ'


# In[65]:


rating_songd1 = np.average(data[(data.iloc[:,1]=='B002WIDRM6')].iloc[:,4])
rating_songd2 = np.average(data[(data.iloc[:,1]=='B0014CBXOK')].iloc[:,4])
rating_songd3 = np.average(data[(data.iloc[:,1]=='B00BPWDMP2')].iloc[:,4])
rating_songd4 = np.average(data[(data.iloc[:,1]=='B0097RFAJI')].iloc[:,4])
rating_songd5 = np.average(data[(data.iloc[:,1]=='B00FMVV326')].iloc[:,4])
rating_songd6 = np.average(data[(data.iloc[:,1]=='B003ZDZ1WG')].iloc[:,4])
rating_songd7 = np.average(data[(data.iloc[:,1]=='B00BD4K1PQ')].iloc[:,4])
list_of_ratingd = [rating_songd1,rating_songd2,rating_songd3,rating_songd4,rating_songd5,rating_songd6,rating_songd7]
print(list_of_ratingd)


# Choose high rating songs to create dreamy playlist: B0050CJNJ2, B002WIDRM6

# In[66]:


avg_rating_dreamy = (5.0+4.563291139240507)/2
print(avg_rating_dreamy)


# 4.Rocks Playlist

# In[67]:


search_rocks = data[data[" reviewText"].str.contains('rocks')==True]
rating_by_overall4=search_rocks.groupby([' asin']).aggregate({" overall":"mean"})
rating_by_overall4.sort_values(by=[' overall'], ascending=False)[:1]


# In[68]:


# also bought B001KQICK8: 'B0011Z0YR2', 'B0064Y5ZBU', 'B0011Z1DPY', 'B0016OAM70', 'B0011ZR9IE', 'B0043CKUAQ', 'B00149F6R8'


# In[69]:


rating_songr1 = np.average(data[(data.iloc[:,1]=='B0011Z0YR2')].iloc[:,4])
rating_songr2 = np.average(data[(data.iloc[:,1]=='B0064Y5ZBU')].iloc[:,4])
rating_songr3 = np.average(data[(data.iloc[:,1]=='B0011Z1DPY')].iloc[:,4])
rating_songr4 = np.average(data[(data.iloc[:,1]=='B0016OAM70')].iloc[:,4])
rating_songr5 = np.average(data[(data.iloc[:,1]=='B0011ZR9IE')].iloc[:,4])
rating_songr6 = np.average(data[(data.iloc[:,1]=='B0043CKUAQ')].iloc[:,4])
rating_songr7 = np.average(data[(data.iloc[:,1]=='B00149F6R8')].iloc[:,4])

list_of_ratingr = [rating_songr1,rating_songr2,rating_songr3,rating_songr4,rating_songr5,rating_songr6,rating_songr7]
print(list_of_ratingr)


# Choose high rating songs to create rocks playlist: B001KQICK8, B0064Y5ZBU, B0016OAM70, B0011Z0YR2, B0043CKUAQ, B0011Z1DPY

# In[43]:


avg_rating_rocks = (5.0+4.75+4.733333333333333+4.548387096774194+4.35+4.25)/6
avg_rating_rocks


# 5.Christmas Playlist

# In[74]:


search_chris = data[data[" reviewText"].str.contains('christmas')==True]
rating_by_overall5=search_rocks.groupby([' asin']).aggregate({" overall":"mean"})
rating_by_overall5.sort_values(by=[' overall'], ascending=False)[0:6]


# In[115]:


# also bought B003WZ7QEI: 'B000VRSXII', 'B000VRPDFO', 'B000X6PY8E', 'B003LLPZ6Y', 'B001JQE9AG', 'B0016OAM70', 'B001OGPVI0', 'B0092MJB0M'


# In[79]:


rating_songs1 = np.average(data[(data.iloc[:,1]=='B000VRSXII')].iloc[:,4])
rating_songs2 = np.average(data[(data.iloc[:,1]=='B000VRPDFO')].iloc[:,4])
rating_songs3 = np.average(data[(data.iloc[:,1]=='B000X6PY8E')].iloc[:,4])
rating_songs4 = np.average(data[(data.iloc[:,1]=='B003LLPZ6Y')].iloc[:,4])
rating_songs5 = np.average(data[(data.iloc[:,1]=='B001JQE9AG')].iloc[:,4])
rating_songs6 = np.average(data[(data.iloc[:,1]=='B0016OAM70')].iloc[:,4])
rating_songs7 = np.average(data[(data.iloc[:,1]=='B001OGPVI0')].iloc[:,4])
rating_songs8 = np.average(data[(data.iloc[:,1]=='B0092MJB0M')].iloc[:,4])
list_of_ratings = [rating_songs1,rating_songs2,rating_songs3,rating_songs4,rating_songs5,rating_songs6,rating_songs7,rating_song8]
print(list_of_ratings)


# Choose high rating songs to create christmas playlist: B003WZ7QEI, B000VRSXII, B001OGPVI0, B001JQE9AG, B0016OAM70, B000X6PY8E 

# In[80]:


avg_rating_christmas = (5.0+5.0+5.0+5.0+4.75+4.5)/6
print(avg_rating_christmas)


# In[ ]:




