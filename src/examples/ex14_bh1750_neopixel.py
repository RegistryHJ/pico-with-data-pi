from machine import Pin, I2C
from utime import sleep
from neopixel import NeoPixel
from bh1750 import BH1750

# Constants
NEOPIXEL = NeoPixel(Pin(21), 1)
BH = BH1750(0x23, I2C(0, scl=Pin(5), sda=Pin(4)))

# Valiables
lx = 0

# NeoPixel Light Level Function
def neopixel_lx(lx):
  for i in range(0, NEOPIXEL.n):
    NEOPIXEL[i] = (lx, lx, lx)
  NEOPIXEL.write()

# BH1750 Light Level Function
def bh1750_lx():
  global lx
  print(f"Light: {BH.measurement:.2f} lx")
  if BH.measurement < 125:
    lx = 255
  elif BH.measurement < 250:
    lx = 192
  elif BH.measurement < 375:
    lx = 128
  elif BH.measurement < 500:
    lx = 64
  else:
    lx = 0

# Main Loop
while True:
  bh1750_lx()
  neopixel_lx(lx)
  sleep(0.1)
