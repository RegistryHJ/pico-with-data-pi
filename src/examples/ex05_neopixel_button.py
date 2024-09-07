from machine import Pin
from utime import sleep
from neopixel import NeoPixel

# Constants
BUTTON = Pin(20, Pin.IN, Pin.PULL_UP)
NEOPIXEL = NeoPixel(machine.Pin(21), 1)

# Color Constants
R = (50, 0, 0)
G = (0, 50, 0)
B = (0, 0, 50)
C = (0, 50, 50)
M = (50, 0, 50)
Y = (50, 50, 0)
W = (50, 50, 50)
COLORS = [R, G, B, C, M, Y, W]

# Variables
color_idx = 0

# NeoPixel Color Function
def neopixel_color(idx):
  for i in range(0, NEOPIXEL.n):
    NEOPIXEL[i] = COLORS[idx]
  NEOPIXEL.write()

# Button Handler Function
def button_handler(pin):
  global color_idx
  color_idx = (color_idx + 1) % len(COLORS)
  neopixel_color(color_idx)

# Button IRQ
BUTTON.irq(trigger=Pin.IRQ_FALLING, handler=button_handler)

# Main Loop
while True:
  sleep(0.1)
