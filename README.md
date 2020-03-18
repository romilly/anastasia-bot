# Anastasia

A wheel-based mobile robot, named after [Dan Dare's spaceship](http://www.dandare.org/dan/anastasia/anastasia.htm) in the Eagle Comic (a classic from my childhood).

![Anastasia](docs/images/anastasia-with-dylaog-battery.jpg)

Initially Anastasia is being driven by a micro:bit and a separate micro:bit controller, programmed in micropython and using radio to communicate.

The motors are controlled by a Kitronik motor controller.

Later I plan to replace the micro:bit by an Adafruit Clue and to add Quadrature encoders and a ToF sensor.

I'll control the Clue version via bluetooth.

You can read more about the project on my blog:
 
1. [Introduction](https://blog.rareschool.com/2020/03/yet-another-homebrew-robot.html).
1. [Anatasia goes live on GitHub](https://blog.rareschool.com/2020/03/anastasia-is-simple-home-brew-robot-now.html)
1. [Controller Code](https://blog.rareschool.com/2020/03/controlling-anastasia-from-second.html)
1. [Code for Anastasia](https://blog.rareschool.com/2020/03/driving-anastasias-kitronik-motor.html)


## Building your own Anastasia

I built Anastasia from parts I had to hand. They are all readily available, apart from the Dyalog Phone Charger Battery for which there are plenty of alternatives.

Version one of Anastasia needed no soldering. If you don't want to solder your version, that will restrict your choice of motor. Some have leads pre-soldered, some do not.

Version 2 (the current version) has a little strip board power controller, with a USB socket, a switch, an LED, a resistor and a terminal block for output. That's entirely optional, and I discuss alternatives in the build instructions. If you don't want to build it, the rest of Anastasia needs no soldering.

I'm currently working on adding an inexpensive LIDAR distance sensor to Anastasia. There are some technical challenges, but if I can overcome them I will add details to this repository. That will be a rather more advanced project, and it will need some soldering.

Here's the BOM (Bill of Materials), along with the sources I used.

When I started the project Anastasia was connected to a battery holder and powered by 4 AA rechargeable batteries. 

Later I replaced the battery holder by a little strip board circuit with an on-off switch, a power LED, and a USB power socket.

I've listed these as alternatives in the [BOM](BOM.md) and in the assembly instructions which I will add shortly.



#### Assembly Instructions

**Coming later today!**



## Project Plan

I'm using Freeplane (a free Mind Map editor) for [planning](plan/anastasia-bot-plan.mm). Not everyone uses this software so I have shown the current state of the planning map below.

![Plan](docs/images/anastasia-bot-plan.svg)


