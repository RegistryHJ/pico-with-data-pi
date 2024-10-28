import uasyncio as asyncio
from utime import sleep

class ShowData:
  # Constructor
  def __init__(self, rtc, aht, ens, oled, team):
    self.rtc = rtc
    self.aht = aht
    self.ens = ens
    self.oled = oled
    self.team = team
    self.show_active = False

  # show_start Asynchronous Function
  async def show_start(self):
    self.show_active = True
    while self.show_active:
      self.time = self.rtc.get_rtc_time()
      self.humid, self.temp = self.aht.read()
      self.aqi, self.co2, self.tvoc = self.ens.AQI, self.ens.CO2, self.ens.TVOC

      self.oled.fill(0)
      self.oled.text(f"[{self.team}]", 0, 0)
      self.oled.text(f"Time: {self.time[4]}:{self.time[5]}:{self.time[6]}", 0, 9)
      self.oled.text(f"Temp: {self.temp:.2f} Deg", 0, 18)
      self.oled.text(f"Humid: {self.humid:.2f} %", 0, 27)
      self.oled.text(f"AQI: {self.aqi}", 0, 36)
      self.oled.text(f"CO2: {self.co2} ppm", 0, 45)
      self.oled.text(f"TVOC: {self.tvoc} ppb", 0, 54)
      self.oled.show()
      await asyncio.sleep(1)

  # show_stop Function
  def show_stop(self):
    self.show_active = False
    self.oled.fill(0)
    self.oled.show()
    sleep(0.5)
