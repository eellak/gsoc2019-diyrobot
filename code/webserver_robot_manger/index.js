var express = require('express');
var app = express();
var fs = require("fs");
var path = require('path');

app.use(express.static("public"));


app.get('/tt', function (req, res) {  

   res.sendFile(path.resolve("./public/index.html"));
   
})



var server = app.listen(8080, function () {
   var host = server.address().address
   var port = server.address().port
   console.log("App listening at http://%s:%s", host, port)
})