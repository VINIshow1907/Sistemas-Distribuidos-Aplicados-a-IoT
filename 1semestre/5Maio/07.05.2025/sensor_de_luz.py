from machine import ADC, Pin # type: ignore
from utime import sleep # type: ignore

LDR_Pin = ADC(Pin(13, Pin.IN))
LED_Pin = Pin(5, Pin.OUT)

while True:
    LDR = LDR_Pin.read()
    print('LDR:',LDR)
    if LDR >=1500:
        LED_Pin.value(1)
    else:
        LED_Pin.value(0)
        sleep(0.5)