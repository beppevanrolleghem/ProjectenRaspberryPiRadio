from midiutil.MidiFile3 import MIDIFile
import random
import sys
import os

#--Variables--

#MIDI Variables
Selected_channel = 0
Selected_track = 0
Time_Constant = 0
Miditrack = MIDIFile(0)

#notes variables. these are pitches of the notes, add 12 to them for every octave you wanna go up

DictOfNotes = {'C' : 0, 'Do' : 0, 'Do#' : 1, 'C#' : 1, 'Reb' : 1, 'Db' : 1, 'Re' : 2, 'D' : 2, 'D#' : 3, 'Re#' : 3, 'Mib' : 3, 'Eb' : 3, 'Mi' : 4, 'E' : 4, 'F' : 5, 'Fa' : 5, 'F#' : 6,'Fa#' : 6, 'Solb':6, 'Gb' : 6, 'Sol':7, 'G' : 7, 'Sol#' : 8, 'G#' : 8, 'Lab' : 8, 'Ab' : 8,'La':9, 'A' : 9,'La#' : 10, 'A#' : 10, 'Bb' : 10,'Sib': 10, 'Tib': 10, 'B' : 11, 'Si':11, 'Ti':11}

C = 0
Db = 1
D = 2
Eb = 3
E = 4
F = 5
Gb = 6
G = 7
Ab = 8
A = 9
Bb = 10
B = 11



#Instrument Variables
DictOfInstruments = {'Piano' : 1, 'Bright_Piano' : 2,'Electric_Grand_Piano' : 3,'Honkytonk_Piano' : 4,'Electric_Piano' : 5,'Electric_Piano_2' : 6,'Harpsichord' : 7,'Clavinet' : 8,'Celesta' : 9,'Glockenspiel' : 10,'Music_Box' : 11,'Vibraphone' : 12,'Marimba' : 13,'Xylophone' : 14,'Tubular_Bells' : 15,'Dulcimer' : 16,'Drawbar_Organ' : 17,'Percussive_Organ' : 18,'Rock_Organ' : 19,'Church_Organ' : 20,'Reed_Organ' : 21,'Accordion' : 22,'Harmonica' : 23,'Tango_Accordion' : 24,'Acoustic_Guitar_nylon' : 25,'Acoustic_Guitar_steel' : 26,'Electric_Guitar_jazz' : 27,'Electric_Guitar_clean' : 28,'Electric_Guitar_muted' : 29,'Overdriven_Guitar' : 30,'Distortion_Guitar' : 31,'Guitar_Harmonics' : 49,'Acoustic_Bass' : 33,'Electric_Bass_finger' : 34,'Electric_Bass_pick' : 35,'Fretless_Bass' : 36,'Slap_Bass' : 37,'Slap_Bass_2' : 38,'Synth_Bass' : 39,'Synth_Bass_2' : 40,'Violin' : 41,'Viola' : 42,'Cello' : 43,'Contrabass' : 44,'Tremolo_Strings' : 45,'Pizzicato_Strings' : 46,'Orchestral_Harp' : 47,'Timpani' : 48,'String_Ensemble' : 49,'String_Ensemble_2' : 50,'Synth_Strings' : 51,'Synth_Strings_2' : 52,'Choir_Aahs' : 53,'Voice_Oohs' : 54,'Synth_Choir' : 55,'Orchestra_Hit' : 56,'Trumpet' : 57,'Trombone' : 58,'Tuba' : 59,'Muted_Trumpet' : 60,'French_Horn' : 61,'Brass_Section' : 62,'Synth_Brass' : 63,'Synth_Brass_2' : 64,'Soprano_Sax' : 65,'Alto_Sax' : 66,'Tenor_Sax' : 67,'Baritone_Sax' : 68,'Oboe' : 69,'English_Horn' : 70,'Bassoon' : 71,'Clarinet' : 72,'Piccolo' : 73,'Flute' : 74,'Recorder' : 75,'Pan_Flute' : 76,'Blown_bottle' : 77,'Shakuhachi' : 78,'Whistle' : 79,'Ocarina' : 80,'Synth_Lead_square' : 81,'Synth_Lead_sawtooth' : 82,'Synth_Lead_calliope' : 83,'Synth_Lead_chiff' : 84,'Synth_Lead_charang' : 85,'Synth_Lead_voice' : 86,'Synth_Lead_fifths' : 87,'Synth_Lead_bass_and_lead' : 88,'Synth_Pad_new_age' : 89,'Synth_Pad_warm' : 90,'Synth_Pad_polysynth' : 91,'Synth_Pad_choir' : 92,'Synth_Pad_bowed' : 93,'Synth_Pad_metallic' : 94,'Synth_Pad_halo' : 95,'Synth_Pad_sweep' : 96,'Synth_FX_rain' : 97,'Synth_FX_soundtrack' : 98,'Synth_FX_crystal' : 99,'Synth_FX_atmosphere' : 100,'Synth_FX_brightness' : 101,'Synth_FX_goblins' : 102,'Synth_FX_echoes' : 103,'Synth_FX_scifi' : 104,'Sitar' : 105,'Banjo' : 106,'Shamisen' : 107,'Koto' : 108,'Kalimba' : 109,'Bagpipe' : 110,'Fiddle' : 111,'Shanai' : 112,'Tinkle_Bell' : 113,'Agogo' : 114,'Steel_Drums' : 115,'Woodblock' : 116,'Taiko_Drum' : 117,'Melodic_Tom' : 118,'Synth_Drum' : 119,'Reverse_Cymbal' : 120,'Guitar_Fret_Noise' : 121,'Breath_Noise' : 122,'Seashore' : 123,'Bird_Tweet' : 124,'Telephone_Ring' : 125,'Helicopter' : 126,'Applause' : 127,'Gunshot' : 128}

#Pianos

Piano = 1
Bright_Piano = 2
Electric_Grand_Piano = 3
Honkytonk_Piano = 4
Electric_Piano = 5
Electric_Piano_2 = 6
Harpsichord = 7
Clavinet = 8



#Chromatic_Percussion

Celesta = 9
Glockenspiel = 10
Music_Box = 11
Vibraphone = 12
Marimba = 13
Xylophone = 14
Tubular_Bells = 15
Dulcimer = 16



#Organ

Drawbar_Organ = 17
Percussive_Organ = 18
Rock_Organ = 19
Church_Organ = 20
Reed_Organ = 21
Accordion = 22
Harmonica = 23
Tango_Accordion = 24



#Guitar

Acoustic_Guitar_nylon = 25
Acoustic_Guitar_steel = 26
Electric_Guitar_jazz = 27
Electric_Guitar_clean = 28
Electric_Guitar_muted = 29
Overdriven_Guitar = 30
Distortion_Guitar = 31
Guitar_Harmonics = 49



#Bass

Acoustic_Bass = 33
Electric_Bass_finger = 34
Electric_Bass_pick = 35
Fretless_Bass = 36
Slap_Bass = 37
Slap_Bass_2 = 38
Synth_Bass = 39
Synth_Bass_2 = 40



#Strings

Violin = 41
Viola = 42
Cello = 43
Contrabass = 44
Tremolo_Strings = 45
Pizzicato_Strings = 46
Orchestral_Harp = 47
Timpani = 48



#Ensemble

String_Ensemble = 49
String_Ensemble_2 = 50
Synth_Strings = 51
Synth_Strings_2 = 52
Choir_Aahs = 53
Voice_Oohs = 54
Synth_Choir = 55
Orchestra_Hit = 56



#Brass

Trumpet = 57
Trombone = 58
Tuba = 59
Muted_Trumpet = 60
French_Horn = 61
Brass_Section = 62
Synth_Brass = 63
Synth_Brass_2 = 64



#Reed

Soprano_Sax = 65
Alto_Sax = 66
Tenor_Sax = 67
Baritone_Sax = 68
Oboe = 69
English_Horn = 70
Bassoon = 71
Clarinet = 72



#Pipe

Piccolo = 73
Flute = 74
Recorder = 75
Pan_Flute = 76
Blown_bottle = 77
Shakuhachi = 78
Whistle = 79
Ocarina = 80



#Synth_Lead

Synth_Lead_square = 81
Synth_Lead_sawtooth = 82
Synth_Lead_calliope = 83
Synth_Lead_chiff = 84
Synth_Lead_charang = 85
Synth_Lead_voice = 86
Synth_Lead_fifths = 87
Synth_Lead_bass_and_lead = 88



#Synth_Pad

Synth_Pad_new_age = 89
Synth_Pad_warm = 90
Synth_Pad_polysynth = 91
Synth_Pad_choir = 92
Synth_Pad_bowed = 93
Synth_Pad_metallic = 94
Synth_Pad_halo = 95
Synth_Pad_sweep = 96



