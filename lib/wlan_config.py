from utime import sleep
from network import WLAN, STA_IF

class WLANConfig:
  # Constructor
  def __init__(self, ssid, password):
    self.ssid, self.password = ssid, password
    self.wlan_0 = WLAN(STA_IF)
    self.wlan_0.active(True)
    self.wlan_0.connect(self.ssid, self.password)

  # connect Function
  def connect(self):
    self.connect_status = False
    connection_count = 0

    while True:
      if self.wlan_0.status() != 3:
        connection_count = connection_count + 1
        print(f"Connection Count: {connection_count}")
      else:
        self.connect_status = True
        self.ip_address = self.wlan_0.ifconfig()[0]
        print(f"WLAN Connected! SSID: {self.ssid}, IP: {self.ip_address}")
        break
      sleep(1)
