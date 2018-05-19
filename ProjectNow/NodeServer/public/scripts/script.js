function test(Arg){
  console.log("tEST");
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      console.log('iets');
    }
  };
  var audio;
  var reader = new FileReader();
  var test1 = httpGet(Arg);
  var enc = new TextEncoder("base64");
  var file = new File(enc.encode(test, true), "Kweetnie", {type : "audio/mid"});
/*
  console.log(file);
  var midName = file.name;
  var wavName = midName.replace(/\..+?$/, '.wav');
  var wav = synth.midiToWav(file);
  var src = URL.createObjectURL(wav);
  audio = new Audio(src);
  audio.play();
  console.log(file)
  reader.readAsArrayBuffer(file);
  anchor.setAttribute('download', wavName);*/
    $("#player").midiPlayer({
        color: "red",
        onUnpdate: midiUpdate,
        onStop: midiStop,
        width: 250
    });
    var tempString = "data:audio/midi;base64,"+btoa(test);
    console.log(tempString);
    $("#player").midiPlayer.play(tempString);
}


function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}
var midiUpdate = function(time) {
               console.log(time);
           }
           var midiStop = function() {
               console.log("Stop");
           }

           function startPlaying() {
               $("#player").midiPlayer.play(song);
           }
