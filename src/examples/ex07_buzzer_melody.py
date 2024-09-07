from machine import Pin, PWM
from utime import sleep

# Constants
BUZZER = PWM(Pin(22))

# Melody Constants (Note, Duration)
C = (262, 0.5)
D = (294, 0.5)
E = (330, 0.5)
F = (349, 0.5)
G = (392, 0.5)
A = (440, 0.5)
B = (494, 0.5)
C2 = (523, 0.5)
MELODYS = [C, D, E, F, G, A, B, C2]


# Main Loop
for note, duration in MELODYS:
  # Buzzer Tone (Configure to the Note)
  BUZZER.freq(note)

  # Buzzer Duty Cycle 50% (Max 65535)
  BUZZER.duty_u16(30000)

  # Wait for the Duration
  sleep(duration)

  # Buzzer Duty Cycle Off
  BUZZER.duty_u16(0)

  # Delay
  sleep(0.1)
