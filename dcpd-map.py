#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy

CONSUMER_KEY = '2ZZoK4yZVYzMQcGfaQx8tZaab'
CONSUMER_SECRET = '902aHEZCZK3QdTNDArIjBYtyWdx7VZayVQvwaDvI4W07x88bNL'
ACCESS_KEY = '300492257-lf1Zn55I4odPrEqFYCyB5ncaeo7i279mdGLoJqGe'
ACCESS_SECRET = 'cOj2DyVl5Dal613C9FpibrdrTl1WC86FLzDL7G9Nm4Fax'

# create a class inheriting from tweepy's StreamListener
class MyStreamListener(tweepy.StreamListener):
	# handles data received from the stream

	def on_status(self, status):
		print('Tweet text: ' + status.text)
		with open('tweets.txt', 'a') as f:
			en_text = status.text.encode('utf-8')
			f.write(en_text + '\n')
			return True
		return True

	def on_error(self, status_code):
		print('Received an error with status code: ' + str(status_code))
		return True

	def on_timeout(self):
		print('Timeout...')
		return True

# if dcpd-map.py is run as the main function, i.e. via command line
if __name__ == '__main__':
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

	api = tweepy.API(auth)

	myStreamListener = MyStreamListener()
	stream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
	# stream.filter(follow=['285198536'], async=True)
	stream.filter(track=['#OregonUnderAttack'])
