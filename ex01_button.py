from machine import Pin
from utime import sleep

# Constants
LED = Pin('LED', Pin.OUT)
BUTTON = Pin(20, Pin.IN, Pin.PULL_UP)

# Main Loop
while True:
  if BUTTON.value() == 0:
    LED.value(True)
    print('Button Pressed!')
  elif BUTTON.value() == 1:
    LED.value(False)
    print('Button Released!')

  sleep(0.1)
