# ETL With Youtube Data
## Project Overview 
This script scrapes data from [Youtube](https://youtube.com/en). Results are saved into a csv file for further analysis.

*Tools used:*
- **jupyter noteboook**
- **Python 3.7**
- **google API Client**
- **pandas**

## Task

Write a script that extracts YouTube data to analyze the #endsars# trend that rocked the entire world.
The script should be able to perform the following:

* Filter out channels and playlists.
* Get only videos published this year.
* Include videos that are between 4 to 20 mins long.
* Generic such that the search query can be changed.

### Output

Store the output into a csv with the filename having the following format: current_timestamp_youtube_data.

The following video attributes should be a part of the dataset:

* the time video was published
* the video id
* the title of the video
* description
* the URL of the video thumbnail
* number of views
* number of likes
* number of dislikes
* number of comments

Create an additional the column that builds the video URL using the video id.


## SetUp
* Apply for a google developer account
* Clone this repo
* Create an environment using :
  ```
  conda create -n "env name" python=3.7
  
  ```
  
* Activate the environment using:

  ```
  conda activate "env name"
  ```
  
* Install Packages using:
  
  ```
  pip install -r requirements.txt 
  
  ```
  ### Store env variables

To store your API credentials:  

* Duplicate  ``` .env.example ``` file and create a new file name *.env*



## Resources used

* [Youtube V3 API - Getting Started](https://developers.google.com/youtube/v3/getting-started)
* [Google API Python Client Github](https://github.com/googleapis/google-api-python-client/blob/master/docs/start.md)
* [How to Extract & Analyze YouTube Data using YouTube API?](https://www.analyticssteps.com/blogs/how-extract-analyze-youtube-data-using-youtube-api)
