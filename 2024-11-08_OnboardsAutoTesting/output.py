import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd
def findOutput(inputCSV):
    with open(inputCSV, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader) #skip header
        data = list(reader)
        data_array = np.array(data, dtype=float)

        df = pd.read_csv(inputCSV)
        df["Power"] = df.iloc[:, 1] * df.iloc[:, 2]
        df.to_csv(inputCSV, index=False)


    with open(inputCSV, newline='') as csvfile:
        
        reader = csv.reader(csvfile)
        next(reader) #skip header
        data = list(reader)
        data_array = np.array(data, dtype=float)
        
        #calculate average power and peak power
        totalAmpUsage = 0 #note: this is the area under the curve (unlike the following three variables that are used for averages)
        totalPower = 0
        totalVoltage = 0
        totalCurrent = 0
        peakPower = data_array[0][3]
        for index, row in enumerate(data_array):
            #compare power to peak power
            totalVoltage += row[1]
            totalCurrent += row[2]
            totalPower += row[3]
            if row[3] > peakPower:
                peakPower = row[3]
                
            #find total power consumption
            if index == 0:
                continue
            else: 
                totalHeight = data_array[index][2] + data_array[index - 1][2] # length1 + length2
                deltaTime = data_array[index][0] - data_array[index - 1][0] #time2 - time1
                riemannSum = totalHeight * deltaTime / 2 #area of trapezoid
                totalAmpUsage += riemannSum
        #get averages
        averageVoltage = totalVoltage / len(data_array)
        averageCurrent = totalCurrent / len(data_array)
        averagePower = totalPower / len(data_array)
        
        #convert totalAmpUsage to mAH
        totalTime = data_array[-1][0] - data_array[0][0] #final time - initial time
        totalmAHs = totalAmpUsage * 1000 / (60 * 60 * 1000) #Amps to mAH, milliseconds to hours
        print("Average Voltage: " + str(averageVoltage))
        print("Average Current: " + str(averageCurrent))
        print("Average Power: " + str(averagePower))
        print("Peak Power: " + str(peakPower))
        print("mAh Consumption " + str(totalmAHs))
        
        
        figure, axis = plt.subplots(1, 3)
        axis[0].plot(data_array[:,0], data_array[:,1])
        axis[0].set_title("Voltage vs Time")
        axis[0].set_xlabel("Time")
        axis[0].set_ylabel("Voltage")
        
        axis[1].plot(data_array[:,0], data_array[:,2])
        axis[1].set_title("Current vs Time")
        axis[1].set_xlabel("Time")
        axis[1].set_ylabel("Current")
        
        axis[2].plot(data_array[:,0], data_array[:,3])
        axis[2].set_title("Power vs Time")
        axis[2].set_xlabel("Time")
        axis[2].set_ylabel("Power")
        
        
        plt.show()
        
#example main
#findOutput('output.csv')