from flask import Flask
app = Flask(__name__)
from flask import render_template
from components.TemperatureSensor import TemperatureSensor
from components.Led import Led
ledr = Led(18)
ledb = Led(24)
@app.route('/')
def hello_world():
    temp = TemperatureSensor()
    celsius = temp.read_temp_c()
    fahrenheit = temp.read_temp_f()
    if (celsius < 15 ):
        ledb.allumer()
        ledr.eteindre()
    elif(15<= celsius< 30):
        ledb.allumer()
        ledr.allumer()
    elif(celsius>=30):
        ledr.allumer()
        ledb.eteindre()
    return  render_template('temperature.html', celsius = celsius, fahrenheit = fahrenheit)

