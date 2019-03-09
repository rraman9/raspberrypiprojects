import urllib.request
import time

def isWebsiteUp(url):
    try:
        page = urllib.request.urlopen(url)
        # print (page.read())
        if page.getcode() == 200:
            return True
        else:
            return False
    except:
        return False

def periodicCheckWebsiteUp(url, sleeptime):
    while True:
        print(isWebsiteUp(url))
        time.sleep(sleeptime)

periodicCheckWebsiteUp("http://ec2-13-127-120-28.ap-south-1.compute.amazonaws.com", 5)