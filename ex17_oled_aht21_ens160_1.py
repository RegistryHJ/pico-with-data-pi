from machine import Pin, I2C, SoftI2C
from utime import sleep
from aht21 import AHT21
from ens160 import ENS160
from ssd1306 import SSD1306_I2C

# Constants
AHT = AHT21(I2C(1, scl=Pin(15), sda=Pin(14), freq=400000))
ENS = ENS160(I2C(1, scl=Pin(15), sda=Pin(14), freq=400000))
OLED = SSD1306_I2C(128, 64, SoftI2C(scl=Pin(5), sda=Pin(4)))

# ENS160 Sensor Setup
ENS.reset()
sleep(0.5)
ENS.operating_mode = 2
sleep(2)

# Start Message
OLED.text("Start Sensor Measurement!", 0, 0)
OLED.show()

# AHT Sensor Function
def AHT_Sensor():
  rht = AHT.read()
  humid, temp = rht
  OLED.text(f"Humid: {humid:.2f} %", 0, 0)
  OLED.text(f"Temp: {temp:.2f} Deg", 0, 10)

# ENS Sensor Function
def ENS_Sensor():
  co2: int = ENS.CO2
  OLED.text(f"CO2: {co2} ppm", 0, 20)

# Main Loop
while True:
  OLED.fill(0)
  AHT_Sensor()
  ENS_Sensor()
  OLED.show()
  sleep(0.1)
