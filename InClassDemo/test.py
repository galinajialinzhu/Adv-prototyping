import os, sys, io
import M5
from M5 import *
from hardware import *
import time


rgb = None
pin1 = None


FutureTime = None
NowTime = None


def setup():
  global rgb, pin1, FutureTime, NowTime

  M5.begin()
  rgb = RGB()
  time.timezone('GMT-8')
  rgb.fill_color(0xffffff)
  pin1 = Pin(1, mode=Pin.OUT)


def loop():
  global rgb, pin1, FutureTime, NowTime
  M5.update()
  print(pin1.value())
  if(pin1.value()):
      rgb.fill_color(0x3366ff)
  rgb.fill_color(0xffffff)
    

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
