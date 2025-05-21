from machine import Pin, ADC # type: ignore
from time import sleep
from math import log

def obterTemperatura(termistor):
    tempK = log(10000.0 * (4096.0 / termistor - 1))
    tempK = 1 / (0.001129148 + (0.000234125 + 
    (0.0000000876741 * tempK * tempK )) * tempK)
    tempC = tempK - 273.15
    return tempC

adc = ADC(Pin(13))
adc.atten(ADC.ATTN_11DB)

while True:
    temp = obterTemperatura(adc.read())
    print ("Temperatura: ", round(temp, 1), "°C")
    sleep(1.0)