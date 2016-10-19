import tweepy as tweety
import csv
from textblob import TextBlob
import argparse

consumer_key        = "xXgGzFe8PyWOoD7x1T2KB0sB9"
consumer_secret     = "VLZRK2QstddIELeCcwzvb0zapo5Nx8zadcCWjv9mbE2ogGgHRJ"
access_token        = "51032036-L0Af231f8X2JCjcaWNscPK7Cxd2ZHdLqI0fH1CV5f"
access_token_secret = "YxBJtKc2KBgnUunc8kVNZSD9rdsWkyXum4zg2eJOd69X6"

auth = tweety.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


parser = argparse.ArgumentParser()
parser.add_argument('--keyword', type=str, help='Enter the string to be searched')
parser.add_argument('--max', type=int, help='Maximum number of tweets in the CSV file')
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