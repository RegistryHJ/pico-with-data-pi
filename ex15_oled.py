from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C

# Constants
OLED = SSD1306_I2C(128, 64, SoftI2C(scl=Pin(5), sda=Pin(4)))

# Define Text and Position on OLED (Text, X, Y)
OLED.text('Hello, World 1!', 0, 0)
OLED.text('Hello, World 2!', 0, 10)
OLED.text('Hello, World 3!', 0, 20)

# Show OLED
oled.show()
