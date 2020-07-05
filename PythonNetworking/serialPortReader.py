import serial


# reads from a serial port and prints the input

ser = serial.Serial(port='COM5', baudrate=115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, timeout=2)

try:
    ser.isOpen()
    print("Serial port is open")
except:
    print("Error")
    exit()

if(ser.isOpen()):
    try:
        while(1):
            print(ser.read())
    except Exception:
        print("error")
else:
    print("Cannot open serial port")
        
        
