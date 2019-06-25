#!/usr/bin/env python 

#this script will display letters with random colors on the Pi HAT
from sense_hat import SenseHat
import time
import random
sense = SenseHat()
blinks = input()

xcoord = random.randint(0,7)
ycoord = random.randint(0,7)
for x in range(blinks):
    sense.set_pixel(xcoord, ycoord, (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    time.sleep(0.5)
    sense.set_pixel(xcoord,ycoord,(0,0,0))
    time.sleep(0.5)
sense.clear()
