import pycom
import machine
import time
import math
from array import array

use = "DACA" # comment this depending on what function you want to use

if use == "ADC":
    adc = machine.ADC() # Create adc object
    apin = adc.channel(pin='P16')   # create an analog pin on P16

    while True:
        val = apin()
        print(val)
        time.sleep(0.1)

elif use == "DAC":
    dac_tone = machine.DAC('P21')   # create a DAC object
    dac_tone.tone(20000, 0)          # set tone output to 1kHz
