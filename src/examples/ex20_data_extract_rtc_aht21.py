from machine import Pin, I2C
from utime import sleep
from aht21 import AHT21
from ds3231 import DS3231
from ssd1306 import SSD1306_I2C
import os

# Constants
AHT = AHT21(I2C(1, scl=Pin(15), sda=Pin(14), freq=400000))
DS = DS3231(I2C(0, scl=Pin(5), sda=Pin(4), freq=400000))
OLED = SSD1306_I2C(128, 64, I2C(0, scl=Pin(5), sda=Pin(4), freq=400000))
FILE = open("ex20.csv", "a")

# Data Extract Function
def data_extract():
  while True:
    rht = AHT.read()
    hum, temp = rht
    time = DS.get_time()
    OLED.fill(0)
    OLED.text(f"Date: {time[0]}-{time[1]}-{time[2]}", 0, 0)
    OLED.text(f"Time: {time[3]}:{time[4]}:{time[5]}", 0, 10)
    OLED.text(f"Temp: {temp:.2f} Deg", 0, 20)
    OLED.text(f"Hum: {hum:.2f} %", 0, 30)
    OLED.show()
    FILE.write(f"{time[0]}-{time[1]}-{time[2]} {time[3]}:{time[4]}:{time[5]}, {temp:.2f}, {hum:.2f}\n")
    sleep(60)

# Try-Except-Finally Block
try:
  print("Start Sensor Measurement!")
  data_extract()
except KeyboardInterrupt:
  pass
finally:
  print("Terminate Process!")
  FILE.close()
