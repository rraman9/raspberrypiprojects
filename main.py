import urllib.request
import time
import RPi.GPIO as GPIO
import pygame


def isWebsiteUp(url):
    try:
        page = urllib.request.urlopen(url)
        # print (page.read())
        if page.getcode() == 200:
            GPIO.output(4,GPIO.HIGH)
            pygame.mixer.music.load("/home/pi/lightson/raspberrypiprojects/audio/up.mp3")
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.load("/home/pi/lightson/raspberrypiprojects/audio/down.mp3")
            pygame.mixer.music.play()
            GPIO.output(4,GPIO.LOW)
    except:
        pygame.mixer.music.load("/home/pi/lightson/raspberrypiprojects/audio/down.mp3")
        pygame.mixer.music.play()
        GPIO.output(4,GPIO.LOW)

def periodicCheckWebsiteUp(url, sleeptime):
    while True:
        print(isWebsiteUp(url))
        time.sleep(sleeptime)
        
def piSetup():
    
    #Setup GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(4,GPIO.OUT)
    
    # Setup audio
    pygame.mixer.init()
    
piSetup()
periodicCheckWebsiteUp("http://ec2-13-127-120-28.ap-south-1.compute.amazonaws.com", 5)