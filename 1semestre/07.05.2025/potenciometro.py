from machine import ADC, Pin, PWM # type: ignore
from time import sleep

led = PWM(Pin(5), freq=20000, duty=0)
pot = ADC(Pin(34))
pot.atten(ADC.ATTN_11DB)
try:
    while True:
        led.duty(int(pot.read() / 4))
        sleep(0.1)
except KeyboardInterrupt:
    led.duty(0)