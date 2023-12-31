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
  pressed = 0
  NowTime = time.ticks_ms()
  FutureTime = time.ticks_ms()
  if BtnA.wasClicked():
    if NowTime <= FutureTime + 2000:
      while not ((pin1.value()) != 0 or NowTime >= FutureTime + 2000):
        NowTime = time.ticks_ms()
        rgb.fill_color(0xff6600)
        time.sleep_ms(50)
      if NowTime <= FutureTime + 7000:
        while not ((pin1.value()) != 0 or NowTime >= FutureTime + 7000):
          NowTime = time.ticks_ms()
          rgb.fill_color(0xff0000)
          time.sleep_ms(50)
        while not ((pin1.value()) == 0 or NowTime >= FutureTime + 7000):
          NowTime = time.ticks_ms()
          rgb.fill_color(0x33ccff)
          time.sleep_ms(50)
  else:
    if (pin1.value()) != 0:
      print('hug')
      rgb.fill_color(0xffcc00)
      time.sleep(5)
    print('not showing anything')
    rgb.fill_color(0xffffff)
    time.sleep_ms(50)


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
