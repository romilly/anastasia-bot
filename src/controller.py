from microbit import *
import radio

radio.on()

while True:
    if button_a.is_pressed():
        radio.send('start')
    elif button_b.is_pressed():
        radio.send('stop')
    sleep(100)