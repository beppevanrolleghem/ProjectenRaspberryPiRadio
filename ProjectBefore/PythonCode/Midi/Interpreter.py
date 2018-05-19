import sys
import schedule
import os
import MidiGenerator as m
import time
import json
from os import listdir
from os.path import isfile, join

#vars
#notes first letters
nts = {"D", "R", "M", "F", "S", "L", "S", "T", "C", "E", "G", "A", "B"}
times = {"O", "o", "q", "t", "s"}
Modifiers = {"(", ")",  "|", ":"}
speshNts = {"D", "F"}
eu = {"R", "M", "S", "L", "T", "S"}
us = {"C", "E", "G", "A", "B"}
times = {'O' : 4, 'o' : 2, 'q' : 1, 't' : .5, 's' : .25}
channels = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
noteMods = {"b", "#"}
filetype = None
'| B2t E3t (B3 F4)q pt D4t D3t A3t D4t E4t E3t B4t pt D5t |'
song = '| E4q G#4q B4q pq | ( E4 G#4 B4 )o po |'
ConvertionNotPossible = False
bpm = 140
#/home/beppe/Documents/Python/proj/1718JrpiRadio/PythonCode/Midi/
songPath = "/songs/"

nonExistantNotes = {"D#", "Cb", "E#", "Fb", "Si#", "Ti#", "Dob", "Mi#", "Fab"}
#Methods
instrument = 0


def GetNextCharThing(pos, strg):
	global ConvertionNotPossible
	temp = strg[pos]
	if temp in nts:
		note = GetNoteStr(pos, strg)
		timing = strg[pos+len(note)]
		try:
			m.AddNote(note, times[timing], 100)
		except:
			ConvertionNotPossible = True
			print(str(sys.exc_info()[0]) + " ERROR HAPPENED AT ADDNOTE, ConvertionNotPossible = " + str(ConvertionNotPossible))
		return pos+len(note)+1
	elif temp in Modifiers:
		if temp == "|":
			return pos+1
		elif temp == ":":
			chan = strg[pos+1]
			if chan in channels:
				try:
					m.Selected_channel = channels[chan]
					m.ChangeInstrument(instrument)
				except:
					ConvertionNotPossible = True
					print(str(sys.exc_info()[0]) + " ERROR HAPPENED AT CHANGEINSTRUMENT, ConvertionNotPossible = " + str(ConvertionNotPossible))
			return pos+2
		elif temp == "(":
			charNr = pos +1
			notes = []
			while True:
				if strg[charNr] in nts:
					tempNote = GetNoteStr(charNr, strg)
					notes.append(tempNote)
					charNr = charNr + len(tempNote)
				elif strg[charNr] == ")":
					timing = strg[charNr+1]
					try:
						m.AddChord(notes, times[timing], 100)
					except:
						ConvertionNotPossible = True
						print(str(sys.exc_info()[0]) + " ERROR HAPPENED AT ADDCHORD, ConvertionNotPossible = " + str(ConvertionNotPossible))
					return charNr+1
					break
				elif strg[charNr] == "|":
					charNr = charNr+1
	elif temp in times:
		return pos+1
	elif temp == 'p':
		amount = strg[pos+1]
		timing = strg[pos+2]
		try:
			m.AddPause(amount, times[timing])
		except:
			ConvertionNotPossible = True
			print(str(sys.exc_info()[0]) + " ERROR HAPPENED AT PAUSES, ConvertionNotPossible = " + str(ConvertionNotPossible))
		return pos+2
	else:
		ConvertionNotPossible = True
		return pos+1


