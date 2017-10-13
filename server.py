#!/usr/bin/env python
import random
import socket
import time
import cloudinary
import cloudinary.uploader
import cloudinary.api
import requests
import time 
cloudinary.config(cloud_name="dazkf9e4z",api_key="841282991838964",api_secret="byEUfFRe4ppNlQvzwEGJE5VXrXU")

s = socket.socket()         # Create a socket object
host = socket.getfqdn() # Get local machine name
port = 9082
s.bind((host, port))        # Bind to the port

print 'Starting server on', host, port
print 'The Web server URL for this would be http://%s:%d/' % (host, port)

s.listen(5)                 # Now wait for client connection.

print 'Entering infinite loop; hit CTRL-C to exit'
while True:
    str = cloudinary.CloudinaryImage("i5ak0wve8omorlkxog9d.png").image()
    # Establish connection with client.    
    c, (client_host, client_port) = s.accept()
    print 'Got connection from', client_host, client_port
    c.send('Server Online\n')
    c.send('HTTP/1.0 200 OK\n')
    c.send('Content-Type: text/html\n')
    c.send(' """
        <html>
    <head>
        <meta Http-Equiv="Cache-Control" Content="no-cache">
        <meta Http-Equiv="Pragma" Content="no-cache">
        <meta Http-Equiv="Expires" Content="0">
        <meta Http-Equiv="Pragma-directive: no-cache">
        <meta Http-Equiv="Cache-directive: no-cache">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>

    </head>
    <body style="background-color:#455a64">
        <div style="text-align: center; vertical-align: middle;">
            <p style="background-color: #0a6703;height:40px"></p>
        </div>
        <br/><br/><br/><br/><br/><br/><br/><br/><br/>
        <div style="text-align: center; vertical-align: middle;">
            <img id="qrcode" src="" alt="Loading.." style="text-align:center;background-color: white;"/>
            <br>
            <p style="color: white;font-size: x-large;">Scan QR Code using app</p>
        </div>
        <div style="text-align: center; vertical-align: middle;">
            <img src="lodash.png">
        </div>

        <script>

            $(document).ready(function(){
                startExeu();
            });


            function startExeu() {
                setInterval(getNewImage,100);
            }
            function getNewImage(){
                var d = new Date();
                var n = d.getTime();
                var _img = document.getElementById("qrcode");
                _img.src = """ '+ str + ' """           }

        </script>

    </body>
</html>
        """ ')
		
		
    c.close()