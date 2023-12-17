from servo import Servo
import time
import os, sys, io
import M5
from M5 import *
from hardware import *
from umqtt import *
import machine
import json


################
#set up
################

button = 'Face'
state = None
mode = None
current_time = 0
start_time = 0
end_time = 0
normal = 0
front_move = 0
servo_left = Servo(pin=7)
servo_right = Servo(pin=5)
face_normal_1 = Widgets.Image("res/img/Normal1.jpg", 0, 0)
face_normal_2 = Widgets.Image("res/img/Normal2.jpg", 0, 0)
face_normal_3 = Widgets.Image("res/img/Normal3.jpg", 0, 0)
face_happy_1 = Widgets.Image("res/img/happy1.jpg", 0, 0)
face_happy_2 = Widgets.Image("res/img/happy2.jpg", 0, 0)
face_happy_3 = Widgets.Image("res/img/happy3.jpg", 0, 0)
face_tired_1 = Widgets.Image("res/img/tired1.jpg", 0, 0)
face_tired_2 = Widgets.Image("res/img/tired2.jpg", 0, 0)
face_sleep_1 = Widgets.Image("res/img/sleep1.jpg", 0, 0)
face_sleep_2 = Widgets.Image("res/img/sleep2.jpg", 0, 0)
face_sleep_3 = Widgets.Image("res/img/sleep3.jpg", 0, 0)
mqtt_client = None

current_time = time.ticks_ms()

#switch_mode = Pin(41, mode=Pin.IN)



################
#communication wth adfruit io
################

def mqtt_Gariiizyu_Feeds_car_event(data):
    global bg, testt1, test2, mqtt_client, move_state
    print(data[1])
    move_state = data[1]
    
    
################
#movement function
################
        
def move_front():
    servo_left.move(125)
    servo_right.move(65)
    
def move_back():
    servo_left.move(65)
    servo_right.move(125)
    
def move_right():
    servo_left.move(125)
    servo_right.move(125)
    
def move_left():
    servo_left.move(65)
    servo_right.move(65)
    
def move_stop():
    servo_left.move(90)
    servo_right.move(90)
    
    
################
#face reaction function
################
    
def normal_face():
    global current_time, start_time, end_time, normal
    current_time = time.ticks_ms()
    if(current_time > end_time):
        start_time = time.ticks_ms()
        normal = 1
    end_time = start_time + 2800
    
    if(current_time < start_time + 1200)and(normal == 1):
        #face_normal_1.setVisible(True)
        face_normal_1.setImage("res/img/Normal1.jpg")
        normal = 2
    if(current_time > start_time + 1250)and(normal == 2):
        #face_normal_2.setVisible(True)
        face_normal_2.setImage("res/img/Normal2.jpg")
        normal = 3
    if(current_time > start_time + 1700)and(normal == 3):
        #face_normal_3.setVisible(True)
        face_normal_3.setImage("res/img/Normal3.jpg")
        normal = 4
    if(current_time > start_time + 2200)and(normal == 4):
        #face_normal_2.setVisible(True)
        face_normal_2.setImage("res/img/Normal2.jpg")
        normal = 1
    
def happy_face():
    face_happy_1.setVisible(True)
    time.sleep_ms(1200)
    face_happy_2.setVisible(True)
    time.sleep_ms(250)
    face_happy_3.setVisible(True)
    time.sleep_ms(1000)
    face_happy_2.setVisible(True)
    time.sleep_ms(250)
    face_happy_1.setVisible(True)
    time.sleep_ms(250)
    
def tired_face():
    face_normal_3.setVisible(True)
    time.sleep_ms(1200)
    face_tired_1.setVisible(True)
    time.sleep_ms(500)
    face_tired_2.setVisible(True)
    time.sleep_ms(1000)
    if (state == "sleep"):
        face_sleep_1.setVisible(True)
        time.sleep_ms(500)
        face_sleep_2.setVisible(True)
        time.sleep_ms(500)
        face_sleep_3.setVisible(True)
        time.sleep_ms(500)
        
################
#code
################
        
def setup():
    global mqtt_client

    Widgets.fillScreen(0x1ec9ff)
    mqtt_client = MQTTClient('TEST', 'io.adafruit.com', port=1883, user='Gariiizyu', password='aio_UhoC66OwPMFlvygE7G7zexH4htqK', keepalive=0)
    mqtt_client.connect(clean_session = True)
    mqtt_client.subscribe('Gariiizyu/feeds/car', mqtt_Gariiizyu_Feeds_car_event, qos=0)


def loop():
    global mqtt_client, move_state, mode, button
    
    print(button)
    
        
        
    
    if (button == 'Face'):
        move_stop()
        state = "normal"
        normal_face()
        current_time = time.ticks_ms()
        if (BtnA.wasClicked() and button == 'Face'):
            button = 'Motor'
        if (Imu.getAccel() > (1,1,1)):
            state = "happy"
            happy_face()
    
    M5.update()
    
    if (button == 'Motor'):
        mqtt_client.wait_msg()
        if (BtnA.wasClicked() and button == 'Motor'):
            button = 'Face'
        if(move_state ==b'front'):
            move_front()
        if(move_state ==b'back'):
            move_back()
        if(move_state ==b'left'):
            move_left()
        if(move_state ==b'right'):
            move_right()
        if(move_state == b'stop'):
            move_stop()
        
    
        
        

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

