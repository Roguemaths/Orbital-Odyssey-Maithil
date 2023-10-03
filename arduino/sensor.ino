#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BMP280.h>
#include <SoftwareSerial.h>

SoftwareSerial BTSerial(0, 1); // RX, TX

Adafruit_BMP280 bmp;

void setup() {
  Serial.begin(9600);
  BTSerial.begin(9600);
  if (!bmp.begin(0x76)) {
    Serial.println("Could not find a valid BMP280 sensor, check wiring!");
    while (1);
  }
}

void loop() {
  float temperature = bmp.readTemperature();
  float pressure = bmp.readPressure() / 100.0F; // in hPa
  float altitude = bmp.readAltitude(1013.25); // sea-level pressure in hPa
  int ldrValue = analogRead(A0);

  Serial.print("Temperature: ");
  Serial.println(temperature);
  Serial.print("Pressure: ");
  Serial.println(pressure);
  Serial.print("Altitude: ");
  Serial.println(altitude);
  Serial.print("Light Intensity: ");
  Serial.println(ldrValue);

  // Send data over Bluetooth
  BTSerial.print("T:");
  BTSerial.println(temperature);
  BTSerial.print("P:");
  BTSerial.println(pressure);
  BTSerial.print("A:");
  BTSerial.println(altitude);
  BTSerial.print("L:");
  BTSerial.println(ldrValue);

  delay(1000);
}



