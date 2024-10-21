# RaspberryPi Pico with DataPi

The project aims to install RaspberryPi Pico in DataPi and directly code and learn by connecting embedded sensors, external sensors, and equipment.

### Configure Project

`Conda` is assumed to be installed.

**First.** Clone this repository:

```bash
git clone https://github.com/RegistryHJ/pico-with-data-pi.git
```

**Second.** Create Conda new environment (e.g `pico`)

```bash
conda create -n pico python=3.10
```

**Third.** Activate environment and Install Dependencies

```bash
conda activate pico
pip install -r requirements.txt
```

Configure is Done.

### Examples

<table>
  <thead>
    <tr>
      <th>File</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="./src/examples/ex01_button.py">ex01_button.py</a></td>
      <td>Implement Button.</td>
    </tr>
    <tr>
      <td><a href="./src/examples/ex02_button_toggle.py">ex02_button_toggle.py</a></td>
      <td>Implement Toggle button with state.</td>
    </tr>
    <tr>
      <td><a href="./src/examples/ex03_button_toggle_irq.py">ex03_button_toggle_irq.py</a></td>
      <td>Implement Toggle button with button handler bind.</td>
    </tr>
    <tr>
      <td><a href="./src/examples/ex04_neopixel.py">ex04_neopixel.py</a></td>
      <td>Implement NeoPixel on/off, colors</td>
    </tr>
    <tr>
      <td><a href="./src/examples/ex05_neopixel_button.py">ex05_neopixel_button.py</a></td>
      <td>Implement NeoPixel color change when button pressed</td>
    </tr>
    <tr>
      <td><a href="./src/examples/ex06_buzzer.py">ex06_buzzer.py</a></td>
      <td>Implement Buzzer sound with PWM</td>
    </tr>
    <tr>
      <td><a href="./src/examples/ex07_buzzer_melody.py">ex07_buzzer_melody.py</a></td>
      <td>Implement Buzzer melody with notes</td>
    </tr>
    <tr>
      <td><a href="./src/examples/ex08_fan.py">ex08_fan.py</a></td>
      <td>Implement 12V Fan on</td>
    </tr>
    <tr>
      <td><a href="./src/examples/ex09_fan_button.py">ex09_fan_button.py</a></td>
      <td>Implement 12V Fan on/off when button pressed</td>
    </tr>
    <tr>
      <td><a href="./src/examples/ex10_fan_button_count.py">ex10_fan_button_count.py</a></td>
      <td>Implement 12V Fan on/delay-off when button pressed</td>
    </tr>
    <tr>
      <td><a href="./src/examples/ex11_bh1750_sensor.py">ex11_bh1750_sensor.py</a></td>
      <td>Implement Illuminance sensor</td>
    </tr>
    <tr>
      <td><a href="./src/examples/ex12_aht21_sensor.py">ex12_aht21_sensor.py</a></td>
      <td>Implement AHT sensor</td>
    </tr>
    <tr>
      <td><a href="./src/examples/ex13_ens160_sensor.py">ex13_ens160_sensor.py</a></td>
      <td>Implement Gas Sensor</td>
    </tr>
    <tr>
      <td><a href="./src/examples/ex14_bh1750_neopixel.py">ex14_bh1750_neopixel.py</a></td>
      <td>Implement NeoPixel Illumination with Illuminance sensor</td>
    </tr>
    <tr>
      <td><a href="./src/examples/ex15_oled.py">ex15_oled.py</a></td>
      <td>Implement OLED display show</td>
    </tr>
    <tr>
      <td><a href="./src/examples/ex16_data_extract_aht21.py">ex16_data_extract_aht21.py</a></td>
      <td>Implement Data extract with AHT Sensor</td>
    </tr>
    <tr>
      <td><a href="./src/examples/ex17_oled_aht21_ens160_1.py">ex17_oled_aht21_ens160_1.py</a></td>
      <td>Implement OLED display show with 1 AHT Sensor and Gas Sensor</td>
    </tr>
    <tr>
      <td><a href="./src/examples/ex18_oled_aht21_ens160_2.py">ex18_oled_aht21_ens160_2.py</a></td>
      <td>Implement OLED display show with 2 AHT Sensor and Gas Sensor</td>
    </tr>
    <tr>
      <td><a href="./src/examples/ex19_rtc_sync.py">ex19_rtc_sync.py</a></td>
      <td>Implement Sync RTC time with NTP server</td>
    </tr>
    <tr>
      <td><a href="./src/examples/ex20_data_extract_rtc_aht21.py">ex20_data_extract_rtc_aht21.py</a></td>
      <td>Implement Data extract with AHT Sensor and RTC time</td>
    </tr>
    <tr>
      <td><a href="./src/examples/ex21_colab_with_python.ipynb">ex21_colab_with_python.ipynb</a></td>
      <td>Implement Python syntax in colab</td>
    </tr>
    <tr>
      <td><a href="./src/examples/ex22_matplotlib.ipynb">ex22_matplotlib.ipynb</a></td>
      <td>Implement Matplotlib visualization in colab</td>
    </tr>
    <tr>
      <td><a href="./src/examples/ex23_matplotlib_aht21.ipynb">ex23_matplotlib_aht21.ipynb</a></td>
      <td>Implement Matplotlib visualization with extracted AHT sensor data in colab</td>
    </tr>
    <tr>
      <td><a href="./src/examples/ex24_data_analysis.ipynb">ex24_data_analysis.ipynb</a></td>
      <td>Implement Data analysis with data.csv extracted by running 1.0.0-release in colab</td>
    </tr>
  </tbody>
</table>
