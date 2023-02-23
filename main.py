from machine import Pin
import time

# Setup
green = Pin("PC5", Pin.OUT)
red = Pin("PB0", Pin.OUT)

# Loop
while True:
	red.value(0)
	green.value(1)
	time.sleep(1)
	green.value(0)
	red.value(1)
	time.sleep(1)
