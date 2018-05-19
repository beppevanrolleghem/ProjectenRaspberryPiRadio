# &#9836; MidiPlayerJS
[![npm version](https://badge.fury.io/js/midi-player-ts.svg)](https://badge.fury.io/js/midi-player-ts)

MidiPlayerJS is a JavaScript library which reads standard MIDI files and emits JSON events in real time.  This player does not generate any audio, but by attaching a handler to the event emitter you can trigger any code you like which could play audio, control visualizations, feed into a MIDI interface, etc.

Forked & modified by Tim Mensch to be easier to include into an ES6 or TypeScript project. Includes TypeScript types.

Additional post-fork improvements include:

* Older Safari browser compatibility: There were several places where the code would fail on Safari on iOS 9. Fixed/polyfilled.
* Optimized: Was using `Uint8Array.slice` previously, which creates a copy of the slice. Changed to `subarray` which links to the original data.
* Use a gulpfile to enable building cross-platform. Previously it wouldn't build on Windows.
* Improved the packaging to use `require`, and correctly use `browserify` to package both browser and node versions.
* Add a `yarn.lock` file for consistent builds.
* Fix Program Change message to work as expected

## Demos
* [Neopixel Music](https://github.com/robertvorthman/neopixel-music) by robertvorthman @robertvorthman
* [Autocomposer](http://www.rj-salvador.com/apps/autocomposer/) by RJ Salvador @rjsalvadorr
* [Simple Browser Player](http://grimmdude.com/MidiPlayerJS/) by Garrett Grimm @grimmdude

## Getting Started
Using MidiWriterJS is pretty simple.  Create a new player by instantiating `MidiPlayer.Player` with an event handler to be called for every MIDI event.  Then you can load and play a MIDI file.

```js
var MidiPlayer = require('midi-player-js');

// Initialize player and register event handler
var Player = new MidiPlayer.Player(function(event) {
	console.log(event);
});

// Load a MIDI file
Player.loadFile('./test.mid');
Player.play();
```
## Player Events
There are a handful of events on the `Player` object which you can subscribe to using the `Player.on()` method.  Some events pass data as the first argument of the callback as described below:

```js
Player.on('fileLoaded', function() {
    // Do something when file is loaded
});
Player.on('playing', function(currentTick) {
    // Do something while player is playing
    // (this is repeatedly triggered within the play loop)
});
Player.on('midiEvent', function(event) {
    // Do something when a MIDI event is fired.
    // (this is the same as passing a function to MidiPlayer.Player() when instantiating.
});
Player.on('endOfFile', function() {
    // Do something when end of the file has been reached.
});
```
## Full API Documentation
[http://grimmdude.com/MidiPlayerJS/docs/](http://grimmdude.com/MidiPlayerJS/docs/)

