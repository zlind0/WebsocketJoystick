var https = require('https');
var fs = require('fs');
var server_port = 8000;
var path = require('path');
var baseDirectory = __dirname;   // or whatever base directory you want
io = require('socket.io');
var httpsOptions = {
    key: fs.readFileSync('private.key'),
    cert: fs.readFileSync('certificate.crt')
};

var app = function (request, response) {
    var uri = "index.html"
        , filename = path.join(process.cwd(), uri);

    fs.exists(filename, function(exists) {
        if(!exists) {
        response.writeHead(404, {"Content-Type": "text/plain"});
        response.write("404 Not Found\n");
        response.end();
        return;
        }

        if (fs.statSync(filename).isDirectory()) filename += '/index.html';

        fs.readFile(filename, "binary", function(err, file) {
        if(err) {        
            response.writeHead(500, {"Content-Type": "text/plain"});
            response.write(err + "\n");
            response.end();
            return;
        }

        response.writeHead(200);
        response.write(file, "binary");
        response.end();
        });
    });
}   
server=https.createServer(httpsOptions, app);
server.listen(server_port);

var socket = io(server); 
socket.on('connection', function(client){
    client.on('rotation', function(rot){
        console.log(JSON.stringify(rot));
    });
});