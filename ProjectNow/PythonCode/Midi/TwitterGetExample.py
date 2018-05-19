import twitter
import json
import requests
import sys
import schedule
import time

since_id = None
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
location = ""
json_data = "{\"tweets\":["

def getTweets():
	global json_data
	print('getting tweets')
	with open('/files/lastid', 'r') as file:
		since_id = file.readline()
	if (since_id == ""):
		since_id = None
	api=twitter.Api(consumer_key=consumer_key,
					consumer_secret=consumer_secret,
					access_token_key=access_token,
					access_token_secret=access_token_secret)
	temp = api.GetMentions(since_id=since_id, count=None,max_id=None,trim_user=False,contributor_details=False,include_entities=True)
	if len(temp) > 0:
		for item in temp:
			data = {}
			data['id'] = item.id
			data['UserName'] = item.user.name
			data['Date'] = item.created_at
			data['text'] = item.text
			data['location'] = ""
			data['success'] = "no"
			json_data = json_data + json.dumps(data) + ","
		with open('/files/lastid', 'w') as outfile:
			outfile.write(temp[0].id_str)
		with open(location + 'tweets.json', "a") as outfile:
			json_data = json_data[:len(json_data)-1] + "]}"
			outfile.write(json_data)
	print('wrote some json shit')


getTweets()
