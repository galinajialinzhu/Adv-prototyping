# print 2 values separated by comma every 100ms:
# 1. analog input on pin G1 coverted to 8 bits (0 - 255 range) 
# 2. digital input on pin G41 (built-in button on AtomS3 Lite)

import os, sys, io
import M5
from M5 import *
from hardware import *
import time

light = None
light_val = None
sound = None
sound_val = None

def setup():
  global light, light_val, sound_val, sound
  M5.begin()
  # configure ADC input on pin G1 with 11dB attenuation:
  light = ADC(Pin(2), atten=ADC.ATTN_11DB)
  sound = ADC(Pin(1), atten=ADC.ATTN_11DB)

def loop():
  global light, light_val, sound_val, sound
  M5.update()
  # read 12-bit analog value (0 - 4095 range):
  light_val = light.read()
  sound_val = sound.read()
  #print(light_val)
  # convert light_val from 12-bit to 8-bit (0 - 255 range):
  # print 8-bit ADC value ending with comma:
  print(light_val, end=',')
  print(sound_val)
  # print built-in button value converted to integer:
  time.sleep_ms(100)
  
# map an input value (v_in) between min/max ranges:
def map_value(in_val, in_min, in_max, out_min, out_max):
  v = out_min + (in_val - in_min) * (out_max - out_min) / (in_max - in_min)
  if (v < out_min): 
    v = out_min 
  elif (v > out_max): 
    v = out_max
  return int(v)

if __name__ == '__main__':
  try:
    setup()
    while True:
      loop()
  except (Exception, KeyboardInterrupt) as e:
    try:
      from utility import print_error_msg
      print_error_msg(e)
    except ImportError:
      print("please update to latest firmware")

