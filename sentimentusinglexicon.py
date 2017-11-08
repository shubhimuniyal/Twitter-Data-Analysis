import tweepy
from textblob import TextBlob

access_token = '<access token here>'
access_token_secret = '<access key secret here>'

consumer_key = '<consumer key here>'
consumer_secret = '<consumer key secret here>'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
