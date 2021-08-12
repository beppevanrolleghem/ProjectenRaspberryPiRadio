# RaspberryPi Radio

TLDR; This is a refactor of a college assignment where we parsed tweets and turned them into music on a server

It was supposed to be a group project but unfortunately I ended up having to do most of the coding. 
I didn't help myself by making the code really weird and obscure, hardly documenting anything and taking on a subject I had a lot more experience with then the other members of the group.
The group vibe was off aswell since some of the members and I ran into some "ethical differences" (basically the guy turned out to be a weird 4chan sexist type beat).

The project itself was pretty interesting. The original idea was to be able to receive texts on a raspberry pi using a certain syntax which would then be translated to music and played. 
4chan was in charge of the hardware but we burned through at least 2 rpi's (while loops without pause) and receiving texts seemed to be outside the scope of the project (which would mean that all he did was plug in a speaker in the speaker port of the rpi). *also no headless server, no idea why he chose that*
Since texts were no option I went to the next best thing which was a twitter bot. Idk if its still up/around somewhere.
The project ended up being a giant python file that just accepted my weird notation and turned it into midi using a different library.