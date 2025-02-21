import pyvisa
import time

def runSetup(mosi, miso, clk, cs, display, mode, select, edge, polarity, endian, format, width):
    rm = pyvisa.ResourceManager()
    print("Resources detected\n{}\n".format(rm.list_resources()))

    Oscope = rm.open_resource('USB0::0x1AB1::0x04CE::DS1ZA203013017::INSTR') # Put your device IDs here
    Oscope.timeout = 3000
    Oscope.read_termination = '\n'
    Oscope.write_termination = '\n'

    time.sleep(0.04)
    print("Performing Configuration...")


    # print("Setup Configuration Complete")

    Oscope.write(':DECoder1:MODE SPI')   

    Oscope.write(f':DECoder1:SPI:CLK {clk}') # 1-4
    Oscope.write(f':DECoder1:SPI:MISO {miso}') # 1-4
    Oscope.write(f':DECoder1:SPI:MOSI {mosi}') # 1-4
    Oscope.write(f':DECoder1:SPI:CS {cs}') # 1-4
    Oscope.write(f':DECoder1:SPI:MODE {mode}') # PARallel/UART/SPI/IIC
    Oscope.write(f':DECoder1:SPI:SELect {select}') # NCS/CS CS pin pulled low (NCS) or pulled high (CS) when decoding
    Oscope.write(f':DECoder1:SPI:EDGE {edge}') # RISE/FALL edge
    Oscope.write(f':DECoder1:SPI:POLarity {polarity}') # POS/NEG for polarity
    Oscope.write(f':DECoder1:SPI:ENDian {endian}') # MSB/LSB
    Oscope.write(f':DECoder1:FORMat {format}') # HEX/ASCii/DEC/BIN/LINE
    Oscope.write(f':DECoder1:SPI:WIDTh {width}') # 8 to 32 Bit width
    Oscope.write(f':DECoder1:DISPlay {display}') # ON/OFF decoder

    print("Decoder Setup Configuration Complete")


    Oscope.close()


    # Oscope.write('')
    # :CHANnel1:PROBe 1