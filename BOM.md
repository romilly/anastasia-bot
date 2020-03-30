# Bill of Materials

## Anastasia and Controller

**Notes**

1. *Generic* is my shorthand for *available from lots of places - any will do!* 
1. The Caster and Brackets come with their own mounting nuts and bolts.
1. You'll need *two* micro:bits - one for Anastasia, one for the controller.
1. Alternative motors are widely available, but you'll need to check a few things.
    1. Make sure the motors are described as *TT motors*.
    1. Make sure the motors can run off 3-6 volts. Some appear to be 3v only; these might burn out.
    1. Make sure the motors will fit the Motor brackets. Some have a large raised pillar around their shaft.
    1. Make sure the size and shape of the motor shaft matches the wheels you get.
    1. If you don't want to do any soldering, make sure the motors have wires attached.
    
*For Anastasia:*

|-|Component|Qty|Where I got it/them|Comment|
|-:|---|-:|--|-------|
|1|Pololu board|1|[Proto-PIC](https://www.proto-pic.co.uk/product/pololu-1532-rp5rover-5-expansion-plate-rrc07a-narrow-solid-blue/)|
|2|Adafruit caster 1.3"|1|[The Pi Hut](https://thepihut.com/products/adafruit-supporting-swivel-caster-wheel-1-3-diameter)|
|3|micro:bit|1|[Kitronik](https://www.kitronik.co.uk/5613-bbc-microbit-board-only.html)|for Anastasia|
|4|TT motor|2|[The Pi Hut](https://thepihut.com/products/adafruit-dc-gearbox-motor-tt-motor-200rpm-3-to-6vdc-ada3777)|Slow but powerful|
|5|TT wheel|2|[The Pi Hut](https://thepihut.com/products/adafruit-orange-and-clear-tt-motor-wheel-for-tt-dc-gearbox-motor-ada3766)|Fits the motor above|
|6|Kitronik Motor Controller|1|[Kitronik](https://www.kitronik.co.uk/5620-motor-driver-board-for-the-bbc-microbit-v2.html)|v 2.0|
|7|M3 spacers, bolts, nuts|4|Generic||
|8|Adafruit motor brackets|2|[The Pi Hut](https://thepihut.com/products/adafruit-motor-mount-for-tt-gearbox-dc-motors-l-bracket-type-ada3768)||

*For programming the micro:bits:*

|Component|Qty|Where I got it/them|Comment|
|---|-:|--|-------|
|USB A to micro_B lead|1|Generic|Make sure it's a data transfer cable!|

*For the controller:*

|Component|Qty|Where I got it/them|Comment|
|---|-:|--|-------|
|AA battery|2|Generic|Rechargeable batteries are greener.|
|battery holder with switch|1|[Kitronik](https://www.kitronik.co.uk/2268-2x-aa-battery-box-with-switch-and-connector.html)
|micro:bit|1|[Kitronik](https://www.kitronik.co.uk/5613-bbc-microbit-board-only.html)|for controller|

To power Anastasia you'll need **one of the alternatives below**:

### If you use a simple battery holder for Anastasia

|Component|Qty|Where I got it/them|Comment|
|---|-:|--|-------|
|battery holder|1|Generic|4 cells. Make sure it has leads attached!|
|AA cells|4|Generic|Rechargeable batteries are greener.|


### If you use a Phone charger and stripboard with switch

|Component|Qty|Where I got it/them|Comment|
|---|-:|--|-------|
|switch|1|[BitsBox](https://www.bitsbox.co.uk/index.php?main_page=product_info&cPath=116_120_124_125&products_id=2364)||
|Stripboard (9x27)|1|[BitsBox](https://www.bitsbox.co.uk/index.php?main_page=product_info&cPath=238_244&products_id=1855)|If cut down, >= 6x20|
|Adafruit USB socket|1|[Pimoroni](https://shop.pimoroni.com/products/adafruit-usb-micro-b-breakout-board)||
|Mobile charger|1|Generic|Use any charger that can provide 5V @ >=1A|
|Resistor 470R 1/8W 5%|1|Generic|1/4 W would also be OK|
|LED 3mm|1|Generic||
|short USB lead|1|Generic|to connect battery + power unit|
