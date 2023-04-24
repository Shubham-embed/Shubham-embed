from machine import I2C
from machine import SD
import os
import pycom
from machine import Pin
import time

from machine import Pin

pycom.heartbeat(False)

def pin_handler(arg):
    print("got an interrupt in pin %s" % (arg.id()))
    bleh = (i2c.readfrom(0x21, 1))
    if bleh == b'\xfd':
        print("POE in")
        pycom.rgbled(0x007f00)
        time.sleep(5)
    else:
        print("POE out")
        pycom.rgbled(0x7f0000)
        time.sleep(5)


pycom.rgbled(0x007f00)
time.sleep(10)
pycom.rgbled(0x000000)
i2c = I2C(0, I2C.MASTER, baudrate=100000)
# print(i2c.scan()) # returns list of slave addresses

p_in = Pin('P13', mode=Pin.IN, pull=Pin.PULL_UP)
p_in.callback(Pin.IRQ_FALLING | Pin.IRQ_RISING, pin_handler)


# pycom.heartbeat(False)
# while True:
#     Interrupt = Pin('P13', mode = Pin.IN)
#     if Interrupt ==1:
#         print(" yeah 1")
#         pycom.rgbled(0x007f00)
#         time.sleep(10)
#     else:
#         print(" nahh 0")
#         pycom.rgbled(0x7f0000)
#         time.sleep(10)


# print(bleh)
#
#

# # pycom.rgbled(0xff00)
# pycom.rgbled(0x7f7f00)
