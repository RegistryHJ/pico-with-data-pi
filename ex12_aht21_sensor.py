from machine import Pin, I2C
from utime import sleep
from aht21 import AHT21

# Constants
AHT = AHT21(I2C(1, scl=Pin(15), sda=Pin(14), freq=400000))

# Start Message
print("Start AHT21 Sensor Measurement!")

# Main Loop
while True:
  rht = AHT.read()
  hum, temp = rht
  print(f"Temp: {temp:.2f} °C")
  print(f"Hum: {hum:.2f} %")
  sleep(1)
