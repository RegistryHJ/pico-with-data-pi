from machine import Pin, I2C, RTC
from utime import sleep, gmtime, localtime
from usocket import getaddrinfo, socket, AF_INET, SOCK_DGRAM
from ustruct import unpack
from network import WLAN, STA_IF
from wlan_config import WLANConfig
from ds3231 import DS3231

# Constants
SSID, PASSWORD = WLANConfig.get_wlan_kcce()
WLAN_0 = WLAN(STA_IF)
RTC = RTC()
DS = DS3231(I2C(0, scl=Pin(5), sda=Pin(4)))
KST_OFFSET = 3600 * 9
NTP_HOST = "pool.ntp.org"
IP_ADDRESS = ""

# WLAN Connection
WLAN_0.active(True)
WLAN_0.connect(SSID, PASSWORD)

# Get Time from NTP Function
def get_time_from_ntp():
  NTP_DELTA = 2208988800
  NTP_QUERY = bytearray(48)
  NTP_QUERY[0] = 0x1B
  ADDRESS = getaddrinfo(NTP_HOST, 123)[0][-1]
  SOCKET = socket(AF_INET, SOCK_DGRAM)

  try:
    SOCKET.settimeout(1)
    response = SOCKET.sendto(NTP_QUERY, ADDRESS)
    message = SOCKET.recv(48)

  finally:
    SOCKET.close()

  ntp_time = unpack("!I", message[40:44])[0]

  return gmtime(ntp_time - NTP_DELTA + KST_OFFSET)

# Set RTC Time Function
def set_rtc_time():
  time = get_time_from_ntp()
  RTC.datetime((time[0], time[1], time[2], time[6], time[3], time[4], time[5], 0))

# WLAN Connection Function
def wlan_connection():
  max_retry = 10
  while max_retry > 0:
    if WLAN_0.status() < 0 or WLAN_0.status() >= 3:
      break
    max_retry -= 1
    sleep(1)
  status = None
  if WLAN_0.status() != 3:
    raise RuntimeError("WLAN Connection Failed")
  else:
    status = WLAN_0.ifconfig()
    print(f"WLAN Connected! SSID: {SSID}, IP: {status[0]}")

  IP_ADDRESS = status[0]

# Main Function
def main():
  # Invoke WLAN Connection
  wlan_connection()
  print()

  # Invoke Set RTC Time
  set_rtc_time()
  print(RTC.datetime())
  print()

  # Init Time Test
  print("Init Time")
  print(f"DS3231 Time: {DS.get_time()}")
  print(f"RTC Time: {RTC.datetime()}")
  print()

  # Sync Time Test
  print("Sync Time")
  DS.save_time()
  print(f"DS3231 Time: {DS.get_time()}")
  print(f"RTC Time: {RTC.datetime()}")
  print()

  # Time Difference Test
  print("Time Difference")
  print(DS.rtc_test(120, True), 'ppm')
  print()

# Run Main Function
if __name__ == "__main__":
  main()
