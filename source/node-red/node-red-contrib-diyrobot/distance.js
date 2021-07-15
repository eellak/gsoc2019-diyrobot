module.exports = function(RED) {
    function DistanceNode(config) {
        RED.nodes.createNode(this,config);
        var node = this;
	node.on('input', function(msg) {
	    
	    var http = require('http');
	    var options = {
	      host: 'localhost',
	      port: '5000',
	      path: '/dist'
	    };
	    //~ callback = function(response){
		//~ console.log(response)
	    //~ }

	    //~ http.request(options, callback).end();
            //~ node.send(msg);
	    
	    //~ var http = require('http');
	    //~ var req = http.get({
		//~ host: 'localhost',
		//~ port: '5000',
		//~ path: '/dist'
		//~ }, (res) => { 
		    //~ // res = response.json();
		    //~ node.log(res); 
		    //~ // node.log('Hello'); 
		    //~ msg.payload = res;
		    //~ node.send(msg);
		    //~ // console.log(res); 
		//~ }).on('error', (e) => {
		    //~ node.log(e);
		    //~ // console.log(e);
		//~ });
		
		
		
		
	    http.get(options, (res) => {
	      const { statusCode } = res;
	      const contentType = res.headers['content-type'];

	      let error;
	      // Any 2xx status code signals a successful response but
	      // here we're only checking for 200.
	      if (statusCode !== 200) {
		error = new Error('Request Failed.\n' +
				  `Status Code: ${statusCode}`);
	      } else if (!/^application\/json/.test(contentType)) {
		error = new Error('Invalid content-type.\n' +
				  `Expected application/json but received ${contentType}`);
	      }
	      if (error) {
		console.error(error.message);
		// Consume response data to free up memory
		res.resume();
		return;
	      }

	      res.setEncoding('utf8');
	      let rawData = '';
	      res.on('data', (chunk) => { rawData += chunk; });
	      res.on('end', () => {
		try {
		  const parsedData = JSON.parse(rawData);
		  // console.log(parsedData);
		  
		  // node logic 
		  msg.payload = parsedData.distance;
		  node.send(msg);
		
		} catch (e) {
		  console.error(e.message);
		}
	      });
	    }).on('error', (e) => {
	      console.error(`Got error: ${e.message}`);
	    });

        });
    }
    RED.nodes.registerType("distance",DistanceNode);
}
