# project 4
## Ideation
![10781702804935_ pic](https://github.com/galinajialinzhu/Adv-prototyping/assets/92561657/2168d004-7f47-4bb5-a96f-81d045148b0a)
this is the ideation of my project, I want to make an emotional support robot that could provide fun interaction with users.
Then I designed three scenarios for this robot. (but in the end, only two worked due to limited pins... but I tried to combine the ai camera)
## Design

![Slide 4_3 - 2](https://github.com/galinajialinzhu/Adv-prototyping/assets/92561657/2f8bbc50-a4b7-456f-95dc-ae9d5ebae3db)

I am also trying hard with the mqtt. it did not let me subscribe at first, but then I checked some of the documentation that showed uiflow2 had some broken unfinished code there. And then I fix them with my handwriting code:


def setup():
    mqtt_client = MQTTClient('TEST', 'io.adafruit.com', port=1883, user='', password='', keepalive=0)
    mqtt_client.connect(clean_session = True)
    mqtt_client.subscribe('Gariiizyu/feeds/car', mqtt_Gariiizyu_Feeds_car_event, qos=0)
    
def loop():
    mqtt_client.wait_msg()

Then I 3d printing the case for my robot. 
![QQ截图20231217014355](https://github.com/galinajialinzhu/Adv-prototyping/assets/92561657/7fb49731-da11-45f1-8d05-007a0c724e0f)




## video
this is my final video for the project.
https://youtu.be/AcrXHfU6Hic
