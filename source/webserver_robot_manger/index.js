var express = require('express');
var app = express();
var fs = require("fs");
var path = require('path');
var exec = require('child_process').exec;

var options = {
  name: 'Proteas Sudo Prompt',
};

app.use(express.static("public"));



app.get('/shutdown', function (req, res) {
	exec('sudo /sbin/shutdown -r now', function (msg) { console.log(msg) });
})

app.get('/restart', function (req, res) {
	exec('sudo /sbin/reboot', function (msg) { console.log(msg) });
})



var server = app.listen(8080, function () {
   var host = server.address().address
   var port = server.address().port
   console.log("App listening at http://%s:%s", host, port)
})
