from servo import Servo
import time
import os, sys, io
import M5
from M5 import *
from hardware import *

servo = Servo(pin=7)
adc = None
adc_val = None
adc = ADC(Pin(6), atten=ADC.ATTN_11DB)


def map_value(in_val, in_min, in_max, out_min, out_max):
    v = out_min + (in_val - in_min) * (out_max - out_min) / (in_max - in_min)
    if (v < out_min): 
        v = out_min
    elif (v > out_max): 
        v = out_max
    return int(v)  

while(True):
    adc_val = adc.read()
    adc_val_8bit = map_value(adc_val, in_min = 0, in_max = 4095,
                           out_min = 0, out_max = 255)
    #print(adc_val_8bit)
    servo.move(100)
    #time.sleep_ms(500)