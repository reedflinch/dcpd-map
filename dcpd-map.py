#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, yaml, time, os

# create a class inheriting from tweepy's StreamListener
class MyStreamListener(tweepy.StreamListener):
	# handles data received from the stream

	def __init__(self):

		self.tweet_status = []

	# def on_status(self, status):
	# 	print('Tweet text: ' + status.text)
	# 	# with open('tweets.json', 'a') as f:
	# 	# 	f.write(status._json + '\n')
	# 	# 	return True

	# 	return True

	def on_status(self, status):
		saveFile = open('tweets.json', 'a')

		self.tweet_status.append(status)

		saveFile = open('tweets.json', 'w')
		saveFile.write(u'[\n')
		saveFile.write(','.join(self.tweet_status))
		saveFile.write(u'\n]')
		saveFile.close()
		exit()


	def on_error(self, status_code):
		print('Received an error with status code: ' + str(status_code))
		return True

	def on_timeout(self):
		print('Timeout...')
		return Trued

# if dcpd-map.py is run as the main function, i.e. via command line
if __name__ == '__main__':
	# pull the app's twitter API credentials from config.yml file
	with open('config.yml') as f:
		doc = yaml.load(f)
		CONSUMER_KEY = doc["CONSUMER_KEY"]
		CONSUMER_SECRET = doc["CONSUMER_SECRET"]
		ACCESS_KEY = doc["ACCESS_KEY"]
		ACCESS_SECRET = doc["ACCESS_SECRET"]
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

	api = tweepy.API(auth)

	myStreamListener = MyStreamListener()
	stream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
	# stream.filter(follow=['285198536'], async=True)
	stream.filter(track=['#GunsInAmerica'])
