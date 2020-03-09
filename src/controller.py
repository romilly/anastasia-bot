from microbit import *
import radio

radio.on()

def say(command):
    radio.send(command)
    print(command)

while True:
    sleep(100)
    if button_a.is_pressed() and button_b.is_pressed():
        say('stop')
        continue
    if button_a.is_pressed():
        say('go_forward')
        continue
    if button_b.is_pressed():
        say('go_backward')
        continue