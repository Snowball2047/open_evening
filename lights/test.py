from gpiozero import TrafficHat
from time import sleep
from signal import pause

hat = TrafficHat()
green = hat.lights.green
amber = hat.lights.amber
red = hat.lights.red
buzzer = hat.buzzer
button = hat.button

def activate():
    green.on()
    sleep(1)
    green.off()
    amber.on()
    sleep(1)
    amber.off()
    red.on()
    sleep(1)
    red.off()
    buzzer.on()
    sleep(1)
    buzzer.off()

def sound(time,loop):
    for i in range(loop):
        buzzer.on()
        print('Buzzer: on')
        sleep(time)
        buzzer.off()
        print('Buzzer: off')
        sleep(time)

hat.button.wait_for_press()
activate()
