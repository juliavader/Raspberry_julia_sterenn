import RPi.GPIO as GPIO 
import time 
from Led import Led
from time import sleep

GPIO.setmode(GPIO.BCM)
#Initialisation de notre GPIO 17 pour recevoir un signal
#Contrairement à nos LEDs avec lesquelles on envoyait un signal
ledr = Led(18)
ledb = Led(24)
buzzer = 22
GPIO.setup(buzzer, GPIO.OUT)
broche = 17
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(broche, GPIO.IN)

currentstate = 0
previousstate = 0

# Boucle infini jusqu'à CTRL-C
while True:
    # Lecture du capteur
    currentstate = GPIO.input(broche)
		 # Si le capteur est déclenché
    if currentstate == 1 and previousstate == 0:
        print("    Mouvement détecté !")
        ledr.allumer()
        GPIO.output(buzzer, GPIO.HIGH)
        sleep(1)
        GPIO.output(buzzer, GPIO.LOW)
        
        ledb.eteindre()
        # En enregistrer l'état
        previousstate = 1
    # Si le capteur est s'est stabilisé
    elif currentstate == 0 and previousstate == 1:
        print("    Prêt")
        ledb.allumer()
        ledr.eteindre()
        previousstate = 0
    # On attends 10ms
    time.sleep(0.01)
