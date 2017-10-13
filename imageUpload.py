import cloudinary
import cloudinary.uploader
import cloudinary.api
import requests
import time 
cloudinary.config(cloud_name="dazkf9e4z",api_key="841282991838964",api_secret="byEUfFRe4ppNlQvzwEGJE5VXrXU")
#data = cloudinary.uploader.upload("screenshot.png")
infinity = 1
counter = 1
#while infinity>0:
print counter
counter =  counter + 1
print cloudinary.uploader.upload('screenshot.png',public_id = 'i5ak0wve8omorlkxog9d')
