import csv
import serial
import time
from datetime import datetime
import pytz

pst_timezone = pytz.timezone('America/Los_Angeles')

def update_time():
    current_time_utc = datetime.now(pytz.utc)
    current_time_pst = current_time_utc.astimezone(pst_timezone)
    formatted_time = current_time_pst.strftime('%H:%M:%S.%f')
    return formatted_time

def main():
    ser = serial.Serial(
        port='COM6',  # Set COM port (check device manager)
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )

    current_time_utc = datetime.now(pytz.utc)
    current_time_pst = current_time_utc.astimezone(pst_timezone)
    current_date_pst = current_time_pst.strftime('%Y-%m-%d')
    formatted_time = current_time_pst.strftime('%H-%M-%S')
    
    # ser.write(b'*IDN?\r')


    with open(f'Volt_Curr_{current_date_pst}_{formatted_time}.csv', mode='w', newline='') as csvfile:
        fieldnames = ['Time', 'Voltage', 'Current']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        startingTime = datetime.now()
        startingTimeSeconds = startingTime.hour * 60 * 60 + startingTime.minute * 60 + startingTime.second + startingTime.microsecond / 1000000
        endingTimeSeconds = startingTimeSeconds + 30
        count = 0
        while((datetime.now().hour * 60 * 60 + datetime.now().minute * 60 + datetime.now().second + datetime.now().microsecond / 1000000 )< endingTimeSeconds):
            value = ser.read(100).decode('ascii').strip()

            if value and ',' in value:

                values = value.split(',')
                voltageValue = values[0]
                currentValue = values[1]

                timestamp = update_time()

                print(f"COUNT: {count}, Time: {timestamp}, Voltage: {voltageValue}, Current: {currentValue}")
                # print(value)

                row_data = {"Time": timestamp, "Voltage": voltageValue, "Current": currentValue}
                writer.writerow(row_data)
                csvfile.flush()
            
                count += 1
            
        print(f"Count: {count} in 30 seconds\n")
        hz = count / 30
        print(hz)
        
    
if __name__ == '__main__':
    main()