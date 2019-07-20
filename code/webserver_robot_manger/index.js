var express = require('express');
var app = express();
var fs = require("fs");
var path = require('path');

app.use(express.static("public"));
var sudo = require('sudo-prompt');
var options = {
  name: 'Proteas Sudo Prompt',
};


app.get('/wifi', function (req, res) {
	sudo.exec('cat etc/wpa_supplicant/wpa_supplicant.conf', options,
  	function(error, stdout, stderr) {
    	if (error) throw error;
	     console.log(JSON.stringify(stdout));
	      res.send(stdout);
  	}
	);
})

app.get('/shutdown', function (req, res) {
	sudo.exec('shutdown -t 0', options,
  	function(error, stdout, stderr) {
    	if (error) throw error;
	     console.log("Shutdown!");
       res.send("Shutdown");
  	}
	);
})

app.get('/reboot', function (req, res) {
	sudo.exec('reboot', options,
  	function(error, stdout, stderr) {
    	if (error) throw error;
	console.log("Reboot!");
	res.send("Reboot");
  	}
	);
})

var server = app.listen(8080, function () {
   var host = server.address().address
   var port = server.address().port
   console.log("App listening at http://%s:%s", host, port)
})
