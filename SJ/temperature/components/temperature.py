# Imports
import os
import glob
import time

# Intialisation des broches
os.system('modprobe w1-gpio')  # Allume le module 1wire
os.system('modprobe w1-therm')  # Allume le module Temperature

# Chemin du fichier contenant la température (remplacer par votre valeur trouvée précédemment)
device_file = '/sys/bus/w1/devices/28-01131a3eb0d1/w1_slave'

class TemperatureSensor():
    def __init__(self):
        self.celcius = 0
        self.farenheit = 0
    def read_temp_raw(self):
        f = open(device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines
    def read_temp(self):
        lines = self.read_temp_raw()  # Lit le fichier de température
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = self.read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
            self.celcius = temp_c
    def read_temp_c(self):
        self.read_temp()
        print("Il fait {:0.2f}°C".format(self.celcius))
    def read_temp_f(self):
        self.read_temp()
        self.farenheit = (self.celcius*9/5)+32
        print("Il fait {:0.2f}°F".format(self.farenheit))
