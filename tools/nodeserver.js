var
    fs = require('fs');
url = require('url');
path = require('path');
http = require('http');

var root = path.resolve('.');
var server = http.createServer(function(request, response) {
    console.log('connect success.....');
    console.log(request.url);
    //var pathname=url.parse(request.url).pathname;
    //var filepath = path.join(root, pathname);

    if (url.parse(request.url).pathname == '/upgrade_setting.xml') {
        var filepath = path.join(root, '/upgrade_setting.xml');
        fs.stat(filepath, function(err, stats) {
            if (!err && stats.isFile()) {
                console.log('200' + request.url);
                response.writeHead(200);
                fs.createReadStream(filepath).pipe(response);
            } else {
                console.log('404' + resquest.url);
                response.writeHead(404);
                response.end('404 Not Found');
            }
        });
    } else if (url.parse(request.url).pathname === '/download_linux.bin') {
        var filepath = path.join(root, '/download_linux.bin');
        fs.stat(filepath, function(err, stats) {
            if (!err && stats.isFile()) {

                console.log('200' + request.url);
                response.writeHead(200);

                fs.createReadStream(filepath).pipe(response);
            } else {
                console.log('404' + resquest.url);
                response.writeHead(404);
                response.end('404 Not Found');
            }
        });
    }
});
server.listen(8080);
console.log('server init success.......');