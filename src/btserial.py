import lightblue

# Define the Bluetooth device's name (or address)
device_name = 'Your_Device_Name'  # Replace with your device's name or address

try:
    # Search for the Bluetooth device by name
    devices = lightblue.finddevices(device_name)

    if len(devices) == 0:
        raise Exception(f"Device '{device_name}' not found.")

    device = devices[0]  # Assume the first found device is the one we want

    # Connect to the Bluetooth device
    socket = lightblue.socket()
    socket.connect((device[0], 1))  # 1 is the Bluetooth RFCOMM channel (adjust if necessary)

    while True:
        data = socket.recv(1024).decode()
        if not data:
            break
        print("Received data:", data)

except Exception as e:
    print(f"Error: {str(e)}")

except KeyboardInterrupt:
    pass  # Allow Ctrl+C to exit the program gracefully

finally:
    socket.close()  # Close the Bluetooth socket when done
