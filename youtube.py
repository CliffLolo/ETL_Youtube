#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install google-api-python-client')
get_ipython().system('conda install pandas')


# In[ ]:


import os
import csv
import json

from googleapiclient.discovery import build

print("Packages imported successfully.")


# In[ ]:


api_key = os.environ.get('YOUTUBE_V3_API_KEY')

#api_key = ""
api_version='V3'

# TODO: Create a module that keeps keys. This can be imported.

youtube = build('youtube', api_version, developerKey=api_key)

print("API parameters set successfully.")


# In[ ]:


search_rate_limit = 5

print("Search Rate Limit has been set to {0}.".format(search_rate_limit))


# In[ ]:


allItems = []
count = 0

query = '#endsars'
max_results = 50
nextPage_token = None

while (count < search_rate_limit) and 1:
    searchRequest = youtube.search().list(
        part='snippet',
        type='video',
        q=query,
        videoDuration='medium',
        publishedAfter='2020-01-01T00:00:00Z',
        maxResults=max_results,
        pageToken=nextPage_token
    )

    searchResponse = searchRequest.execute()

    allItems += searchResponse['items']

    nextPage_token = searchResponse.get('nextPageToken')

    count += 1

    if nextPage_token is None:
        break
    
print("Total numer of items: {0}".format(len(allItems)))

# TODO: 
# 1. Show only success message. Handle Exceptions
# 2. Place code into function


# In[ ]:


videosIds = list(map(lambda x:x['id']['videoId'], allItems))

print("{0} video IDs was extracted succesfully.".format(len(videosIds)))


# In[ ]:


allVideoItems = []
count = 0

nextPage_token = None

while (count < len(videosIds)) and 1: 
    videosRequest = youtube.videos().list(
        part='snippet, statistics',
        id=",".join(videosIds[count:count+50]),
    )

    videosResponse = videosRequest.execute()
    
    allVideoItems += videosResponse['items']
    
    count+=50
    
print("Total numer of items: {0}".format(len(allVideoItems)))

# TODO: Show only success message. Handle Exceptions


# In[ ]:


video_id = []
video_title = []
video_desc = []
time_published = []
thumbnail_url = []
view_count = []
like_count = []
dislike_count = []
comments_count = []
video_url = []

for i in allVideoItems:
    video_id.append(i['id'])
    video_title.append(i['snippet']['title'])
    video_desc.append(i['snippet']['description'])
    time_published.append(i['snippet']['publishedAt'])  
    thumbnail_url.append(i['snippet']['thumbnails']['default']['url'])
    
    view_count.append(i['statistics'].get('viewCount'))
    like_count.append(i['statistics'].get('likeCount'))
    dislike_count.append(i['statistics'].get('dislikeCount'))
    comments_count.append(i['statistics'].get('commentCount'))
    
    video_url.append("https://www.youtube.com/watch?v=" + i['id'])

print("Data extracted successfully.")

# TODO: Handle nonType being assigned instead of number or string


# In[ ]:


import pandas as pd

data = {
    'videoId': video_id,
    'tltle': video_title,
    'description': video_desc,
    'timePublished': time_published,
    'thumnailUrl': thumbnail_url,
    'views': view_count,
    'likes': like_count,
    'dislikes': dislike_count,
    'comments': comments_count,
    'videoUrl': video_url
}

df = pd.DataFrame(data)

df.head()


# In[ ]:


import time

current_timestamp = time.strftime("%Y%m%d-%H%M%S")
file_name = current_timestamp+"_youtube_data.csv"
df.to_csv(file_name, index=False)

print("File created successfully. File name is {0}".format(file_name))
# TODO: Handle Error exceptions


# In[ ]:




