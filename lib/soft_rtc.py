from machine import RTC
from utime import sleep, gmtime
from usocket import getaddrinfo, socket, AF_INET, SOCK_DGRAM
from ustruct import unpack

class SoftRTC:
  # Constructor
  def __init__(self):
    self.rtc = RTC()
    self.ntp_host = "pool.ntp.org"
    self.kst_offset = 3600 * 9

  # get_time_from_ntp Function
  def get_time_from_ntp(self):
    ntp_delta = 2208988800
    ntp_query = bytearray(48)
    ntp_query[0] = 0x1B
    address = getaddrinfo(self.ntp_host, 123)[0][-1]
    socket_0 = socket(AF_INET, SOCK_DGRAM)

    try:
      socket_0.settimeout(10)
      response = socket_0.sendto(ntp_query, address)
      message = socket_0.recv(48)

    finally:
      socket_0.close()

    ntp_time = unpack("!I", message[40:44])[0]
    kst_time = gmtime(ntp_time - ntp_delta + self.kst_offset)

    return kst_time

  # set_rtc_time Function
  def set_rtc_time(self):
    time = self.get_time_from_ntp()
    self.rtc.datetime((time[0], time[1], time[2], time[6], time[3], time[4], time[5], 0))

  # get_rtc_time Function
  def get_rtc_time(self):
    return self.rtc.datetime()
