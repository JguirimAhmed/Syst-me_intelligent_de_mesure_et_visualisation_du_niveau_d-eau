from machine import Pin
import time
relay = Pin(12,Pin.OUT)
trig = Pin(32,Pin.OUT)
echo = Pin(33,Pin.IN)
Ton = Toff = t = distance = 0
while 1 :
    trig.on()
    time.sleep_us(5)
    trig.off()
    time.sleep_us(2)
    while echo.value() == 0 :
    Toff = time.ticks_us()
    while echo.value() == 1 :
    Ton = time.ticks_us()
    t = Ton - Toff
    distance = (t * 0.0343 ) / 2
    print(distance)
    time.sleep_ms(20)