#Synth_Effects

Synth_FX_rain = 97
Synth_FX_soundtrack = 98
Synth_FX_crystal = 99
Synth_FX_atmosphere = 100
Synth_FX_brightness = 101
Synth_FX_goblins = 102
Synth_FX_echoes = 103
Synth_FX_scifi = 104



#Ethnic

Sitar = 105
Banjo = 106
Shamisen = 107
Koto = 108
Kalimba = 109
Bagpipe = 110
Fiddle = 111
Shanai = 112



#Percussive

Tinkle_Bell = 113
Agogo = 114
Steel_Drums = 115
Woodblock = 116
Taiko_Drum = 117
Melodic_Tom = 118
Synth_Drum = 119
Reverse_Cymbal = 120



#Sound_effects

Guitar_Fret_Noise = 121
Breath_Noise = 122
Seashore = 123
Bird_Tweet = 124
Telephone_Ring = 125
Helicopter = 126
Applause = 127
Gunshot = 128


#--Functions--

#creates a midi file with the wanted amount of tracks, at the tempo and wanted amount of channels.
#these will always be in 4/4ths, since like 90% of music is in 4/4ths anyway it doesn't matter, and if we want, we can make it any multiple of the 4/4ths time since we can just increase the tempo, or take multiple bars and emulate them being one bar.
def MakeMidiFile(Tempo, Channels, Tracks = 16):
	global Selected_channel
	global Selected_track
	global Time_Constant
	global Miditrack
	Time_Constant = 0
	Selected_track = 0
	Selected_channel = 0
	Miditrack = MIDIFile(Tracks)
	for x in range(0,Tracks):
		trcknm = "track " + str(x)
		Miditrack.addTrackName(x, Time_Constant, trcknm)
		Miditrack.addTempo(x, Time_Constant, Tempo)
	return

#changes note to the octave you want
def No( note, octave ):
	temp = note + (12 * octave)
	return int(note + (12 * octave))

def NoPrs( string ):
	if len(string) > 3:
		octNr = string[-1]
		noteNr = DictOfNotes[string[0:-1]]
	elif len(string) > 2 :
		octNr = string[-1]
		noteNr = DictOfNotes[string[0:-1]]
	else:
		octNr = string[-1]
		noteNr = DictOfNotes[string[0]]
	return No(noteNr, int(octNr))

#adds a single note to the track and sets the time_constant further
def AddNote( note, duration, volume ):
	global Selected_channel
	global Selected_track
	global Time_Constant
	global Miditrack
	Miditrack.addNote(Selected_track, Selected_channel, NoPrs(note), Time_Constant, duration, volume)
	Time_Constant += duration
	return

#adds multiple notes to the track and sets the time_constant further
def AddChord( notes, duration, volume ):
	global Selected_channel
	global Selected_track
	global Time_Constant
	global Miditrack
	for note in notes:
		nr = NoPrs(note)
		Miditrack.addNote(Selected_track, Selected_channel, nr, Time_Constant, duration, volume)
	Time_Constant += duration
	return

#adds a pause in the track
def AddPause( times, duration ):
	if (is_number(times)):
		for x in range (0, int(times)):
			AddNote('C0', duration, 0)
	else:
		AddNote('C0', duration, 0)
	return

#generates the .mid and writes it to given name
def ExportMidi(FileName):
	global Miditrack
	binfile = open(FileName+".mid", 'wb')
	Miditrack.writeFile(binfile)
	binfile.close()
	return

def ChangeInstrument(InstrumentNr = 1, Channel = None, Track = None):
	global Selected_channel
	global Selected_track
	global Time_Constant
	global Miditrack
	if Channel is None:
		Channel = Selected_channel
	if Track == None:
		Track = Selected_track
	if InstrumentNr in DictOfInstruments:
		InstrumentNr = DictOfInstruments[InstrumentNr]
	elif is_number(InstrumentNr):
		InstrumentNr = int(InstrumentNr)
	else:
		InstrumentNr = 1
	Miditrack.addProgramChange(Track, Channel, Time_Constant, InstrumentNr)
	return

def ChangeTrack(tracknr):
	global Selected_channel
	global Selected_track
	global Time_Constant
	global Miditrack
	Time_Constant = 0
	Selected_track = tracknr
	if Selected_track == None or Selected_track < 1:
		Selected_track = 1
	return

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
