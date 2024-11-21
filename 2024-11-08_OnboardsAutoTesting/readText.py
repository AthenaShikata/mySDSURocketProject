def parseForDouble(value, toReplace, toCheck):
    newString = ""
    value = value.replace(toReplace, "")
    for char in value:
        if char.isdigit() or char == ".":
            newString += char
    newDouble = float(newString)
    if(toCheck == "mA"):
        last2 = value[len(value) - 2:]
        if(last2 == "mA" or last2 == "MA" or last2 == "ma"):
            newDouble = newDouble / 1000
    elif(toCheck == "min"):
        if("min" in value): #minutes
            newDouble = newDouble * 60
        elif("hr" or "hrs" in value): #hours
            newDouble = newDouble * 60 * 60
        elif("ms" in value): #milliseconds
            newDouble = newDouble / 1000
    return newDouble

def read (file_path):
    with open(file_path, 'r') as file: 
        content = file.read()

    inputs = [line for line in content.split('\n') if line.strip() != '']
    Ch1V, Ch1I, Ch2V, Ch2I, Time = "", "", "", "", ""
    Ch1VDouble, Ch1IDouble, Ch2VDouble, Ch2IDouble, TimeDouble = 0.0, 0.0, 0.0, 0.0, 0.0

    for value in inputs:
        try:
            if "Ch1V:" in value:
                Ch1VDouble = parseForDouble(value, "Ch1V:", "none")
            elif "Ch1I:" in value:
                Ch1IDouble = parseForDouble(value, "Ch1I:", "mA")
            elif "Ch2V:" in value:
                Ch2VDouble = parseForDouble(value, "Ch2V:", "none")
            elif "Ch2I:" in value:
                Ch2IDouble = parseForDouble(value, "Ch2I:", "mA")
            elif "Time:" in value:
                TimeDouble = parseForDouble(value, "Time:", "min")
            else:
                raise ValueError("Invalid input: " + value + " line: " + str(inputs.index(value) + 1))
                        
        except Exception as e:
            print(e)
            continue
                    
    return Ch1VDouble, Ch1IDouble, Ch2VDouble, Ch2IDouble, TimeDouble
    
#main
Ch1V, Ch1I, Ch2V, Ch2I, time = read("input.txt")
print("Ch1V: " + str(Ch1V))
print("Ch1I: " + str(Ch1I))
print("Ch2V: " + str(Ch2V))
print("Ch2I: " + str(Ch2I))
print("Time: " + str(time))