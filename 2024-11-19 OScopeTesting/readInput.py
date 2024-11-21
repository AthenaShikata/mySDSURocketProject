def cleanInput(value, variable):
    newString = ""
    value = value.lstrip().rstrip()

    if variable == 'mosi': 
        if value.isnumeric() == True and 0<int(value)<=4: value = f"CHANnel{value}"
        else: raise ValueError("Invalid input: " + value + " for MOSI variable. Must be integer between 1 and 4.")
    if variable == 'miso': 
        if value.isnumeric() == True and 0<int(value)<=4: value = f"CHANnel{value}"
        else: raise ValueError("Invalid input: " + value + " for MISO variable. Must be integer between 1 and 4.")
    if variable == 'clk': 
        if value.isnumeric() == True and 0<int(value)<=4: value = f"CHANnel{value}"
        else: raise ValueError("Invalid input: " + value + " for CLK variable. Must be integer between 1 and 4.")
    if variable == 'cs': 
        if value.isnumeric() == True and 0<int(value)<=4: value = f"CHANnel{value}"
        else: raise ValueError("Invalid input: " + value + " for CS variable. Must be integer between 1 and 4.")
    if variable == 'display':
        if variable == 'on' or 'ON' or 'On' or 'oN': value = 'ON'
        if variable == 'off' or 'OFF' or 'Off' or 'oFF' or 'oFf' or 'OfF': value == 'OFF'
        else: raise ValueError("Invalid input: " + value + " for Display variable. Must be ON or OFF")
    if variable == 'select': pass
    if variable == 'edge': 
        if variable == 'rise' or 'RISE' or 'Rise': value = 'RISE'
        if variable == 'fall' or 'FALL' or 'Fall': value == 'FALL'
        else: raise ValueError("Invalid input: " + value + " for EDGE variable. Must be RISE or FALL")
    if variable == 'polarity': pass
    if variable == 'endian': pass
    if variable == 'format': pass
    if variable == 'width': 
        if value.isnumeric() == True and 8<=int(value)<=32: value = f"{value}"
        else: raise ValueError("Invalid input: " + value + " for MOSI variable. Must be integer between 8 and 32.")
    
    
    print(value)
    return value

def readInput(file_path):
    with open(file_path, 'r') as file: 
        content = file.read()

    inputs = [line for line in content.split('\n') if line.strip() != '']
    mosi, miso, clk, cs, display, select, edge, polarity, endian, format, width = '', '', '', '', '', '', '', '', '', '', ''

    for value in inputs:
        try: 
            if value.startswith('MOSI:'): mosi = cleanInput(value[5:],'mosi')
            if value.startswith('MISO:'): miso = cleanInput(value[5:]),'miso'
            if value.startswith('CLK:'): clk = cleanInput(value[4:],'clk')
            if value.startswith('CS:'): cs = cleanInput(value[3:],'cs')
            if value.startswith('Display:'): display = cleanInput(value[8:],'display')
            if value.startswith('Select:'): select = cleanInput(value[7:],'select')
            if value.startswith('Edge:'): edge = cleanInput(value[5:],'edge')
            if value.startswith('Polarity:'): polarity = cleanInput(value[9:],'polarity')
            if value.startswith('Endian:'): endian = cleanInput(value[7:],'endian')
            if value.startswith('Format:'): format = cleanInput(value[7:],'format')
            if value.startswith('Width:'): width = cleanInput(value[6:],'width')
            
            else:
                raise ValueError("Invalid input: " + value + " line: " + str(inputs.index(value) + 1))

        except Exception as e:
            print(e)
            continue

    if mosi or miso or clk or cs or display or select or edge or polarity or endian or format or width == '': raise ValueError(f'Input File Error: Not all values specified.')
    
    return mosi, miso, clk, cs, display, select, edge, polarity, endian, format, width

mosi, miso, clk, cs, display, select, edge, polarity, endian, format, width = readInput('input.txt')

print(mosi, miso, clk, cs, display, select, edge, polarity, endian, format, width)