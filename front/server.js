var express = require('express');
 
var app = express();

app.get('/', function (request, response) {
    console.log(request.url);
    response.writeHeader(200, {'Content-Type': 'text/html'});
    response.send('<h1> Hello world </h1>')
});

app.get('/login', function (request, response) {
    console.log("123");
    console.log(request.url);
    response.send('<h1> LOGIN page </h1>')
});

app.get('/[a-zA-Z]*/', function (request, response) {
    console.log(request.url);
    response.send(request.url);
});

app.listen(80);