def GetNoteStr(pos, strg):
	temp = strg[pos]
	if temp in nts:
		if temp in speshNts:
			if temp == "D":
				if strg[pos+1] == "o":
					if strg[pos+2] in noteMods:
						note = strg[pos:pos+3]
						octv = strg[pos+3]
						return note+octv
					else:
						note = strg[pos:pos+2]
						octv = strg[pos+2]
						return note+octv
				else:
					if strg[pos+1] in noteMods:
						note = strg[pos:pos+2]
						octv = strg[pos+2]
						return note+octv
					else:
						note = strg[pos]
						octv = strg[pos+1]
						return note+octv
			else:
				if strg[pos+1] == "a":
					if strg[pos+2] in noteMods:
						note = strg[pos:pos+3]
						octv = strg[pos+3]
						return note+octv
					else:
						note = strg[pos:pos+2]
						octv = strg[pos+2]
						return note+octv
				else:
					if strg[pos+1] in noteMods:
						note = strg[pos:pos+2]
						octv = strg[pos+2]
						return note+octv
					else:
						note = strg[pos]
						octv = strg[pos+1]
						return note+octv
		elif temp in eu:
			if temp == "S":
				if strg[pos+1] == "o":
					if strg[pos+3] in noteMods:
						note = strg[pos:pos+4]
						octv = strg[pos+4]
						return note+octv
					else:
						note = strg[pos:pos+3]
						octv = strg[pos+3]
						return note+octv
				else:
					if strg[pos+2] in noteMods:
						note = strg[pos:pos+3]
						octv = strg[pos+3]
						return note+octv
					else:
						note = strg[pos:pos+2]
						octv = strg[pos+2]
						return note+octv
			else:
				if strg[pos+2] in noteMods:
					note = strg[pos:pos+3]
					octv = strg[pos+3]
					return note+octv
				else:
					note = strg[pos:pos+2]
					octv = strg[pos+2]
					return note+octv
		elif temp in us:
			if strg[pos+1] in noteMods:
				note = strg[pos:pos+2]
				octv = strg[pos+2]
				return note+octv
			else:
				note = strg[pos]
				octv = strg[pos+1]
				return note+octv
		else:
			return None
	else:
		return None



def writeSong(sng, title, bpm = 140, inst=1):
	global songPath
	m.MakeMidiFile(bpm, 16, 1)
	currentpos = sng.find('|')
	global instrument
	global ConvertionNotPossible
	if (instrument > 0):
		m.ChangeInstrument(instrument)
	else:
		instrument = 1
	while currentpos < len(sng):
		currentpos = GetNextCharThing(currentpos, sng)
		if ConvertionNotPossible:
			break
	if not ConvertionNotPossible:
		m.ExportMidi(songPath + title)
	else:
		print("NOTABLETOWRITETRACK")
	return True

def writeSongTracked(sngTracks, title, bpm=140, inst=1):
	m.MakeMidiFile(bpm, 16, len(sngTracks)+1)
	tracknr = 1
	global ConvertionNotPossible, songPath
	for track in sngTracks:
		currentpos = track.find('|')
		m.ChangeTrack(tracknr)
		global instrument
		InstrumentChk(track)
		if (instrument > 0):
			m.ChangeInstrument(instrument)
		else:
			instrument = 1
			m.ChangeInstrument(instrument)
		while currentpos < len(track):
			currentpos = GetNextCharThing(currentpos, track)
			if ConvertionNotPossible:
				break
			print (ConvertionNotPossible)
		tracknr = tracknr +1
		print (ConvertionNotPossible)
	print (ConvertionNotPossible)
	if not ConvertionNotPossible:
		m.ExportMidi(songPath + title)
	else:
		print("NOTABLETOWRITETRACK")
		m.ExportMidi(songPath + title)
	return


def checkText(txt):
	if txt.find('|') == -1:
		return True
	if any(Noot in txt for Noot in nonExistantNotes):
		return True
	return False


