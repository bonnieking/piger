import pygame
from pygame.locals import *
from updownbox import UpDownBox
from time import sleep

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

while True:
    #while pygame.event.poll().type != KEYDOWN:
    while True:
        if GPIO.input(4) == True:
            GPIO.output(17, GPIO.HIGH)
            GPIO.output(18, GPIO.HIGH)
            sleep(0.01)
            GPIO.output(17, GPIO.LOW)
            GPIO.output(18, GPIO.LOW)
            print "click!"
