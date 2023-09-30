import serial
print(serial.__doc__)
# Instanciating the serial.Serial class
ser: serial.Serial = serial.Serial(port='COM6', baudrate=9600)

while True:
    # ToDo: Add appropriate sleep time for optimization.
    values: bytes = ser.readlines()
    values_as_string: values.decode()
    print('Recived data: ', values_as_string)