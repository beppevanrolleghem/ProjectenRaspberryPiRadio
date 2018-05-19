import pymongo
from pymongo import MongoClient
import json

client = MongoClient('localhost', 27017)
db = client.tweets
file_obj = open('tweets.json', 'r')
print(file_obj)
raw_data = file_obj.read()
temp = json.loads(raw_data)
post = []
posts = db.posts
for tweet in temp['tweets']:
   #post.append(tweet)
    db.tweets.insert(tweet)
open("tweets.json", 'w').close()
