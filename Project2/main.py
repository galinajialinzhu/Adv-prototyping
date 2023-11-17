import js as p5
import time
from js import document


  
matrix_size = 8 
x_list = [25,75,125,175,225,275,325,375]
y_list = [25,75,125,175,225,275,325,375]
blink_duration = 3000
eye_open_duration = 2500
next_blink_time = 0
data_string = None
data_list = None
light_val = None
sound_val = None
noise = None
noise_time = 0

def setup():
  p5.createCanvas(400, 400)
  print('hello p5!')
  print(time.time())

def draw():
  global data_string, data_list
  global light_val, sound_val
  global noise_time,current_time
  # assign content of "data" div on index.html page to variable:
  data_string = document.getElementById("data").innerText
  # split data_string by comma, making a list:
  data_list = data_string.split(',')

  # assign 1st item of data_list to sensor_val:
  light_val = int(data_list[0])
  # assign 2nd item of data_list to sensor_val:
  sound_val = int(data_list[1])


  current_time = time.time() * 1000 

  if (sound_val>1000):
    noise_time = time.time() * 1000 +5000

  if(noise_time<current_time and light_val>1000):
    happy()
  elif (noise_time>current_time and light_val>1000):
    sad()
  elif (noise_time>current_time and light_val<1000):
    angry()
  elif (noise_time<current_time and light_val<1000):
    sleep()
  print(sound_val, light_val)

  #sad()
  #happy()
  #sleep()
  #angry()

def sad():
  global next_blink_time,current_time
  for x in range(8):
    for y in range(8):
      p5.noStroke()
      p5.fill(255,248,221)
      p5.ellipse(x_list[x], y_list[y], 50, 50);


  p5.fill(159,135,255)
  #FACE
  p5.ellipse(x_list[2], y_list[3], 50, 50);
  p5.ellipse(x_list[5], y_list[3], 50, 50);
  #SMILE
  p5.ellipse(x_list[1], y_list[6], 50, 50);
  p5.ellipse(x_list[2], y_list[5], 50, 50);
  p5.ellipse(x_list[3], y_list[5], 50, 50);
  p5.ellipse(x_list[4], y_list[5], 50, 50);
  p5.ellipse(x_list[5], y_list[5], 50, 50);
  p5.ellipse(x_list[6], y_list[6], 50, 50);

  if current_time > next_blink_time:
    # Blink
    p5.fill(255, 248, 221)
    p5.ellipse(x_list[2], y_list[2], 50, 50)
    p5.ellipse(x_list[5], y_list[2], 50, 50)
    next_blink_time = current_time + blink_duration
  elif current_time > next_blink_time - eye_open_duration:
    # Eyes open
    p5.fill(159, 135, 255)
    p5.ellipse(x_list[2], y_list[2], 50, 50)
    p5.ellipse(x_list[5], y_list[2], 50, 50)

def happy():
  global next_blink_time, current_time
  for x in range(8):
    for y in range(8):
      p5.noStroke()
      p5.fill(255,225,197)
      p5.ellipse(x_list[x], y_list[y], 50, 50);


  p5.fill(255,82,82)
  #FACE
  p5.ellipse(x_list[2], y_list[3], 50, 50);
  p5.ellipse(x_list[5], y_list[3], 50, 50);
  #SMILE when blink
  p5.ellipse(x_list[2], y_list[5], 50, 50);
  p5.ellipse(x_list[3], y_list[5], 50, 50);
  p5.ellipse(x_list[4], y_list[5], 50, 50);
  p5.ellipse(x_list[5], y_list[5], 50, 50);
  p5.ellipse(x_list[3], y_list[6], 50, 50);
  p5.ellipse(x_list[4], y_list[6], 50, 50);



  if current_time > next_blink_time:
    # Blink
    next_blink_time = current_time + blink_duration
  elif current_time > next_blink_time - eye_open_duration:
    # Eyes open
    p5.fill(255,225,197)
    p5.ellipse(x_list[3], y_list[6], 50, 50);
    p5.ellipse(x_list[4], y_list[6], 50, 50);
    p5.fill(255,82,82)
    p5.ellipse(x_list[2], y_list[2], 50, 50)
    p5.ellipse(x_list[5], y_list[2], 50, 50)
    #smile
    p5.ellipse(x_list[2], y_list[6], 50, 50);
    p5.ellipse(x_list[5], y_list[6], 50, 50);
    p5.ellipse(x_list[3], y_list[7], 50, 50);
    p5.ellipse(x_list[4], y_list[7], 50, 50);

