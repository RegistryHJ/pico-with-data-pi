from machine import Pin, I2C
from utime import sleep
from bh1750 import BH1750

# Constants
BH = BH1750(0x23, I2C(0, scl=Pin(5), sda=Pin(4)))

# Start Message
print("Start BH1750 Sensor Measurement!")

# Main Loop
while True:
  print(f"{BH.measurement:.2f} lx")
  sleep(1)
