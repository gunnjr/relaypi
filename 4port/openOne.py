#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# we are working with pin 2
relayPin = 2

# set mod eand state to 'high' on our pin
GPIO.setup(relayPin, GPIO.OUT)
GPIO.output(relayPin, GPIO.HIGH)

try:	
   print "opening Relay for 10 secs..."
   GPIO.output(relayPin, GPIO.LOW)
   time.sleep(10);
   print "Now closing."
   GPIO.cleanup()

# End program cleanly with keyboard
except KeyboardInterrupt:
  print "  Quit"

  # Reset GPIO settings
  GPIO.cleanup()


# find more information on this script at
# http://youtu.be/WpM1aq4B8-A
