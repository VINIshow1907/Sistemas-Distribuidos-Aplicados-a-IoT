#o simulador worki não possui pinos touch
from machine import TouchPad, Pin # type: ignore

touch = TouchPad(Pin(4)) #GPIO 4 correspondente ao Touch0
led = Pin(2, Pin.OUT)

while True:
    valor = touch.read()
    print("Valor do toque:", valor)
    if valor < 500:
        led.value(1)
    else:
         led.value(0)
