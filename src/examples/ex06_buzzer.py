from machine import Pin, PWM
from utime import sleep

# Constants
BUZZER = PWM(Pin(22))

# Main Loop
while True:
  # Buzzer Tone
  BUZZER.freq(500)

  # Buzzer Duty Cycle 1.5% (Max 65535)
  BUZZER.duty_u16(1000)

  # Wait 1 second (Buzzer makes a Sound for 1sec)
  sleep(1)

  # Buzzer Duty Cycle Off
  BUZZER.duty_u16(0)
