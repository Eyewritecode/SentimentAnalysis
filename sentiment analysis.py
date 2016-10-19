import tweepy as tweety
import csv
from textblob import TextBlob
import argparse

consumer_key        = "loremipsum"
consumer_secret     = "loremipsum"
access_token        = "loremipsum"
access_token_secret = "loremipsum"

auth = tweety.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


parser = argparse.ArgumentParser()
parser.add_argument('--keyword', type=str)
args = parser.parse_args()
searchkeyword = args.keyword




api = tweety.API(auth)
public_tweets = api.search(searchkeyword, lang="en", rpp="100")
sentiment= ""
with open("data.csv", "w") as file:
	data = csv.writer(file)
	data.writerow(("Tweet", "Sentiment"))
	for tweet in public_tweets:
		#print(tweet.text)
		analysis = TextBlob(tweet.text)
		#print (analysis)
		if analysis.sentiment.polarity > 0.1:
			sentiment = "Positive" 
		else:
			sentiment = "Negative"
		 #print(analysis.sentiment)
		data.writerow((tweet.text.encode('UTF-8'), sentiment))