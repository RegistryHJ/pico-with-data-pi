from machine import Pin, PWM
from neopixel import NeoPixel
from utime import sleep

# Constants
BUTTON = Pin(20, Pin.IN, Pin.PULL_UP)
BUZZER = PWM(Pin(22))
FAN = Pin(10, Pin.OUT)
NEOPIXEL_0 = NeoPixel(Pin(21), 1)
NEOPIXEL_1 = NeoPixel(Pin(6), 30)
NEOPIXEL_2 = NeoPixel(Pin(7), 30)

# Variables
is_active = False
neopixel_color_0 = (0, 50, 0)      # DataPi NeoPixel Color
neopixel_color_1 = (255, 255, 255)  # Customizable (NeoPixel Strip 1 Color; Default: White)
neopixel_color_2 = (255, 255, 255)  # Customizable (NeoPixel Strip 2 Color; Default: White)
neopixel_color_off = (0, 0, 0)     # NeoPixel Off Color

# Define Active DataPi NeoPixel Function
def active_neopixel_0():
  global is_active
  if is_active == True:
    for i in range(0, NEOPIXEL_0.n):
      NEOPIXEL_0[i] = neopixel_color_0
    NEOPIXEL_0.write()
  else:
    for i in range(0, NEOPIXEL_0.n):
      NEOPIXEL_0[i] = neopixel_color_off
    NEOPIXEL_0.write()

# Define Active NeoPixel Strip 1 Function
def active_neopixel_1():
  global is_active
  if is_active == True:
    for i in range(0, NEOPIXEL_1.n):
      NEOPIXEL_1[i] = neopixel_color_1
    NEOPIXEL_1.write()
  else:
    for i in range(0, NEOPIXEL_1.n):
      NEOPIXEL_1[i] = neopixel_color_off
    NEOPIXEL_1.write()

# Define Active NeoPixel Strip 2 Function
def active_neopixel_2():
  global is_active
  if is_active == True:
    for i in range(0, NEOPIXEL_2.n):
      NEOPIXEL_2[i] = neopixel_color_2
    NEOPIXEL_2.write()
  else:
    for i in range(0, NEOPIXEL_2.n):
      NEOPIXEL_2[i] = neopixel_color_off
    NEOPIXEL_2.write()

# Define Active Fan Function
def active_fan():
  global is_active
  FAN.value(is_active)

# Define Active Buzzer Function
def active_buzzer():
  global is_active
  freqs = [1000, 2000]

  if is_active:
    for freq in freqs:
      BUZZER.freq(freq)
      BUZZER.duty_u16(30000)
      sleep(0.1)
    BUZZER.duty_u16(0)
  else:
    for freq in reversed(freqs):
      BUZZER.freq(freq)
      BUZZER.duty_u16(30000)
      sleep(0.1)
    BUZZER.duty_u16(0)

# Define Button Handler Function
def button_handler(pin):
  global is_active
  is_active = not is_active
  active_neopixel_0()
  active_neopixel_1()
  active_neopixel_2()
  active_fan()
  active_buzzer()

# Register Button Handler
BUTTON.irq(trigger=Pin.IRQ_FALLING, handler=button_handler)

# Define Boot Neopixel Function
def boot_neopixel():
  colors = [(50, 0, 0), (0, 50, 0), (0, 0, 50), (0, 0, 0)]
  for color in colors:
    for i in range(0, NEOPIXEL_0.n):
      NEOPIXEL_0[i] = color
    NEOPIXEL_0.write()
    sleep(0.25)

# Define Boot Buzzer Function
def boot_buzzer():
  freqs = [1000, 2000, 3000]
  for freq in freqs:
    BUZZER.freq(freq)
    BUZZER.duty_u16(30000)
    sleep(0.1)
  BUZZER.duty_u16(0)

# Define Main Function
def main():
  boot_neopixel()
  boot_buzzer()
  while True:
    sleep(1)

# Run Main Function
if __name__ == "__main__":
  main()
