from machine import Pin
from utime import sleep

# Constants
LED = Pin('LED', Pin.OUT)
FAN = machine.Pin(10, machine.Pin.OUT)
BUTTON = Pin(20, Pin.IN, Pin.PULL_UP)

# variables
state = False
count = 0

# Button Handler function
def button_handler(pin):
  global state
  global count
  state = not state
  print(f"Fan State: {state}")
  FAN.value(state)
  LED.value(state)

  # If Fan is ON
  if state:
    count = 10

# Button IRQ
BUTTON.irq(trigger=Pin.IRQ_FALLING, handler=button_handler)

# Main Loop
while True:
  # If Button Pressed
  if state and count > 0:
    count -= 1
    print(f"Remaining Time: {count + 1}s")
    sleep(1)
    
    # If Count is 0
    if count < 1:
      state = False
      FAN.value(state)
      LED.value(state)
      print("Fan OFF!")  

  else:
    sleep(1)