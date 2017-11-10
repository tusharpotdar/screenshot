from __future__ import unicode_literals
import time
import pyscreenshot as ImageGrab
import pyautogui, sys
if __name__ == "__main__":
	q= raw_input("Take mouse to left upper corner ==> and press enter") 
	x = pyautogui.position()
	x1 = x[0]
	x2 = x[1]
	qqq= raw_input("Take mouse to right bottom corner ==> and press enter") 
	y = pyautogui.position()
	y1 = y[0]
	y2 = y[1]
	while True:
		print "asdf"
		time.sleep(0.9)
 		im=ImageGrab.grab(bbox=(x1,x2,y1,y2))
		im.show()
		im.save('userPhoto.png')