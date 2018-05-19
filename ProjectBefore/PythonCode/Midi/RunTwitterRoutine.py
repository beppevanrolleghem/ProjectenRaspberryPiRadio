import os
import sys
import schedule
import MidiGenerator as m
import time
from os import listdir
from os.path import isfile, join
import twitter
import json
import requests
from multiprocessing import Process

mongodbPath = 'c:/MongoDb/bin/mongod'
jsonPath = 'tweets.json'


def runLoop():
	os.system('python TwitterGetExample.py')
	os.system('python Interpreter.py ' + jsonPath)
	time.sleep(30)
	os.system('python DbUpdate.py')


schedule.every(1).minutes.do(runLoop)
#os.system(mongodbPath) this doesn't finish, so other programs won't run
runLoop()


while 1:
	schedule.run_pending()
	time.sleep(1)
