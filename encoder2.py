
import gaugette.rotary_encoder
import gaugette.switch
import time
import os
from time import sleep
from pushbullet.pushbullet import PushBullet
#import wiringpi2 as wiringpi

A_PIN  = 7
B_PIN  = 9
SW_PIN = 8
Xapikey = "08767C1F6E15462D851BAAA5643B7E844"
encoder = gaugette.rotary_encoder.RotaryEncoder.Worker(A_PIN, B_PIN)
encoder.start()
switch = gaugette.switch.Switch(SW_PIN)
last_state = None
count = 0
ecou = 0
envoi = 1
delai = 10
apiKey = "iJqqpUXVEZiBuxFuv35LQYeigq4Ido0L"
p = PushBullet(apiKey)
devices = p.getDevices()
contacts = p.getContacts()
#p.pushNote(devices[0]["iden"], 'Hello world', 'Test body')
#wiringpi.wiringPiSetupGpio()
#wiringpi.pinMode(21, 0)
#wiringpi.digitalRead(21)
#p.pushList( "list", "courses", "tomates", "oeufs", "pain", "eau", "mayo")
while True :
    #delta = encoder.get_delta()
    sleep(0.5)
    timer = time.time()
    ecou = timer + delai
    sw_state = switch.get_state()
    #print "boucle1"
    while sw_state == 1 :
	#print "boucle2"
	sleep(0.5)
	sw_state = switch.get_state()
        delta = encoder.get_delta()
        timer = time.time()
        if delta!=0:
            count = delta + count
            ecou = timer + delai
            envoi = 0
            #print "rotate %d" % count

        if envoi == 0 :
            if timer > ecou :
                #print "temps ecoule"
                #print "os.system(curl -H "Content-Type: application/json" --request POST --data '{"command": "pause"}' --header 'X-ApiKey: apikey' --verbose http://127.0.0.1:5000/api/job)"
                #os.system("curl -H \"Content-Type: application/json\" --request POST --data \'{\"command\": \"pause\"}\' --header \'X-ApiKey: apikey\' --verbose http://127.0.0.1:5000/api/job")
		p.pushNote(devices[0]["iden"], 'Probleme de filament', ' ')
                print "curl -H \"Content-Type: application/json\" --request POST --data \'{\"command\": \"pause\"}\' --header \'X-Api-Key: %s\' --verbose http://127.0.0.1/api/job" %Xapikey
		os.system ("curl -H \"Content-Type: application/json\" --request POST --data \'{\"command\": \"pause\"}\' --header \'X-Api-Key: %s\' --verbose http://127.0.0.1/api/job" %Xapikey)
		sleep(0.5)
		print "curl -H \"Content-Type: application/json\" --request POST --data \'{\"command\": \"home\", \"axes\": [\"x\", \"y\"]}\' --header \'X-Api-Key: %s\' --verbose http://127.0.0.1/api/printer/printhead" %Xapikey
		os.system ("curl -H \"Content-Type: application/json\" --request POST --data \'{\"command\": \"home\", \"axes\": [\"x\", \"y\"]}\' --header \'X-Api-Key: %s\' --verbose http://127.0.0.1/api/printer/printhead" %Xapikey)
		sleep(0.5)
		print "curl -H \"Content-Type: application/json\" --request POST --data \'{\"command\": \"M109 S50\"}\' --header \'X-Api-Key: %s\' --verbose http://127.0.0.1/api/printer/command"  %Xapikey
		os.system ("curl -H \"Content-Type: application/json\" --request POST --data \'{\"command\": \"M104 S10\"}\' --header \'X-Api-Key: %s\' --verbose http://127.0.0.1/api/printer/command"  %Xapikey)
                envoi = 1
