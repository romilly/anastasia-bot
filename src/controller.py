"""
Control Anastasia's motors from a second micro:bit.

This library detects how you want Anastasia to move based on how you tilt the micro:bit.
It uses the micro:bit radio to send your commands to the robot.
See `motoring.py` for the code that runs on Anastasia.
"""
from microbit import *
import radio

radio.on()
# The critical value for tilt detection.
# A lower value makes the controller more sensitive.
RANGE = 250


def say(command):
    """
    Send a command over the the radio

    :param command: The outgoing command, or None if a command was not required.
    :return: True if there was a command to send
    """
    if command is not None:
        radio.send(command)
        return True
    return False


def react_to_tilt(tilt, low, high):
    """
    Determine the command to send based on how the controller is tilted.

    :param tilt: the tilt angle of the micro:bit in the x or y direction
    :param low: the message to send if the tilt is below the critical value
    :param high: the message to send if the tilt is abovee the critical value
    :return: a message, or None if the micro:bit is held level
    """
    if tilt > RANGE:
        return high
    if tilt < - RANGE:
        return low
    return None


def check_tilt():
    """
    Send the appropriate command based on how the micro:bit is tilted.
    """
    if say(react_to_tilt(accelerometer.get_x(), 'right', 'left')):
        return
    if say(react_to_tilt(accelerometer.get_y(), 'forward', 'backward')):
        return
    # micro:bit is more or less level, so stop the robot.
    say('stop')


while True:
    """
    Loop forever looking for commands to send ten times a second.
    """
    sleep(100)
    check_tilt()



