from machine import Pin, I2C
from utime import sleep
from aht21 import AHT21
import os

# Constants
AHT = AHT21(I2C(1, scl=Pin(15), sda=Pin(14), freq=400000))
FILE = open("ex16.csv", "a")

# File Setup
FILE.write("Temp, Hum\n")

# Data Extract Function
def data_extract():
  while True:
    rht = AHT.read()
    hum, temp = rht
    FILE.write(f"{temp:.2f}, {hum:.2f}\n")
    sleep(1)

# Try-Except-Finally Block
try:
  print("Start AHT21 Sensor Measurement!")
  data_extract()

except KeyboardInterrupt:
  pass

finally:
  print("Terminate Process!")
  FILE.close()
