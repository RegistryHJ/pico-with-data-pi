import os
import uasyncio as asyncio
from utime import sleep

class Record:
  # Constructor
  def __init__(self, rtc, aht, ens):
    self.rtc = rtc
    self.aht = aht
    self.ens = ens
    self.file = None
    self.record_active = False

  # record_start Asynchronous Function
  async def record_start(self, interval):
    self.record_active = True
    self.file = open("data.csv", "a")
    print("Recording started!")
    print("Recording...")

    try:
      while self.record_active:
        now = self.rtc.get_rtc_time()
        humid, temp = self.aht.read()
        aqi, co2, tvoc = self.ens.AQI, self.ens.CO2, self.ens.TVOC
        self.file.write(f"{now[0]}-{now[1]}-{now[2]} {now[4]}:{now[5]}:{now[6]}, {temp:.2f}, {humid:.2f}, {aqi}, {co2}, {tvoc}\n")
        self.file.flush()
        await asyncio.sleep(interval)
    except Exception as e:
      print(e)

  # record_stop Function
  def record_stop(self):
    self.record_active = False
    self.file.close() if self.file else None
    print("Recording stopped!")
    print("File Saved!")
