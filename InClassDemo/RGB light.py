import os, sys, io
import M5
from M5 import *
from hardware import *
import time


rgb = None
pin1 = None
pin2 = None


FutureTime = None
pressed = None
NowTime = None


def setup():
  global rgb, pin1, pin2, FutureTime, pressed, NowTime

  M5.begin()
  rgb = RGB()
  time.timezone('GMT-8')
  rgb.fill_color(0xffffff)
  pin1 = Pin(1, mode=Pin.IN)
  pin2 = Pin(2, mode=Pin.OUT)
  pressed = 0


def loop():
  global rgb, pin1, pin2, FutureTime, pressed, NowTime
  M5.update()
  rgb.set_color(0, 0)
  time.sleep_ms(500)
  rgb.set_color(0, 0xff0000)
  time.sleep_ms(500)


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
