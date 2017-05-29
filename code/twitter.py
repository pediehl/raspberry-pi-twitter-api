#!/usr/bin/python3
import time
import Adafruit_DHT
from twython import Twython
from datetime import datetime


sensor = Adafruit_DHT.DHT11
pin = 21

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)


 
while 1:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)                   
        if humidity is not None and temperature is not None:
	   
           message  = "Raumklima"
           message  += " am: %s - " %datetime.now ().strftime ('%d.%m.%Y um %H:%M Uhr')
           message  += "Temp: %0.1f*C" % (temperature)
           message  += " Luftfeuchte: %0.1f%%" % (humidity)
           time.sleep(60)
           twitter.update_status(status=message)
           print("Tweeted: %s" % message)

        else:
                        print('Fehler beim Einlesen der Daten. Starte einen weiteren Versuch!')

