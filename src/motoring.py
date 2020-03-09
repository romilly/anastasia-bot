from microbit import *
import radio

left = (pin16, pin0)
right = (pin8, pin12)

forward = (0, 1)
backward = (1, 0)
coast = (0, 0)
brake = (1,1)

# TODO: make class
# add methods for go_forward, go_back, start, stop, turn_left, turn_right
# Add running instance variable
# map incoming commands to bound methods and run them

# TODO: When complete, add doc comments

def move(side, direction):
    for i in range(2):
        side[i].write_digital(direction[i])


move(left, brake)
move(right,brake)

controls = {'start' : (forward, forward),
            'stop': (brake, brake),
            }
radio.on()
while True:
    message = radio.receive()
    if message is not None and message in controls:
        move(left, controls[message][0])
        move(right, controls[message][1])
    sleep(50)
