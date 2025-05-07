from machine import Pin # type: ignore
from time import sleep

led = Pin(2, Pin.OUT)


botao =Pin(23, Pin.IN)

try:
  while True:
    led.value(botao.value())
    sleep(0.2)

except KeyboardInterrupt:
  led.value(0)