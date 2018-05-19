import twitter
import json
import requests
import _pickle as pickle
import sys
import schedule
import time

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''


api=twitter.Api(consumer_key=consumer_key,
                consumer_secret=consumer_secret,
                access_token_key=access_token,
                access_token_secret=access_token_secret)

for line in api.getstreamfilter():
    print (line)
