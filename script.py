# gyanopedia

import tweepy as tp
import time
import os

# credentials to login to twitter api
consumer_key = '1roOi997X7szhlmlLSc9G3hlK'
consumer_secret = '5MHUURM4J87t9yk6OhaMKrxiqSwNzMBp5UlYceGKHbehCbE1xr'
access_token = '853178510-cbisRmYB2ZUejYJpDmonZNmy4RotRywX9Cwvk25b'
access_secret = 'xeTVetuWC3j9zBVyHdwHOJrOZKtvBrmkN8YR2utBosTp6'

# login to twitter account api
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

os.chdir('post')

# iterates over pictures in models folder
for posts in os.listdir('.'):
    api.update_with_media(posts, status="#gyanopedia #twitter #facts #test")
    time.sleep(10)
 
