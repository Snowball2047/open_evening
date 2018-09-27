from gpiozero import TrafficHat
from time import sleep
from signal import pause


hat = TrafficHat()
green = hat.lights.green
amber = hat.lights.amber
red = hat.lights.red
buzzer = hat.buzzer
button = hat.button

def end():
    if button.is_active:
        green.off()
        amber.off()
        red.off()
        exit()

def sound(time, loop):
    for i in range(loop):
        buzzer.on()
        print('Buzzer: on')
        sleep(time)
        buzzer.off()
        print('Buzzer: off')
        sleep(time)
        end()

def flash(time, loop, colour):
    for i in range(loop):
        colour.on()
        print('Flash: on')
        sleep(time)
        colour.off()
        print('Flash: off')
        sleep(time)
        end()

def cross():
    green.off()
    amber.on()
    sleep(4)
    amber.off()
    red.on()
    sound(0.1, 7)
    red.off()
    flash(0.5, 5, amber)
    green.on()
    end()
    
green.on()
amber.off()
red.off()
while(True):
    button.wait_for_press()
    cross()
