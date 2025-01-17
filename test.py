from adafruit_servokit import ServoKit
import time 
kit = ServoKit(channels=16)
for i in range(13):
    kit.servo[i].angle = 90
    time.sleep(1)
