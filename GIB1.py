from machine import Pin

import random

from utime import sleep

led = Pin(0, Pin.OUT)

blue = Pin(9, Pin.OUT)
red = Pin(22, Pin.OUT)
yellow = Pin(5, Pin.OUT)
green = Pin(28, Pin.OUT)

bbutton = Pin(2, Pin.IN, Pin.PULL_DOWN)
rbutton = Pin(1, Pin.IN, Pin.PULL_DOWN)
gbutton = Pin(15, Pin.IN, Pin.PULL_DOWN)
ybutton = Pin(16, Pin.IN, Pin.PULL_DOWN)

random.seed(2021)

while True:
    x = random.randrange(3, 7)
    sleep(x)
    red.on()
    blue.on()
    yellow.on()
    green.on()
    sleep(.1)
    while True:
        if rbutton.value():
            led.off()
            red.on()
            sleep(2)
            red.off()
            break
        elif bbutton.value():
            led.off()
            blue.on()
            sleep(2)
            blue.off()
            break
        elif gbutton.value():
            led.off()
            green.on()
            sleep(2)
            green.off()
            break
        elif ybutton.value():
            led.off()
            yellow.on()
            sleep(2)
            yellow.off()
            break
