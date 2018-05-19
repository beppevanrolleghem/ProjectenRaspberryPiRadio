const exp = require('express');
const app = exp();
const exphbs = require('express-handlebars');
const MongoClient = require('mongodb').MongoClient;
const port = 8080;
const pars = require('body-parser');
const shell = require('python-shell');
const url = 'mongodb://localhost:27017';
var MidiPlayers = require('midi-player-js');
var MidiPlayer = require('midi-player-ts');
const synth = require('synth-js');
const fs = require('fs');
let db;
var temp;
var Player = new MidiPlayers.Player(function(event) {
    console.log(event);
});
function updateDb() {
  MongoClient.connect(url, function(err, client) {
    const dbitems = client.db('tweets').collection('tweets');
    dbitems.find({}).toArray(function(err, items) {
      temp = items;
    });
    if(err){console.log(err)}
  });
}

function iets (err){
  console.log("require");
  // Initialize player and register event handler
  var Player = new MidiPlayer.Player(function(event) {
      console.log(event);
  });
  console.log("init");
  // Load a MIDI file
  Player.loadFile('pink.mid');
  console.log('played');
  Player.play();
  if (err )  {throw err;}
}
function ClearDb(){
  MongoClient.connect(url, function(err, client) {
    var dbitems = client.db('tweets');
    dbitems.collection("tweets").drop(function(err, delOK) {
      if (err) throw err;
      if (delOK) console.log("Collection deleted");
      //dbitems.close();
    });
  });
}
function DumpDb(){
  temp = {};
  const dbitems = client.db('tweets').collection('tweets');
  dbitems.find({}).toArray(function(err, items) {
    temp = items;
  });
  return temp
}
function InsertDb(title, text, Testlocation, user) {
  MongoClient.connect(url, function(err, client) {
    if (err) throw err;
    var dbitems = client.db('tweets');
    var myobj = { title: title, text: text, location: Testlocation+".mid", UserName: user, Date: new Date().toISOString()};
    dbitems.collection("tweets").insertOne(myobj, function(err, res) {
      if (err) throw err;
      console.log("1 document inserted");
      client.close();
    });
    var options= {
      scriptPath: __dirname+'/PythonCode/Midi/',
      args: [text, title]
    };
    convertText(options);
  });
}
function convertText(options){
  shell.run('Interpreter.py', options, function(err) {if (err) throw err; console.log('finished');});
}
updateDb();
app.engine('handlebars', exphbs({defaultLayout: 'main'}));
app.set('view engine', 'handlebars');
app.use(pars.json());
app.use(exp.static('static'));
app.use("/scripts",exp.static(__dirname + "/public/scripts"));
app.use('/css', exp.static(__dirname + "/public/css"));
app.use('/img', exp.static(__dirname + "/public/img"));
app.use('/files', exp.static(__dirname +"/files"))
app.use('/songs', exp.static(__dirname +"/songs"))
app.use(pars.urlencoded({ extended: true })); // support encoded bodies
app.listen(port, function(){
  console.log('Server is running at localhost:'+port);
})
app.get('/', (req, res) => {
  res.render('index');
})
app.get('/index', (req, res) => {
  res.render('index');
})
app.get('/download', (req, res) => {
  updateDb();
  res.render('downloads', {tweets : temp, download : "false"});
})
app.get('/about', (req, res) => {
  res.render('about');
})
app.get('/management', (req, res) => {
  res.render('management');
})
app.get('/testPage', (req, res) =>{
  res.render('testPage')
})
app.get('/DATATest', (req, res) =>{
  res.send("TEST");
})
app.get('/songs/*', (req, res) =>{
  console.log('GOTREQUEST')
  console.log(req.originalUrl);
  let midBuffer = fs.readFileSync(__dirname + req.originalUrl);
  console.log(midBuffer);
  res.send("TEST");
  res.render('about');
})
app.post('/download', (req, res) => {
  console.log(req.body.location);
  tempVar = req.body.location;
  typeS = req.body.typeScript;
  updateDb();
  switch (typeS) {
    case "play":
      iets();
      break;
    case "downloadMid":
      res.download(__dirname+"/"+tempVar);
      break;
  }
})
app.post('/index', (req, res) =>{
  stringNaam = req.body.text;
  stringNaam = stringNaam.replace("\x1a", "");
  console.log(req.body.title);
  console.log(stringNaam);
  console.log(req.body.user);
  res.render("index");
  InsertDb(req.body.title, stringNaam, 'songs/'+req.body.title, req.body.user)
})

app.post('/management', (req, res) => {
  switch (req.body.scriptType){
    case "Interpreter.py":
      stringTest = JSON.stringify(req.body.textArg);
      var options= {
        scriptPath: __dirname+'/PythonCode/Midi/',
        args: [stringTest, req.body.title]
      };
      shell.run('Interpreter.py', options,function (err) {if (err) throw err; console.log('finished');});
      //res.render('/management')
      break;
    case "ClearDb":
      ClearDb();
      break;
    case "TwitterGet":
      var options = {
        scriptPath: __dirname+'/PythonCode/Midi/',
        args: ['tweets.json']
      };
      shell.run('TwitterGetExample.py', options,function (err) {if (err) throw err; console.log('finished');});
      break;
    case "TweetsToMidi":
      var options = {
        scriptPath: __dirname+'/PythonCode/Midi/',
        args: ['tweets.json']
      };
      shell.run('Interpreter.py', options,function (err) {if (err) throw err; console.log('finished');});
    case "TweetsToDb":
      var options = {
        scriptPath: __dirname+'/PythonCode/Midi/'
      };
      shell.run('DbUpdate.py', options,function (err) {if (err) throw err; console.log('finished');});
      break;
    case "Iets":
      iets();
      break;
    default:
      break;
  }
  res.render('management');
})
