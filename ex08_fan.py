from machine import Pin
from utime import sleep

# Constants
FAN = Pin(10, Pin.OUT)

# Main Loop
while True:
  FAN.on()
  sleep(1)
