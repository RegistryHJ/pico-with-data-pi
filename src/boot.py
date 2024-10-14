from utime import sleep

class Boot:
  # Constructor
  def __init__(self, neopixel, buzzer, oled):
    self.colors = [(50, 0, 0), (0, 50, 0), (0, 0, 50), (0, 0, 0)]
    self.freqs = [1000, 2000, 3000]
    self.neopixel = neopixel
    self.buzzer = buzzer
    self.oled = oled

  # boot_start_message Function
  def boot_start_message(self):
    print("Booting...")
    self.oled.fill(0)
    self.oled.text("Booting...", 0, 0)
    self.oled.show()

  # boot_end_message Function
  def boot_end_message(self):
    print("Boot Complete!")
    self.oled.fill(0)
    self.oled.text("Boot Complete!", 0, 0)
    self.oled.show()

  # boot_neopixel Function
  def boot_neopixel(self):
    for color in self.colors:
      self.neopixel[0] = color
      self.neopixel.write()
      sleep(0.25)

  # boot_buzzer Function
  def boot_buzzer(self):
    for freq in self.freqs:
      self.buzzer.freq(freq)
      self.buzzer.duty_u16(30000)
      sleep(0.1)
    self.buzzer.duty_u16(0)

  # boot Function
  def boot(self):
    self.boot_start_message()
    self.boot_neopixel()
    self.boot_buzzer()
    self.boot_end_message()
