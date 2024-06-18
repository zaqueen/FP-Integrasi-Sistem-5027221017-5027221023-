#This Program will subscribe to /afzal-home/room/temperature topic and Check the Command
#If Program Receive "On" From the Broker then it will turn on the LED 
#If Receive "Off" Command then it will turn off the LED
#pip install paho-mqtt

import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

GPIO_PIN = 18

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(GPIO_PIN, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and$

def on_connect(client, userdata, flags, rc):
    # subscribe, which need to put into on_connect
    # if reconnect after losing the connection with the broker, it will continue to subscribe to the raspberry/topic topic
    client.subscribe("/lab-kcks/room/led")

# the callback function, it will be triggered when receiving messages
def on_message(client, userdata, message):
    if str(message.payload.decode("utf-8"))=="On":
        GPIO.output(GPIO_PIN, GPIO.HIGH) # Turn on
    else:
        GPIO.output(GPIO_PIN, GPIO.LOW) # Turn Off
    print("message received " ,str(message.payload.decode("utf-8")))
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
# create connection, the three parameters are broker address, broker port number, and keep-alive time respectively
client.username_pw_set(username="admin",password="kcks1029")
client.connect("152.42.194.14", 1883, 60)
# set the network loop blocking, it will not actively end the program before calling disconnect() or the program crash
client.loop_forever()
