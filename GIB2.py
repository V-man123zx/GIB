from machine import Pin

import random

from utime import sleep

blue = Pin(9, Pin.OUT)
red = Pin(22, Pin.OUT)
yellow = Pin(5, Pin.OUT)
green = Pin(28, Pin.OUT)

bbutton = Pin(13, Pin.IN, Pin.PULL_DOWN)
rbutton = Pin(18, Pin.IN, Pin.PULL_DOWN)
gbutton = Pin(27, Pin.IN, Pin.PULL_DOWN)
ybutton = Pin(0, Pin.IN, Pin.PULL_DOWN)

random.seed(2021)

while True:
    x = random.randrange(3, 7)
    sleep(x)
    blue.on()
    red.on()
    yellow.on()
    green.on()
    sleep(.1)
    while True:
        if rbutton.value():
            blue.off()
            red.off()
            yellow.off()
            green.off()
            sleep(.1)
            red.on()
            sleep(2)
            red.off()
            break
        elif bbutton.value():
            blue.off()
            red.off()
            yellow.off()
            green.off()
            sleep(.1)
            blue.on()
            sleep(2)
            blue.off()
            break
        elif gbutton.value():
            blue.off()
            red.off()
            yellow.off()
            green.off()
            sleep(.1)
            green.on()
            sleep(2)
            green.off()
            break
        elif ybutton.value():
            blue.off()
            red.off()
            yellow.off()
            green.off()
            sleep(.1)
            yellow.on()
            sleep(2)
            yellow.off()
            break
