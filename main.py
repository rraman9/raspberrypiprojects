import urllib.request
import time
import RPi.GPIO as GPIO
import pygame

def isWebsiteUp(url, currentStatus):
    isUp = currentStatus
    try:
        page = urllib.request.urlopen(url)
        # print (page.read())
        if page.getcode() == 200 and not isUp:
            isUp = True
            handleWebsiteUp()
        elif isUp and page.getCode() != 200:
            isUp = False
            handleWebsiteDown()
    except:
        if isUp:
            isUp = False
            handleWebsiteDown()
    return isUp


def handleWebsiteDown():
    playfile("/home/pi/lightson/raspberrypiprojects/audio/down.mp3")
    GPIO.output(4, GPIO.LOW)


def handleWebsiteUp():
    GPIO.output(4, GPIO.HIGH)
    playfile("/home/pi/lightson/raspberrypiprojects/audio/up.mp3")


def periodicCheckWebsiteUp(url, sleeptime):
    currentStatus = False
    while True:
        currentStatus = isWebsiteUp(url, currentStatus)
        time.sleep(sleeptime)

def playfile(filename):
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
        
def piSetup():
    
    #Setup GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(4,GPIO.OUT)
    
    # Setup audio
    pygame.mixer.init()
    
piSetup()
periodicCheckWebsiteUp("http://ec2-13-127-120-28.ap-south-1.compute.amazonaws.com", 5)