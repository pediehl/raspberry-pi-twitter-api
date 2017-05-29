# Raspberry Pi - Twitter Api & Raumklima twittern

## Vorraussetzung

* Twython für Python 3
* Temperatur/Luftfeuchtigkeits-Sensor
* Kabel
* Steckbrett



## Twython für Python 3 installieren (Raspbian Jessie)
Wir installieren Twython für Python 3.
Du musst online sein, um Pakete zu installieren.

Zunächst bringe dein System auf den aktuellen Stand:
```
sudo apt-get update
sudo apt-get upgrade
```
## Jetzt installieren wir Twython für Python 3:

sudo pip3 install twython

Testen Sie, was Sie brauchen, indem Sie die folgenden Befehle eingeben:

`python3 -c "import twython"`

Dies bringt Sie zurück zur Eingabeaufforderung ohne Fehler. Wenn du einen Fehler bekommst No module named X, dann sagst du, dass du die Befehle richtig eingegeben hast.

## Twython für Python 3 installieren für Raspbian Jessie Lite (Raspberry Pi Zero und alle älteren Modelle)

Zunächst bring dein System auf den aktuellen Stand:

```
sudo apt-get update
sudo apt-get upgrade
```

jetzt müssen wir python3 und python3-pip installieren:

`sudo apt-get install python3 python3-pip`

Im Anschluss können wir Twython für Python 3 installieren:

`sudo pip3 install twython`

Testen Sie, was Sie brauchen, indem Sie die folgenden Befehle eingeben:

`python3 -c "import twython"`

Dies bringt Sie zurück zur Eingabeaufforderung ohne Fehler. Wenn du einen Fehler bekommst No module named X, dann sagst du, dass du die Befehle richtig eingegeben hast.

## Installieren der Bibliothek von Adafruit für DHT11 & DHT22

`sudo apt-get install build-essential python-dev python-openssl git`

Zuerst laden wir die benötigte Bibliothek von Adafruit.

`git clone https://github.com/adafruit/Adafruit_Python_DHT.git && cd Adafruit_Python_DHT`

Dadurch wird eine Python Bibliothek angelegt, die wir einfach in unsere Projekte einbinden können.
Mit `sudo python3 setup.py install` installieren wir die benötigte Python Bibliothek.
