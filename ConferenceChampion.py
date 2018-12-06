#this script will help you attend security conferences like Schmoocon. 
#Use it to start a loop that will check the time and if it is the defined time that the conference registration open (ex. December 13th 2018 at Noon EST) it'll open 5 webpages
#

#import demz libs
import webbrowser
import datetime
import time

myTime = datetime.datetime.now()
registrationOpen = datetime.datetime(2018, 12, 5, 12, 0, 0)
url = "http://landing.shmoocon.org/" 

print(registrationOpen)

while datetime.datetime.now().replace(microsecond=0) != registrationOpen:
	time.sleep(0.01)
	print(datetime.datetime.now())

else:
	webbrowser.open(url)
	webbrowser.open(url)
	webbrowser.open(url)
	webbrowser.open(url)
	webbrowser.open(url)
	webbrowser.open(url)
	print("good luck, Chuck! :)")


