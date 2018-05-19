

# Syntax

## Types of notes
The usage of european (Do Re Mi Fa Sol La Si/Ti) notes are allowed and will work just as well as american notation (A B C D E F G). After that we signify if the note is flat (b) or sharp (#) and then we put the octave we want the note to be on.


## Pauses
a "p" sign signifies a pause, it works the same as a normal note, but is just silent. ex:
"pq" is a quarter note pause


## Timing
Timing was a little harder to do in a user friendly manner, however. this is how the script understands length of notes.

O is a whole note
o is a half note
q is a quarter note
t is an eight note
s is a sixteenth note

you would add these after your notes to signify how long the note should last

## Instruments
Right now i have it set that you have to set your instrument before you start your song part(?). The syntax for this is Inst($$$), with $$$ representing the name of one of the instruments or the instrument number. these are the program change event values that is used in General Midi (GM) at the end of this readme i will include a list of all the numbers with their respective instruments

## Tracks
Right now this feature is not yet fully implimented because of the way syntax works. I would really like to implement it, but damn is it hard to find an easy way to put this in text form.

## Channels and the implication of not having access to channel 10 at this stage
At this point i'm having trouble implementing this concept of channels. Normally you would think this isn't that bad, because you can easily implement tracks. However, in GM there is a channel reserved for percussion which makes it a lot easyer to create percussion in a song. Right now as i'm trying to implement tracks i could create percussion by assigning an instrument to a certain track and playing my notes by that track and the sample of the drump to a pitch. This however is not very handy. so i would much rather create a syntax for the 10th midi channel so that i could have access to create a more comprehensive track

## Examples
example:

| E4q G#4q B4q pq |

this would result in the notes E G# and B being played in the 4th octave all for 1/4th of a bar, and then there is a 1/4th of a bar of rest.


chords are created using the ( ) signs. you can put multiple notes inside of the () without marking their timing, and then mark the time after the chord. example:

| ( E4 G#4 B4 )o po |

this would result in half a bar of the chord e-major being played, and then half a bar of pause.


### Prototype Examples
Here i'm going to put the examples of ways to syntax this shit so that i can actually code towards this syntax. Pro's from going at it from this side is that creating a syntax from this way would make it a lot more user friendly (or at least friendly for me to use) because i think ab out the syntax first and then the code behind deserializing(?) it.

#### Channels
so in the end i have decided to go with tracks at a later time and focus on channels for now.

taking our basic note note note pause chord pause progression:

| E4q G#4q B4q pq | ( E4 G#4 B4 )o po |

##### Formula 1

|:1 E4q G#4q B4q pq |:2 ( E4 G#4 B4 )o po |

the idea being that the number would represent the channel of the track, problem with this being that there are more then 10 channels, so even using 0 as a channel, we would get into double digits. This brings me to the next version:


##### formula 2

|:1 E4q G#4q B4q pq |:B ( E4 G#4 B4 )o po |

It is the same concept as the one above, but it uses the hexadecimal system. so :1 would mean channel 2, :0 would become channel 1 and :B would become channel 12 this way we can use all 16 channels with a minimal amount of space used and it helps a lot during interpretation. the cost of this being that it makes it less ux friendly. but when you're at the point of using channels, it doesn't matter anymore. channel 9 would be percussion so the only reason to use channels a b c d e and f would be for even more instruments and at that point, why not use a daw. (Digital audio workstation)

#### tracks
the concept behind tracks right now will be to get notes to play at the same time. hopefully we'll be able to make tracks repeat at the end, but thats gonna be kindof hard.
syntax possibilities

##### formula 1

`[|:1 E4q G#4q B4q pq |]*(3)[Inst(44)|:2 ( E4 G#4 B4 )o po |]*(5)`
this is the forumla i eventually ended upon, instrument changes still work, this reps the first bar 3 times and during that reps the last bar 5 times


# Channel 10 (9)
In general midi channel number 9 is used as a channel exclusively for percussion, certain notes create a sound, see the list of what notes make what sound below (at a later date)


# Instrument List

## Piano
1 Piano
2 Bright_Piano
3 Electric_Grand_Piano
4 Honkytonk_Piano
5 Electric_Piano
6 Electric_Piano_2
7 Harpsichord
8 Clavinet
## Chromatic Percussion
9 Celesta
10 Glockenspiel
11 Music_Box
12 Vibraphone
13 Marimba
14 Xylophone
15 Tubular_Bells
16 Dulcimer
## Organ
17 Drawbar_Organ
18 Percussive_Organ
19 Rock_Organ
20 Church_Organ
21 Reed_Organ
22 Accordion
23 Harmonica
24 Tango_Accordion
## Guitar
25 Acoustic_Guitar_nylon
26 Acoustic_Guitar_steel
27 Electric_Guitar_jazz
28 Electric_Guitar_clean
29 Electric_Guitar_muted
30 Overdriven_Guitar
31 Distortion_Guitar
32 Guitar_Harmonics
## Bass
33 Acoustic_Bass
34 Electric_Bass_finger
35 Electric_Bass_pick
36 Fretless_Bass
37 Slap_Bass
38 Slap_Bass_2
39 Synth_Bass
40 Synth_Bass_2
## Strings
41 Violin
42 Viola
43 Cello
44 Contrabass
45 Tremolo_Strings
46 Pizzicato_Strings
47 Orchestral_Harp
48 Timpani
## Ensemble
49 String_Ensemble
50 SString_Ensemble_2
51 Synth_Strings
52 Synth_Strings_2
53 Choir_Aahs
54 Voice_Oohs
55 Synth_Choir
56 Orchestra_Hit
## Brass
57 Trumpet
58 Trombone
59 Tuba
60 Muted_Trumpet
61 French_Horn
62 Brass_Section
63 Synth_Brass
64 Synth_Brass_2
## Reed
65 Soprano_Sax
66 Alto_Sax
67 Tenor_Sax
68 Baritone_Sax
69 Oboe
70 English_Horn
71 Bassoon
72 Clarinet
## Pipe
73 Piccolo
74 Flute
75 Recorder
76 Pan_Flute
77 Blown_bottle
78 Shakuhachi
79 Whistle
80 Ocarina
## Synth Lead
81 Synth_Lead_square
82 Synth_Lead_sawtooth
83 Synth_Lead_calliope
84 Synth_Lead_chiff
85 Synth_Lead_charang
86 Synth_Lead_voice
87 Synth_Lead_fifths
88 Synth_Lead_bass_and_lead
## Synth Pad
89 Synth_Pad_new_age
90 Synth_Pad_warm
91 Synth_Pad_polysynth
92 Synth_Pad_choir
93 Synth_Pad_bowed
94 Synth_Pad_metallic
95 Synth_Pad_halo
96 Synth_Pad_sweep
## Synth Effects
97 Synth_FX_rain
98 Synth_FX_soundtrack
99 Synth_FX_crystal
100 Synth_FX_atmosphere
101 Synth_FX_brightness
102 Synth_FX_goblins
103 Synth_FX_echoes
104 Synth_FX_scifi
## Ethnic
105 Sitar
106 Banjo
107 Shamisen
108 Koto
109 Kalimba
110 Bagpipe
111 Fiddle
112 Shanai
## Percussive
113 Tinkle_Bell
114 Agogo
115 Steel_Drums
116 Woodblock
117 Taiko_Drum
118 Melodic_Tom
119 Synth_Drum
120 Reverse_Cymbal
## Sound effects
121 Guitar_Fret_Noise
122 Breath_Noise
123 Seashore
124 Bird_Tweet
125 Telephone_Ring
126 Helicopter
127 Applause
128 Gunshot
