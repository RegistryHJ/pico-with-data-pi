from machine import Pin, I2C
from utime import sleep
from ens160 import ENS160

# Constants
ENS = ENS160(I2C(1, scl=Pin(15), sda=Pin(14), freq=400000))

# ENS160 Sensor Setup
ENS.reset()
sleep(0.5)
ENS.operating_mode = 2
sleep(2)

# Start Message
print("Start ENS160 Sensor Measurement!")

# Main Loop
while True:
  aqi = ENS.AQI()  # Air Quality Index (1: Excellent, 2: Good, 3: Moderate, 4: Poor, 5: Unhealthy)
  co2 = ENS.CO2()  # CO2
  tvoc = ENS.TVOC()  # TVOC

  print(f"Air Quality Index: {aqi}")
  print(f"CO2: {co2:.2f} ppm")
  print(f"TVOC: {tvoc:.2f} ppb")

  sleep(1)
