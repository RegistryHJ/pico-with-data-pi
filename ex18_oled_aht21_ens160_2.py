from machine import Pin, I2C, SoftI2C
from utime import sleep
from aht21 import AHT21
from ens160 import ENS160
from ssd1306 import SSD1306_I2C

# Constants
AHT_1 = AHT21(I2C(1, scl=Pin(15), sda=Pin(14), freq=400000))
AHT_2 = AHT21(I2C(1, scl=Pin(19), sda=Pin(18), freq=400000))
ENS_1 = ENS160(I2C(1, scl=Pin(15), sda=Pin(14), freq=400000))
ENS_2 = ENS160(I2C(1, scl=Pin(19), sda=Pin(18), freq=400000))
OLED = SSD1306_I2C(128, 64, SoftI2C(scl=Pin(5), sda=Pin(4)))

# ENS160 Sensor Setup
ENS_1.reset()
ENS_2.reset()
sleep(0.5)
ENS_1.operating_mode = 2
ENS_2.operating_mode = 2
sleep(2)

# Start Message
OLED.text("Start Sensor Measurement!", 0, 0)
OLED.show()

# AHT_1 Sensor Function
def aht_1_Sensor():
  rht = AHT_1.read()
  humid, temp = rht
  OLED.text(f"Humid: {humid:.2f} %", 0, 0)
  OLED.text(f"Temp: {temp:.2f} Deg", 0, 10)

# AHT_2 Sensor Function
def aht_2_Sensor():
  rht = AHT_2.read()
  humid, temp = rht
  OLED.text(f"Humid: {humid:.2f} %", 0, 35)
  OLED.text(f"Temp: {temp:.2f} Deg", 0, 45)

# ENS_1 Sensor Function
def ens_1_Sensor():
  co2: int = ENS_1.CO2
  OLED.text(f"CO2: {str(co2):.2f} ppm", 0, 20)

# ENS_2 Sensor Function
def ens_2_Sensor():
  co2: int = ENS_2.CO2
  OLED.text(f"CO2: {str(co2):.2f} ppm", 0, 55)

# Main Loop
while True:
  OLED.fill(0)
  aht_1_Sensor()
  ens_1_Sensor()
  aht_2_Sensor()
  ens_2_Sensor()
  OLED.show()
  sleep(0.1)
