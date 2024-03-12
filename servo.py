from __future__ import division
import time
import math
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)


def Joint_1(A):
    kit.servo[10].angle = A
def Joint_2(A):
    kit.servo[5].angle = A
def Joint_3(A):
    kit.servo[2].angle = A
def Joint_4(A):
    kit.servo[13].angle = A
    
def Thigh_1(A):
    kit.servo[11].angle = 180-A
def Thigh_2(A):
    kit.servo[4].angle = A
def Thigh_3(A):
    kit.servo[1].angle = 180-A
def Thigh_4(A):
    kit.servo[14].angle = A

def Calf_1(A):
    kit.servo[12].angle = 180-A
def Calf_2(A):
    kit.servo[3].angle = A
def Calf_3(A):
    kit.servo[0].angle = 180- A
def Calf_4(A):
    kit.servo[15].angle = A

def Joints(A):
    Joint_1(A)
    Joint_2(A)
    Joint_3(A)
    Joint_4(A)

def Thighs(A):
    Thigh_1(A)
    Thigh_2(A)
    Thigh_3(A)
    Thigh_4(A)

def Calfs(A):
    Calf_1(A)
    Calf_2(A)
    Calf_3(A)
    Calf_4(A)

#поднимает лапы
def LegsUp():
    time.sleep(1)
    Joints(90)
    time.sleep(1)
    Thighs(0)
    Calfs(180)
    time.sleep(1)

#инициализация сервомоторов для калибровки
def SetUp():
    print("Инициализация началась")    

    time.sleep(1)
    Joints(90)
    time.sleep(1)
    Thighs(90)
    time.sleep(1)
    Calfs(90)
    time.sleep(1)
    print("Инициализация закончена")
    
#сел на пенек    
def Sit():
    Calfs(30)
    time.sleep(1)
    Thighs(30)
    
#проходочка
def Forward():
    
    Calf_1(45)    
    Calf_3(45)

     
    Thigh_1(30) 
    Thigh_3(30)
    Joint_1(90)
    Joint_3(90)
    time.sleep(0.2)
    Joint_2(120) 
    Joint_4(60)
    time.sleep(0.2)
    Calf_1(90)
    Thigh_1(90) 
    Thigh_3(90)
    Calf_3(90)
    time.sleep(0.2)
    Calf_2(45)
    
    Thigh_2(45)
    Calf_4(45)
    Thigh_4(45)
    Joint_2(90) 
    Joint_4(90)
    Joint_1(60) 
    Joint_3(60)
    time.sleep(0.2)
    Calf_2(90)
    Thigh_2(90) 
    Thigh_4(90)
    Calf_4(90)

    time.sleep(0.2)
 



SetUp()
LegsUp()
time.sleep(2)
Sit()
time.sleep(2)
while True:
    Forward()
