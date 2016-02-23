#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, yaml, time, os


def main():
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

	listener = StreamListener()
	stream = tweepy.Stream(auth = api.auth, listener=listener)

	# stream.filter(follow=['285198536'], async=True)
	stream.filter(track=['#TheBachelor'])


def split_text(status):
	words = status.split()

	for word in words:
		print(word)
	return words

def find_keyword(words = []):
	for word in words:
		if (word.lower() == "block") or (word.lower() == "blk"):


# create a class inheriting from tweepy's StreamListener
class StreamListener(tweepy.StreamListener):
	# handles data received from the stream

<<<<<<< HEAD

	def on_status(self, status):
		print('Tweet text: ' + status.text)

# not sure that text needs to be written to a file...
# take close look at this block
		with open('tweets.txt', 'a') as f:
			en_text = status.text.encode('utf-8')
			f.write(en_text + '\n')
			split_text(en_text);
			return True
		return True
=======
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

>>>>>>> f206ae6e1f822d1fb41c699c5df744cb62e439b5


	def on_error(self, status_code):
		print('Received an error with status code: ' + str(status_code))
		return True


	def on_timeout(self):
		print('Timeout...')
		return Trued


# if dcpd-map.py is run as the main function, i.e. via command line
if __name__ == '__main__':
<<<<<<< HEAD
	main()
=======
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
>>>>>>> f206ae6e1f822d1fb41c699c5df744cb62e439b5
