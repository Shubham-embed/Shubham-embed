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
    pycom.rgbled(0x007f00)
    time.sleep(10)
    pycom.rgbled(0x000000)
    bleh = (i2c.readfrom(0x21, 1))
    print(bleh)
i2c = I2C(0, I2C.MASTER, baudrate=100000)
# print(i2c.scan()) # returns list of slave addresses
p_in = Pin('P13', mode=Pin.IN, pull=Pin.PULL_UP)
p_in.callback(Pin.IRQ_FALLING | Pin.IRQ_RISING, pin_handler)
