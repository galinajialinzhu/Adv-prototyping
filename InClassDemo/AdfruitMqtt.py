import os, sys, io
import M5
from M5 import *
from umqtt import *
from hardware import *
import time


mqtt_client = None
mqtt_timer = 0
adc = None
adc_val = None



def mqtt_button_feed_event(data):
  global image0, image_plus0, mqtt_client
  if (data[1]) == 'ON':
    print('sent data success')


def setup():
  global mqtt_client
  global adc, adc_val

  M5.begin()
  mqtt_client.subscribe('car', mqtt_button_feed_event, qos=0)

  mqtt_client = MQTTClient(
           'test',
           'io.adafruit.com',
           port=1883,
           user='Gariiizyu',
           password='aio_UhoC66OwPMFlvygE7G7zexH4htqK',
           keepalive=0
  )
  mqtt_client.connect(clean_session=True)
  adc = ADC(Pin(8), atten=ADC.ATTN_11DB)



def loop():
  global mqtt_client
  global mqtt_timer
  global adc, adc_val
  
  adc_val = adc.read()

  
  M5.update()
  if BtnA.wasPressed():
    print("button_press")
    mqtt_client.publish('Gariiizyu/feeds/button-feed', 'ON', qos=0)
  if BtnA.wasReleased():
    print("button_released")
    mqtt_client.publish('Gariiizyu/feeds/button-feed', 'OFF', qos=0)

      

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
