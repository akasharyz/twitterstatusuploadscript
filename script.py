#import 
import tweepy
import time
import os

# credentials to login to twitter api
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

# login to twitter account api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

#Access to the folder post
os.chdir('post')

# iterates over pictures in post folder
for posts in os.listdir('.'):
    api.update_with_media(posts, status="Enter the status here")
    time.sleep(10)
 
