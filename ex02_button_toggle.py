from machine import Pin
from utime import sleep

# Constants
LED = Pin('LED', Pin.OUT)
BUTTON = Pin(20, Pin.IN, Pin.PULL_UP)

# Variables
state = False

# Main Loop
while True:
  if BUTTON.value() == 0:
    state = not state
    print(f"Button Pressed: {state}")
    sleep(0.1)

  LED.value(state)
  sleep(0.1)
