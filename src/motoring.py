from microbit import *
import radio

left = (pin16, pin0)
right = (pin8, pin12)

forward = (0, 1)
backward = (1, 0)
coast = (0, 0)
brake = (1,1)


class Driver:
    def __init__(self):
        radio.on()
        self.commands = {
            'stop' :        self.stop,
            'go_forward':   self.go_forward,
            'go_backward':  self.go_backward,
        }

    def stop(self):
        self.do(left,brake)
        self.do(right, brake)

    def go_forward(self):
        self.do(left, forward)
        self.do(right, forward)

    def go_backward(self):
        self.do(left, backward)
        self.do(right, backward)

    def do(self, side, direction):
        for i in range(2):
            side[i].write_digital(direction[i])

    def run(self):
        while True:
            message = radio.receive()
            if message is not None and message in self.commands:
                command = self.commands[message]
                command()
            sleep(50) # 50 ms


Driver().run()