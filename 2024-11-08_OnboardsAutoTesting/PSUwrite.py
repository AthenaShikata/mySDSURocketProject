import pyvisa
import time # for sleep

def setPSU(Ch1V, Ch1I,Ch2V, Ch2I):
    
    time_delay = 0.05 # Delay between PSU commands need
    
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
    PSU.write('CH1:VOLTage ' + str(Ch1V)) # Apply voltage to channel 1
    time.sleep(time_delay)
    PSU.write('CH1:CURRent ' + str(Ch1I)) # Apply current to channel 1
    time.sleep(time_delay)
    PSU.write('OUTPut CH1,ON')   # Turn on PSU channel
    
# Turn off PSU at end
def turnOffPSU():
    # time_delay = 0.05
    
    # time.sleep(time_delay)
    
    rm = pyvisa.ResourceManager()
    PSU = rm.open_resource('USB0::0x0483::0x7540::SPD3XHBD2R5155::INSTR') # Put your device IDs here
    
    # time.sleep(time_delay)

    PSU.write('OUTPut CH1,OFF')
    print("psuoff")
    
    # PSU.close()
    
    