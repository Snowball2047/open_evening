from gpiozero import TrafficHat
from time import sleep
from signal import pause

hat = TrafficHat()
green = hat.lights.green
amber = hat.lights.amber
red = hat.lights.red
buzzer = hat.buzzer
button = hat.button

green.off()
