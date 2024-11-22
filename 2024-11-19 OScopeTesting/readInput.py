def cleanInput(value, variable):
    value = value.lstrip().rstrip()

    #Checks for proper format and input from the input file and converts to oscope format
    if variable == 'mosi': # 1-4
        if value.isnumeric() == True and 0<int(value)<=4: value = f"CHANnel{value}"
        else: raise ValueError("Invalid input: " + value + " for MOSI variable. Must be integer between 1 and 4.")
    if variable == 'miso': # 1-4
        if value.isnumeric() == True and 0<int(value)<=4: value = f"CHANnel{value}"
        else: raise ValueError("Invalid input: " + value + " for MISO variable. Must be integer between 1 and 4.")
    if variable == 'clk': # 1-4
        if value.isnumeric() == True and 0<int(value)<=4: value = f"CHANnel{value}"
        else: raise ValueError("Invalid input: " + value + " for CLK variable. Must be integer between 1 and 4.")
    if variable == 'cs': # 1-4
        if value.isnumeric() == True and 0<int(value)<=4: value = f"CHANnel{value}"
        else: raise ValueError("Invalid input: " + value + " for CS variable. Must be integer between 1 and 4.")
    if variable == 'display': # ON/OFF
        if value.upper() == 'ON': value = 'ON'
        elif value.upper() == 'OFF': value = 'OFF'
        else: raise ValueError("Invalid input: " + value + " for Display variable. Must be ON or OFF.")
    if variable == 'mode': # PARallel/UART/SPI/IIC
        if value.upper() == 'PARALLEL': value = 'PARallel'
        elif value.upper() == 'UART': value = 'UART'
        elif value.upper() == 'SPI': value = 'SPI'
        elif value.upper() == 'IIC': value = 'IIC'
        else: raise ValueError("Invalid input: " + value + " for Mode variable. Must be PARallel, UART, SPI, or IIC.")
    if variable == 'select': # NCS/CS
        if value.upper() == 'NCS': value = 'NCS' 
        elif value.upper() == 'CS': value = 'CS'
        else: raise ValueError("Invalid input: " + value + " for Display variable. Must be NCS or CS.")
    if variable == 'edge': # RISE/FALL edge
        if value.upper() == 'RISE': value = 'RISE'
        elif value.upper() == 'FALL': value = 'FALL'
        else: raise ValueError("Invalid input: " + value + " for Edge variable. Must be RISE or FALL.")
    if variable == 'polarity': # POS/NEG
        if value.upper() == 'POS' or 'POSITIVE' or '+': value = 'POSitive'
        elif value.upper() == 'NEG' or 'NEGATIVE' or '-': value = 'NEGitive'
        else: raise ValueError("Invalid input: " + value + " for Polarity variable. Must be POSITIVE or NEGATIVE.")
    if variable == 'endian': # MSB/LSB
        if value.upper() == 'MSB': value = 'MSB'
        elif value.upper() == 'LSB': value = 'LSB'
        else: raise ValueError("Invalid input: " + value + " for Endian variable. Must be MSB or LSB.")
    if variable == 'format': # HEX/ASCii/DEC/BIN/LINE
        if value.upper() == 'HEX': value = 'HEX'
        elif value.upper() == 'ASCII': value = 'ASCii'
        elif value.upper() == 'DEC': value = 'DEC'
        elif value.upper() == 'BIN': value = 'BIN'
        elif value.upper() == 'LINE': value == 'LINE'
        else: raise ValueError("Invalid input: " + value + " for Format variable. Must be HEX, ASCii, DEC, BIN, or LINE.")
    if variable == 'width': # 8 to 32 Bit width
        if value.isnumeric() == True and 7<int(value)<33: value = f"{value}"
        else: raise ValueError("Invalid input: " + value + " for MOSI variable. Must be integer between 8 and 32.")

    ''' clean the variable off a number
        if value.endswith('mV') == True: value == str(float(value.rstrip('mV')) / 1000)
        elif value.endswith('V') == True: value == value.rstrip('V')
        elif value[-1].isnumeric() == True: pass
        else: raise ValueError("Invalid input: " + value + " for MOSI variable. Invalid units.")'''
    
    return value

def readInput(file_path):
    with open(file_path, 'r') as file: 
        content = file.read()

    inputs = [line for line in content.split('\n') if line.strip() != '']
    mosi, miso, clk, cs, display, mode, select, edge, polarity, endian, format, width = '', '', '', '', '', '', '', '', '', '', '', ''

    for value in inputs:
        try: 
            # Gets the setting we want in the oscope format
            if value.startswith('MOSI:'): mosi = cleanInput(value[5:],'mosi')
            elif value.startswith('MISO:'): miso = cleanInput(value[5:],'miso')
            elif value.startswith('CLK:'): clk = cleanInput(value[4:],'clk')
            elif value.startswith('CS:'): cs = cleanInput(value[3:],'cs')
            elif value.startswith('Display:'): display = cleanInput(value[8:],'display')
            elif value.startswith('Mode:'): mode = cleanInput(value[5:],'mode')
            elif value.startswith('Select:'): select = cleanInput(value[7:],'select')
            elif value.startswith('Edge:'): edge = cleanInput(value[5:],'edge')
            elif value.startswith('Polarity:'): polarity = cleanInput(value[9:],'polarity')
            elif value.startswith('Endian:'): endian = cleanInput(value[7:],'endian')
            elif value.startswith('Format:'): format = cleanInput(value[7:],'format')
            elif value.startswith('Width:'): width = cleanInput(value[6:],'width')
            else: raise ValueError("Invalid input: " + value + " line: " + str(inputs.index(value) + 1))
        except Exception as e:
            print(e)
            continue

    # Checks the input file to make sure that all the variables we need are detected
    if mosi == '': raise ValueError(f'Input File Error: MOSI variable not detected.')
    elif miso == '': raise ValueError(f'Input File Error: MISO variable not detected.')
    elif clk == '': raise ValueError(f'Input File Error: CLK variable not detected.')
    elif cs == '': raise ValueError(f'Input File Error: CS variable not detected.')
    elif display == '': raise ValueError(f'Input File Error: Display variable not detected.')
    elif mode == '': raise ValueError(f'Input File Error: Mode variable not detected.')
    elif select == '': raise ValueError(f'Input File Error: Select variable not detected.')
    elif edge == '': raise ValueError(f'Input File Error: Edge variable not detected.')
    elif polarity == '': raise ValueError(f'Input File Error: Polarity variable not detected.')
    elif endian == '': raise ValueError(f'Input File Error: Endian variable not detected.')
    elif format == '': raise ValueError(f'Input File Error: Format variable not detected.')
    elif width == '': raise ValueError(f'Input File Error: Width variable not detected.')
    else: print('All variables detected! :)')

    print('Setup Values Import Complete')
    
    return mosi, miso, clk, cs, display, mode, select, edge, polarity, endian, format, width