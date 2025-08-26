import serial

try:
    ser = serial.Serial(port='COM8', baudrate=9600, timeout=1)
except serial.SerialException as e:
    print(f"Error opening serial port: {e}")
    ser = None








def led(fingerUp):
    if fingerUp==[0,0,0,0,0]:
        ser.write(b'0')
    elif fingerUp==[0,1,0,0,0]:
        ser.write(b'1')
    elif fingerUp==[0,1,1,0,0]:
        ser.write(b'2')          
    elif fingerUp==[0,1,1,1,0]:
        ser.write(b'3')
    elif fingerUp==[0,1,1,1,1]:
        ser.write(b'4')
    elif fingerUp==[1,1,1,1,1]:
        ser.write(b'5')