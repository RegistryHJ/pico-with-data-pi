from machine import Pin
from utime import sleep
from neopixel import NeoPixel

# Constants
NEOPIXEL = NeoPixel(machine.Pin(21), 1)

# NeoPixel On Function
def neopixel_on():
  for i in range(0, NEOPIXEL.n):
    NEOPIXEL[i] = (255, 255, 255)
  NEOPIXEL.write()

# NeoPixel Off Function
def neopixel_off():
  for i in range(0, NEOPIXEL.n):
    NEOPIXEL[i] = (0, 0, 0)
  NEOPIXEL.write()

# Main Loop
while True:
  neopixel_on()
  sleep(1)
  neopixel_off()
  sleep(1)
