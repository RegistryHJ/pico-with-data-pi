from machine import Pin
from utime import sleep

# Constants
LED = Pin('LED', Pin.OUT)
FAN = machine.Pin(10, machine.Pin.OUT)
BUTTON = Pin(20, Pin.IN, Pin.PULL_UP)

# variables
state = False

# Button Handler function
def button_handler(pin):
  global state
  state = not state
  print(f"Fan ON: {state}")
  LED.value(state)
  FAN.value(state)

# Button IRQ
BUTTON.irq(trigger=Pin.IRQ_FALLING, handler=button_handler)

# Main Loop
while True:
  sleep(1)
