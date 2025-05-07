#importação de bibliotecas
from machine import Pin # type: ignore
from time import sleep

led_vm = Pin(2, Pin.OUT)
led_am = Pin(4, Pin.OUT)
led_vd = Pin(5, Pin.OUT)

try:
    while True:
        #led vermelho e acesso
        led_vm.value(1)
        sleep(3)
        #led verde acesso
        led_vd.value(1)

        #vermelho é apagado
        led_vm.value(0)
        sleep(3)

        #após 2 segundos o led amarelo apaga
        led_am.value(1)
        #led verde é apagado
        led_vd.value(0)
        sleep(1)

        led_am.value(0)
except KeyboardInterrupt:

    led_vm.value(0)
    led_am.value(0)
    led_vd.value(0)