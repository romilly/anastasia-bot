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

I built Anastasia from parts I had to hand. They are all readily available, apart from the Dyalog Phone Charger Battery for which there are plenty of alternatives.)

Here's the BOM (Bill of Materials), along with the sources I used.

When I started the project Anastasia was connected to a battery holder and powered by 4 AA rechargeable batteries. 

Later I replaced the battery holder by a little stripboard circuit with an on-off switch, a power LED, and a USB power socket.

I've listed these as alternatives in the BOM and in the instructions below.

### Bill of Materials

#### Anastasia and Controller

|Component|Qty|Where I got it|Comment|
|-----------------------------------------|---|--------------|-------|
|micro:bit|2|[Kitronik](https://www.kitronik.co.uk/5613-bbc-microbit-board-only.html)|One for Anastasia, one for the controller|
|Kitronik micro:bit Motor Controller|1|[Kitronik](https://www.kitronik.co.uk/5620-motor-driver-board-for-the-bbc-microbit-v2.html)|v 2.0|
|battery holder with switch|1|[Kitronik](https://www.kitronik.co.uk/2268-2x-aa-battery-box-with-switch-and-connector.html)
|usb lead for programming|1|Generic|Make sure it's a data lead, not just a power lead!|
|Pololu board|1|
|Resistor 470R 1/8W|
|motor|2|
|wheel|2|
|M3 bolts|4|
|M3 nuts|4|
|M3 standoffs|4|
|caster|1|
|AA battery|2|

and **one of the alternatives below**:

#### If you use a simple batter holder for Anatasia

|battery holder|1|
|AA battery|4|


#### If you use Phone charger and stripboard with switch

|AA cells|4|Generic|Rechargeable batteries are greener|
|switch|1|||
|LED 3mm|1|Generic||
|USB socket|1|[Pimoroni]()|
|short USB lead to connect battery + power unit|1|Generic|
|Stripboard (9x27)|1|[BitsBox]()|If cut down, >= 6x20|



#### Controller



## Project Plan

I'm using Freeplane (a free Mind Map editor) for [planning](plan/anastasia-bot-plan.mm). Not everyone uses this software so I have shown the current state of the planning map below.

![Plan](docs/images/anastasia-bot-plan.svg)


