from machine import Pin
from utime import sleep

# Constants
LED = Pin('LED', Pin.OUT)
BUTTON = Pin(20, Pin.IN, Pin.PULL_UP)

# Variables
state = False

# Button Handler Function
def button_handler(pin):
  global state
  state = not state
  print(f"Button Pressed: {state}")
  LED.value(state)

# Button IRQ
BUTTON.irq(trigger=Pin.IRQ_FALLING, handler=button_handler)

# Main Loop
while True:
  sleep(0.1)
