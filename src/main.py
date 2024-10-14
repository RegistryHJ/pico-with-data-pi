import os
import uasyncio as asyncio
from machine import Pin, I2C, PWM
from utime import sleep, localtime
from neopixel import NeoPixel
from ssd1306 import SSD1306_I2C
from aht21 import AHT21
from ens160 import ENS160
from wlan_config import WLANConfig
from soft_rtc import SoftRTC
from boot import Boot
from record import Record
from show_data import ShowData

# Constants
BUTTON = Pin(20, Pin.IN, Pin.PULL_UP)
BUZZER = PWM(Pin(22))
NEOPIXEL = NeoPixel(Pin(21), 1)
OLED = SSD1306_I2C(128, 64, I2C(0, scl=Pin(5), sda=Pin(4), freq=400000))
AHT = AHT21(I2C(1, scl=Pin(15), sda=Pin(14), freq=400000))
ENS = ENS160(I2C(1, scl=Pin(15), sda=Pin(14), freq=400000))

# Variables
ssid, password = "*", "*"
team_name = "TeamName"
record_active = False
record_interval = 1

# Instances
WLAN_0 = WLANConfig(ssid, password)
RTC = SoftRTC()
BOOT = Boot(NEOPIXEL, BUZZER, OLED)
SHOW = ShowData(RTC, AHT, ENS, OLED, team_name)
RECORD = Record(RTC, AHT, ENS)

# ENS160 Sensor Setup
ENS.reset()
sleep(2)
ENS.operating_mode = 2
sleep(2)

# active_oled Function
def active_oled():
  global record_active

  if record_active:
    OLED.fill(0)
    OLED.text("Started!", 0, 0)
    OLED.show()
  else:
    OLED.fill(0)
    OLED.text("Stopped!", 0, 0)
    OLED.show()

# active_buzzer Function
def active_buzzer():
  global record_active
  freqs = [1000, 2000]

  if record_active:
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

# active_neopixel Asynchronous Function
async def active_neopixel():
  global record_active
  is_incresed = True
  brightness = 0

  while True:
    if record_active:
      if is_incresed:
        brightness += 1
        if brightness >= 50:
          is_incresed = False
      else:
        brightness -= 1
        if brightness <= 0:
          is_incresed = True
    else:
      brightness = 0

    NEOPIXEL[0] = (0, brightness, 0)
    NEOPIXEL.write()

    await asyncio.sleep(0.025)

# active_show Asynchronous Function
async def active_show():
  global record_active
  while True:
    if record_active:
      await SHOW.show_start()
    await asyncio.sleep(1)

# active_record Asynchronous Function
async def active_record():
  global record_active
  while True:
    if record_active:
      await RECORD.record_start(record_interval)
    await asyncio.sleep(1)

# button_handler Function
def button_handler(pin):
  global record_active
  record_active = not record_active  # Toggle the state when the button is pressed

  # Stop the show and record when the button is pressed
  if not record_active:
    SHOW.show_stop()
    RECORD.record_stop()

  active_oled()  # Update OLED
  active_buzzer()  # Update Buzzer

# button_handler Function Binding to the BUTTON Pin
BUTTON.irq(trigger=Pin.IRQ_FALLING, handler=button_handler)

# main Asynchronous Function
async def main():
  WLAN_0.connect()
  RTC.set_rtc_time()
  now = RTC.get_rtc_time()
  print(f"RTC Time: {now[0]}-{now[1]}-{now[2]} {now[4]}:{now[5]}:{now[6]}")
  BOOT.boot()

  # Run the active_neopixel, active_show, and active_record functions concurrently
  await asyncio.gather(active_neopixel(), active_show(), active_record())

# Run the main function
asyncio.run(main())
