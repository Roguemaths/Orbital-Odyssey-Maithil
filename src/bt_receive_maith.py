import bluetooth

hc05_address = "00:22:12:01:83:4C"

# Create a Bluetooth socket
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

try:
    # Connect to the HC-05 module
    sock.connect((hc05_address, 1))

    print("Connected to HC-05")

    while True:
        # Receive data from the HC-05 module
        data = sock.recv(1024)
        if not data:
            break

        # Decode and print the received data
        print("Received:", data.decode("utf-8"))

except bluetooth.BluetoothError as e:
    print(f"BluetoothError: {e}")

finally:
    # Close the Bluetooth socket
    sock.close()
