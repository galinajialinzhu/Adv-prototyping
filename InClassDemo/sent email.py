import network
import urequests
import M5
from M5 import *
from hardware import *

wlan = network.WLAN(network.STA_IF)
print("wlan is connected = ", wlan.isconnected())

while (True):
        M5.update()
        if BtnA.wasPressed():
            print('button pressed')
            req = urequests.request(
                method='POST',
                url='https://maker.ifttt.com/trigger/Button_press/json/with/key/kIocjMwi-XHEfMVXRhWbArMoFONHsOGBHy-VOSKEbLX',
                json ={'button_value': '0'},
                headers={'Content-Type': 'application/json'}
                )
            print('success!')