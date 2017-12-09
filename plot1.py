#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 12:07:05 2017

@author: shubhi
"""

import tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt

access_token = ''
access_token_secret = ''

consumer_key = ''
consumer_secret = ''

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)

public_tweets = api.search('Suicide')

sub=[]
pol=[]

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    sub.append(analysis.sentiment.subjectivity)
    pol.append(analysis.sentiment.polarity)
    print(analysis.sentiment)
     

plt.axis([0,1,-1,1])
plt.ylabel('polarity')
plt.xlabel('subjectivity')
plt.plot(sub,pol,'ro')
plt.show
