#!/usr/bin/env python

import time
import os

BUTTON = "3"
SLEEP_TIME = 0.2

def setup_gpio(button):
	if not os.path.isdir('/sys/class/gpio/gpio' + button):
		f = open('/sys/class/gpio/export', "w")
		f.write(button)
		f.close()

	f = open('/sys/class/gpio/gpio' + BUTTON + '/direction', "w")
	f.write("in")
	f.close()


class PressState():
	def __init__(self, button):
		self.f = open("/sys/class/gpio/gpio" + button + "/value")
		self.last_state = False

	def pressed(self):
		#print "last: " + str(self.last_state)
		self.f.seek(0)
		val = self.f.read()
		#print "Val: " + val
		if val[0] == "1" and not self.last_state:
			self.last_state = True
			return True
		elif val[0] == "0":
			self.last_state = False 


setup_gpio(BUTTON)

ps = PressState(BUTTON) 

while True:
	if ps.pressed():
		print "Button pressed"
	
	time.sleep(SLEEP_TIME)
