import machine

dac_tone = machine.DAC('P21')   # create a DAC object
dac_tone.tone(20000, 0)          # set tone output to 1kHz
