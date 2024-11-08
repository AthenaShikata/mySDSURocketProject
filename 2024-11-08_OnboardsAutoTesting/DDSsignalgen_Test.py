# To open ENV remember to go to the root folder and than activate using "envTest\Scripts\Activate.ps1"

# Lab's Signal Generator JDS6600 ID: "ASRL5::INSTR"


import pyvisa
import time # for sleep
import numpy as np
import matplotlib.pyplot as plt

time_delay = 0.05


def identify():
    rm = pyvisa.ResourceManager()
    print("Resources detected\n{}\n".format(rm.list_resources()))
    return rm

def ChanToggle(instr):
    rm = instr
    #print("Resources detected\n{}\n".format(rm.list_resources()))

    DDSsig = rm.open_resource('ASRL5::INSTR') # Put your device IDs here

    DDSsig.timeout = 3000
    DDSsig.read_termination = '\n'
    DDSsig.write_termination = '\n'
    DDSsig.baud_rate = 115200 # Baudrate for Lab Signal Generator

    time.sleep(0.01)
    DDSsig.write(":w20=1,1. <CR><LF>") # Turn on channels 1 and 2
    time.sleep(0.01)
    # : {w , r , a , b} {0-99} = {input},{input}. <CR><LF>
    DDSsig.write(":w23=25786,0. <CR><LF>") # Sine wave at 257.86 Hz for channel 1
    time.sleep(0.01)
    DDSsig.write(":w24=25786,0. <CR><LF>") # Sine wave at 257.86 Hz for channel 2
    time.sleep(2)
    DDSsig.write(":w20=0,0. <CR><LF>") # Turn off channels 1 and 2



def main(instr):
    rm = instr
    DDSsig = rm.open_resource('ASRL5::INSTR') # Put your device IDs here

    DDSsig.timeout = 3000
    DDSsig.read_termination = '\n'
    DDSsig.write_termination = '\n'
    DDSsig.baud_rate = 115200 # Baudrate for Lab Signal Generator

    #DDSsig.write(":w20=1,1. <CR><LF>") # Turn on channels 1 and 2
    #time.sleep(0.01)

    DDSsig.write(":w23=10000,0. <CR><LF>") # Sine wave at 100 Hz for channel 1
    time.sleep(0.01)
    DDSsig.write(":w24=20000,0. <CR><LF>") # Sine wave at 200 Hz for channel 2
    time.sleep(0.01)
    DDSsig.write(":w20=1,1. <CR><LF>") # Turn on channels 1 and 2
    time.sleep(3)
    DDSsig.write(":w20=0,0. <CR><LF>") # Turn on channels 1 and 2






if __name__ == '__main__':
    gen = identify()
    #ChanToggle(gen) # Toggles Channels on and off
    main(gen)