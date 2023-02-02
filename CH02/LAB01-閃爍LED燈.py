# import Pin object from machine module
from machine import Pin

# import time module
import time

# 建立5號腳位的Pin物件，設定為腳位輸出，命名為led
# 此顆led燈的低腳位為5號腳位
led = Pin(5, Pin.OUT)

# Repeat light on and light off
while True:
    led.value(0) # 高電位，熄燈
    time.sleep(0.5)
    led.value(1) # 低電位，開燈
    time.sleep(0.5)