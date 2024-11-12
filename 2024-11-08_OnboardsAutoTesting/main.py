# PSU setup: 
# - RP lab PSU ID: "USB0::0x0483::0x7540::SPD3XHBD2R5155::INSTR"

# Multimeter setup:
# - In multimeterToCSV.py set COM port
# - Turn on Print Rate: 1 ; (2nd + MIN MAX) ; (AUTO) to select
# - Set Rate: MEDIUM ; (RATE)
# - Set Voltage DC for main channel
# - Set Current DC for secondary channel ; (2nd + A)


import pyvisa
import time # for sleep
from readText import read, parseForDouble
from multimeterToCSV import update_time, multRead
from output import findOutput
from PSUwrite import setPSU, turnOffPSU
import csv
import serial
from datetime import datetime
import pytz
import matplotlib as plt

# print com port if not read***********

# add instructions on how to set up entire device and setup

def main():
    # Reads inputs from txt file
    Ch1V, Ch1I, Ch2V, Ch2I, Time = read('input.txt')
    
    # Sets values from txt file, Turns PSU on
    setPSU(Ch1V, Ch1I, Ch2V, Ch2I)
    
    # Delay for PSU to set values in time
    time.sleep(5)
    
    # Changes current time to seconds from 1970
    update_time()
    
    # Opens CSV and reads from multimeter
    csvName = multRead(Time)
    
    time.sleep(5)
    
    # Turns off PSU
    turnOffPSU()
    
    # Outputs graph and calculations
    findOutput(csvName)

    
if __name__ == '__main__':
    main()
    
    # to do: com port, fix turn off psu, csv file name doesn't have date, add hz test file, rename txt file