def sleep():
  global next_blink_time, current_time
  for x in range(8):
    for y in range(8):
      p5.noStroke()
      p5.fill(218,246,255)
      p5.ellipse(x_list[x], y_list[y], 50, 50);



  #eyes
  p5.fill(135,147,255)
  p5.ellipse(x_list[1], y_list[5], 50, 50);
  p5.ellipse(x_list[2], y_list[5], 50, 50);
  p5.ellipse(x_list[5], y_list[5], 50, 50);
  p5.ellipse(x_list[6], y_list[5], 50, 50);
  #mouse
  p5.ellipse(x_list[3], y_list[7], 50, 50);
  p5.ellipse(x_list[4], y_list[7], 50, 50);
  #sleep
  p5.fill(82,245,255)
  p5.ellipse(x_list[4], y_list[1], 50, 50);
  p5.ellipse(x_list[5], y_list[1], 50, 50);
  p5.ellipse(x_list[5], y_list[2], 50, 50);
  p5.ellipse(x_list[6], y_list[2], 50, 50);

  

  if current_time > next_blink_time:
    # Blink
    next_blink_time = current_time + blink_duration
  elif current_time > next_blink_time - eye_open_duration:
    # Eyes open
    p5.fill(82,245,255)
    p5.ellipse(x_list[4], y_list[2], 50, 50);
    p5.ellipse(x_list[5], y_list[2], 50, 50);
    p5.ellipse(x_list[5], y_list[3], 50, 50);
    p5.ellipse(x_list[6], y_list[3], 50, 50);
    p5.fill(135,147,255)
    p5.ellipse(x_list[0], y_list[4], 50, 50);
    p5.ellipse(x_list[7], y_list[4], 50, 50);
    #face
    p5.fill(218,246,255)
    p5.ellipse(x_list[4], y_list[1], 50, 50);
    p5.ellipse(x_list[5], y_list[1], 50, 50);
    p5.ellipse(x_list[6], y_list[2], 50, 50);

def angry():
  global next_blink_time, current_time
  for x in range(8):
    for y in range(8):
      p5.noStroke()
      p5.fill(255,211,211)
      p5.ellipse(x_list[x], y_list[y], 50, 50);


  #eyes
  p5.fill(255,73,73)
  p5.ellipse(x_list[3], y_list[4], 50, 50);
  p5.ellipse(x_list[6], y_list[4], 50, 50);
  #mouse
  p5.ellipse(x_list[4], y_list[6], 50, 50);
  p5.ellipse(x_list[5], y_list[6], 50, 50);
  p5.ellipse(x_list[3], y_list[6], 50, 50);
  p5.ellipse(x_list[6], y_list[6], 50, 50);
  #angry
  p5.ellipse(x_list[0], y_list[1], 50, 50);
  p5.ellipse(x_list[1], y_list[0], 50, 50);
  p5.ellipse(x_list[1], y_list[1], 50, 50);
  p5.ellipse(x_list[2], y_list[1], 50, 50);
  p5.ellipse(x_list[1], y_list[2], 50, 50);
 

  

  if current_time > next_blink_time:
    # Blink
    next_blink_time = current_time + blink_duration
  elif current_time > next_blink_time - eye_open_duration:
    # Eyes open
    p5.fill(255,73,73)
    p5.ellipse(x_list[3], y_list[3], 50, 50);
    p5.ellipse(x_list[6], y_list[3], 50, 50);
    p5.ellipse(x_list[3], y_list[7], 50, 50);
    p5.ellipse(x_list[6], y_list[7], 50, 50);

    p5.fill(255,211,211)    
    p5.ellipse(x_list[3], y_list[6], 50, 50);
    p5.ellipse(x_list[6], y_list[6], 50, 50);
    


