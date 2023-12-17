from servo import Servo
import time
import os, sys, io
import M5
from M5 import *
from hardware import *
from umqtt import *
import machine
import json

switch_mode =None

def setup():
  global switch_mode
  M5.begin()
  switch_mode = Pin(1, mode=Pin.IN ,pull=Pin.PULL_UP)



def loop():
  global switch_mode
  nowtime = time.tick_ms()
  if (time.tick_ms() - nowtime) > 100:
    print(switch_mode.value())
    nowtime = time.tick_ms()
  M5.update()


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
