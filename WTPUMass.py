"""
Without Their Permission Stream by Christopher Scott
http://www.scottdchris.com
"""
from twython import Twython
import django
import pprint		#Pretty Print
import requests		#Requests


#Twython OAuth 1 Authentication
APP_KEY		= 'Removed for Git'
APP_SECRET	= 'Removed for Git'
OAUTH_TOKEN = 'Removed for Git'
OAUTH_TOKEN_SECRET = 'Removed for Git'

listOfTweets = ''

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
results = twitter.search(q='WTPUMass', result_type='recent', count = '50')
#pprint.pprint(results)
for tweet in results['statuses']:
	user_handle = ('@' + tweet['user']['screen_name']).encode('ascii','ignore')
	tweetText = tweet['text'].encode('ascii','ignore')
	if tweet['entities']['media'][0]['media_url'] is not None:
		imageURL = tweet['entities']['media'][0]['media_url']
	listOfTweets += "%s, %s, %s\n" % (user_handle, tweetText, imageURL)

print listOfTweets
csvFile = open('Tweets.csv', 'wb')
csvFile.write(listOfTweets)
csvFile.close()

time.sleep(1) #Script runs once every 1:01 mins to avoid Twitter API Rate Limit Error of 15 calls per 15 minutes
