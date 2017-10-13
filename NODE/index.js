var cloudinary = require('cloudinary');

var express = require("express");
var app = express();
var recursive = function () {
    app.get('/', function (req, res) {
        console.log(req);
        //Some other function call in callabck
        res.send(cloudinary.image("i5ak0wve8omorlkxog9d.png"));
    });
    app.listen(8000);
    setTimeout(recursive, 1000);
}
recursive();