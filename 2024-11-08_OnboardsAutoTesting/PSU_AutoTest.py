# To open ENV remember to go to the root folder and than activate using "envTest\Scripts\Activate.ps1"

# RP lab PSU ID: "USB0::0x0483::0x7540::SPD3XHBD2R5155::INSTR" (in COM port 5)

# Works!

import pyvisa
import time # for sleep

time_delay = 0.05

def main():
    rm = pyvisa.ResourceManager()
    print("Resources detected\n{}\n".format(rm.list_resources()))

    PSU = rm.open_resource('USB0::0x0483::0x7540::SPD3XHBD2R5155::INSTR') # Put your device IDs here

    PSU.timeout = 3000
    PSU.read_termination = '\n'
    PSU.write_termination = '\n'
    #PSU.baud_rate = 9600

    time.sleep(0.04)
    print("Performing Configuration...")
    #PSU.write('INSTrument CH1')   # Select Ch1
    #time.sleep(.5)
    PSU.write('OUTPut CH1,OFF')   # start OFF - safe :)
    time.sleep(time_delay)
    PSU.write('CH1:CURRent 0.4') # 0.5A
    time.sleep(time_delay)
    PSU.write('CH1:VOLTage 5.0') # apply 5V
    time.sleep(time_delay)
    PSU.write('OUTPut CH1,ON')   # Turn on PSU channel
    print("Configuration complete!")

    time.sleep(time_delay)
    PSU.write('*IDN?') #Write instrument and ask for identification string
    time.sleep(time_delay) #Wait
    qStr = PSU.read() #Read instrument response
    print (str(qStr)) #Print returned string
    time.sleep(time_delay) #Wait
    PSU.write('OUTPut CH1,OFF')   # Turn OFF - safe :)
    time.sleep(time_delay) #Wait
    PSU.close() #Close instrument VISA session


if __name__ == '__main__':
    main()
