//------------------------------------------------------------------------------
// Create the HTTP server
//------------------------------------------------------------------------------
var connect = require('connect');
var serveStatic = require('serve-static');
connect().use(serveStatic(__dirname)).listen(8080);
console.log("listening at port 8080...");
// console.log('Server is listening to http://localhost/ on port 8080…');