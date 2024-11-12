import csv
import serial
import time
from datetime import datetime
import pytz


# Sets current time to time since 1970 in seconds (needed for CSV)
def update_time():
    return int((datetime.now() - datetime(1970, 1, 1)).total_seconds() * 1000)

# Read from multimeter and logs to CSV with time
def multRead(runtime):
    pst_timezone = pytz.timezone('America/Los_Angeles')

    # Multimeter Setup
    ser = serial.Serial(
        port='COM7',  # Set COM port (check device manager)
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )

    # Finds current day and time for CSV
    current_time_utc = datetime.now(pytz.utc)
    current_time_pst = current_time_utc.astimezone(pst_timezone)
    current_date_pst = current_time_pst.strftime('%Y-%m-%d')
    formatted_time = current_time_pst.strftime('%H-%M-%S')
    
    # ser.write(b'*IDN?\r')

    # Name CSV
    csvName = (f'PowerConsumption_{current_date_pst}_{formatted_time}.csv')
    
    # Writes to CSV
    with open(csvName, mode='w', newline='') as csvfile:
        fieldnames = ['Time', 'Voltage', 'Current']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        # Sets starting time
        startingTime = datetime.now()
        startingTimeSeconds = startingTime.hour * 60 * 60 + startingTime.minute * 60 + startingTime.second + startingTime.microsecond / 1000000
        endingTimeSeconds = startingTimeSeconds + runtime
        
        # Decodes binary to ascii
        # value = ser.read(100).decode('ascii').strip() # multimeter reads first value without logging to CSV

        while((datetime.now().hour * 60 * 60 + datetime.now().minute * 60 + datetime.now().second + datetime.now().microsecond / 1000000 )< endingTimeSeconds):
            
            value = ser.read(100).decode('ascii').strip() # ********** DO I NEED ***********

            # Seperates voltage and current with a comma
            if value and ',' in value:

                values = value.split(',')
                voltageValue = values[0]
                currentValue = values[1]

                timestamp = update_time()

                # Prints values to terminal
                print(f"Time: {timestamp}, Voltage: {voltageValue}, Current: {currentValue}")

                # Logs to CSV
                row_data = {"Time": timestamp, "Voltage": voltageValue, "Current": currentValue}
                writer.writerow(row_data)
                csvfile.flush()
                
                
    return csvName
    ser.close()
    
    