def ConvertFile(CONVERTABLEFILE):
	title = ""
	song = ""
	global ConvertionNotPossible
	ConvertionNotPossible = False
	file = str(CONVERTABLEFILE)
	file_extension = file[len(file)-5:]
	if file_extension == '.json':
		content = ""
		with open(CONVERTABLEFILE, 'r') as contentfile:
			content = contentfile.read()
			print(content)
		temp = json.loads(content)
		for tweet in temp['tweets']:
			song = tweet['text']
			song = song.replace(" ", "")
			ConvertionNotPossible = checkText(song)
			title = tweet['UserName'] + " id_" + str(tweet['id'])
			if ConvertionNotPossible == False:
				writeSong(song, title)
				tweet['location'] = 'songs/' + title + '.mid'
				tweet['success'] = "yes"
		with open('tweets.json', "w") as outfile:
			json.dump(temp, outfile)
			return
	else:
		title = os.path.basename(file)
		with open(file, 'r') as files:
			song = files.readline()
	song = song.replace(" ", "")
	firstBar = song.find('|')
	checkText(song)
	writeSong(song, title)
	if ConvertionNotPossible:
		with open(Directory+"/FailedLog", "a") as files:
			files.write("song " + title + " has failed to initialise.... \n")

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def checkItems(path):
	items = os.path.listdir(path)
	for item in items:
		ConvertFile(item)
	return True

def checkTempo(strb):
	global bpm
	if strb.find("Bpm(") > -1:
		temp = strb[strb.find("Bpm(")+4:strb.find(")")]
		if is_number(temp):
			bpm = int(temp)
		else:
			bpm = 140
	return

def ConvertText(txt, ttl=time.strftime("%d_%m_%y_%H_%M_%S")):
	song = txt
	title = ttl
	tracked = False
	song = song.replace(" ", "")
	checkTempo(song)
	global ConvertionNotPossible
	if "[" in song:
		song = song.split("[")
		tracked = True
	if tracked:
		songs = []
		for track in song:
			checkText(track)
			if "Inst(" in track:
				instStr = track[track.find("Inst("):track.find(")")+1]
			else:
				instStr = ""
			testnaam = track[track.find("]")+3:len(track)-1]
			temptrs = track[track.find("|"):track.find("]")]
			if is_number(testnaam):
				songs.append(instStr + temptrs*int(testnaam))
		writeSongTracked(songs, title, bpm)
	else:
		InstrumentChk(song)
		checkText(song)
		writeSong(song, title, bpm)
	if ConvertionNotPossible:
		print('failed to export as song')
	else:
		print('normally it\'s exported now under the title of ' + title+'.mid')
	return True

def InstrumentChk(txt):
	global instrument
	Inst = txt
	if "Inst" in  txt:
		Inst = Inst[Inst.find("Inst(")+5:Inst.find(")")]
	if is_number(Inst):
		if int(Inst) < 129:
			instrument = int(Inst)
		else:
			instrument = 0
	else:
		if Inst in m.DictOfInstruments:
			instrument = m.DictOfInstruments[Inst]
		else:
			instrument = 0

def is_convertabletxt(txt):
	if txt.find("|") > -1:
		return True
	return False



def startupRoutine():
	if len(sys.argv) > 1:
		if os.path.isdir(sys.argv[1]):
			checkItems(sys.argv[1])
		else:
			if is_convertabletxt(sys.argv[1]):
				if len(sys.argv) > 2:
					ConvertText(sys.argv[1], sys.argv[2])
				else:
					ConvertText(sys.argv[1])
				sys.exit()
			if os.path.isfile(sys.argv[1]):
				ConvertFile(sys.argv[1])
				sys.exit()
	print("no valid argument was found\nDo you want to continue? (y/n)")
	char = input()
	if char == 'y':
		print('\nPlease enter the title of the string you want to convert,\nif you don\'t want to give it a name, then leave it blank and it will get a timestamp as the title.')
		title = input()
		print('\nPlease enter the content of the string you want to convert')
		content = input()
		print('\nConverting')
		if(is_convertabletxt(content)):
			if(title==""):
				ConvertText(content)
			else:
				ConvertText(content, title)
		else:
			print('\nthe text you entered is non convertable\nPress enter to continue...')
			input()
			sys.exit()
	else:
		sys.exit()




startupRoutine()
