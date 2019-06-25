#!/usr/bin/env/puthon

#this script will show a matrix of colors on the Pi HAT
from sense_hat import SenseHat
import time
sense = SenseHat()
r = (255,0,0)
b = (0,0,255)
w = (255,255,255)
n = (0,0,0)

pixels1 = [
        b,b,b,b,r,r,r,r,
        b,b,b,b,w,w,w,w,
        b,b,b,b,r,r,r,r,
        b,b,b,b,w,w,w,w,
        r,r,r,r,r,r,r,r,
        w,w,w,w,w,w,w,w,
        r,r,r,r,r,r,r,r,
        w,w,w,w,w,w,w,w,
]
sense.set_pixels(pixels1)
time.sleep(1)
pixels2= [
        b,b,b,b,w,w,w,w,
        b,b,b,b,w,w,w,w,
        b,b,w,b,w,w,w,w,
        w,w,w,w,w,w,w,w,
        b,w,w,b,r,r,r,r,
        w,b,b,w,r,r,r,r,
        b,b,b,b,r,r,r,r,
        b,b,b,b,r,r,r,r,
]
sense.set_pixels(pixels2)
time.sleep(1)
sense.clear()
