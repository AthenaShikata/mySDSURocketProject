from readInput import *
from setup import *

def main():

    # Get values from the input file
    mosi, miso, clk, cs, display, mode, select, edge, polarity, endian, format, width = readInput('input.txt')
    
    # Set values on the Oscope
    runSetup(mosi, miso, clk, cs, display, mode, select, edge, polarity, endian, format, width)


if __name__ == '__main__':
    main()