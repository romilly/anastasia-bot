"""
Obey incoming commands using the Kitronik Motor Conroller.

Commands are senf from a second micro:bit using the radio.
See `controller.py` for the code that runs on the controller micro:bit.
"""
from microbit import *
import radio


class Driver:
    """
    Read incoming radio messages and send commands to the motor controller.
    """
    def __init__(self, left_pins=(pin16, pin0), right_pins=(pin8, pin12)):
        """
        Configure the controls and map commands to bound methods.

        :param left_pins:
        :param right_pins:

        See https://blog.rareschool.com/ for more details

        See https://www.kitronik.co.uk/pdf/5620-motor-driver-board.pdf for Kitronik's data sheet.
        """
        self.pins = left_pins+right_pins
        radio.on()
        self.commands = {
            'stop' :    self.stop,
            'forward':  self.go_forward,
            'backward': self.go_backward,
            'left':     self.spin_left,
            'right':    self.spin_right,
        }

    def stop(self):
        """
        Set both motors to brake.
        """
        self.set_control_pins(1, 1, 1, 1)

    def go_forward(self):
        """
        Set both motors to run forward.
        """
        self.set_control_pins(0, 1, 0, 1)

    def go_backward(self):
        """
        Set both motors to run backwards.
        """
        self.set_control_pins(1, 0, 1, 0)

    def spin_left(self):
        """
        Set left motor to run backwards, right motor to run forwards
        """
        self.set_control_pins(1, 0, 0, 1)

    def spin_right(self):
        """
               Set left motor to run forwards, right motor to run backwards
               """
        self.set_control_pins(0, 1, 1, 0)

    def set_control_pins(self, *pin_values):
        """
        Set the contol pins for the motor contoller
        :param pin_values: four values for the four control pins
        :return:
        """
        for pin, pin_value in  zip(self.pins, pin_values):
            pin.write_digital(pin_value)

    def obey(self, message):
        """
        Map a valid message to a method and run it.

        :param message: the message to obey, or None if no message was received.
        :return:
        """
        if message is None or message not in self.commands:
            return
        # execute the bound method if a valid message was recceived.
        self.commands[message]()

    def run(self):
        """
        Loop forever looking for messages to obey.
        """
        while True:
            self.obey(radio.receive())
            sleep(50) # 50 ms


Driver().run()