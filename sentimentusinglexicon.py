import tweepy
from textblob import TextBlob

access_token = '3469366695-1e8lECse0PDghuhz869TxFgHpXQSuLFJQLfxMtE'
access_token_secret = 'O1C9buxRdi2T7K0LdpoWgnFZaKji5AuwvXIX1WGt3sBoi'

consumer_key = 'mwl4PRxGtLr9UYNFZwB2HwkxO'
consumer_secret = 'DnxH9cFMFoznbPNaehPcCHfhnN1b5sPwNAmDDT5nnTdDyE4ar7'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
