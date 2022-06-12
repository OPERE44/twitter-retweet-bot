# import dependencies
import tweepy
from config import *
import time

#Authenticate the twitter api  
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Hashtag to search for
search = '#python, #javascript'
Tweets = 500


for tweet in tweepy.Cursor(api.search_tweets, search).items(Tweets):
    try:
        tweet.retweet()
        print("Retweeted the tweet")
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e)