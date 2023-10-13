import os, sys, io
import M5
from M5 import *
from hardware import *
import time


rgb = None
pin39 = None
pin41 = None


import random

pressed = None
FutureTime = None
NowTime = None
i = None


def setup():
  global rgb, pin39, pin41, pressed, FutureTime, NowTime, i

  M5.begin()
  rgb = RGB()
  time.timezone('GMT-8')
  rgb.fill_color(0xffffff)
  pin39 = Pin(39, mode=Pin.IN, pull=Pin.PULL_UP)
  pin41 = Pin(41, mode=Pin.IN)
  pressed = 0
  i = 0


def loop():
  global rgb, pin39, pin41, pressed, FutureTime, NowTime, i
  M5.update()
  pressed = 0
  if (pin41.value()) == 0:
    FutureTime = time.ticks_ms()
    NowTime = time.ticks_ms()
    if NowTime <= FutureTime + 2000:
      while not ((pin39.value()) == 0 or NowTime >= FutureTime + 2000):
        NowTime = time.ticks_ms()
        rgb.fill_color(0xff6600)
        rgb.set_brightness(80)
        time.sleep_ms(50)
      if NowTime <= FutureTime + 7000:
        while not ((pin39.value()) == 0 or NowTime >= FutureTime + 7000):
          NowTime = time.ticks_ms()
          rgb.fill_color(0xff0000)
          rgb.set_brightness(80)
          time.sleep_ms(50)
        while not ((pin41.value()) == 0 or NowTime >= FutureTime + 7000):
          NowTime = time.ticks_ms()
          rgb.fill_color(0x33ccff)
          rgb.set_brightness((random.randint(0, 100)))
          time.sleep_ms(50)
  else:
    if (pin39.value()) == 0:
      FutureTime = time.ticks_ms()
      NowTime = time.ticks_ms()
      if NowTime <= FutureTime + 2000:
        NowTime = time.ticks_ms()
        print('hug')
        for i in range(254):
          rgb.fill_color(get_color(255,255,i))
          rgb.set_brightness(80)
          time.sleep_ms(50)

      
          print(i)
    print('not showing anything')
    rgb.fill_color(0xffffff)
    rgb.set_brightness(80)
    time.sleep_ms(50)


def get_color(r, g, b):
    return (r << 16) | (g << 8) | b


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
