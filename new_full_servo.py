from __future__ import division
import time
import math
from adafruit_servokit import ServoKit
#import mpu6050
import numpy as np

#задаем адресс объектов
##mpu6050 = mpu6050.mpu6050(0x68)
kit = ServoKit(channels=16)

# объявляем сервомоторы


OFFSET = {
    "FR_clav": -12,
    "FL_clav": 0,
    "BL_clav": -5,
    "BR_clav": 0,
    "FR_hum": 0,
    "FL_hum": -2,
    "BL_hum": 0,
    "BR_hum": 0,
    "FR_rad": 0,
    "FL_rad": 7,
    "BL_rad": 0,
    "BR_rad": -11,
}
# Ключица
def Front_Right_clauiculum(A):
    kit.servo[8].angle = 180 - A + OFFSET["FR_clav"]

def Front_Left_clauiculum(A):
    kit.servo[9].angle = A + OFFSET["FL_clav"]

def Back_Left_clauiculum(A):
    kit.servo[10].angle = 180 - A + OFFSET["BL_clav"]

def Back_Right_clauiculum(A):
    kit.servo[11].angle = A + OFFSET["BR_clav"]

# Плечевая кость
def Front_Right_humerus(A):
    kit.servo[4].angle = A + OFFSET["FR_hum"]

def Front_Left_humerus(A):
    kit.servo[5].angle = 180 - A + OFFSET["FL_hum"]
    time.sleep(1)

def Back_Left_humerus(A):
    kit.servo[6].angle = 180 - A + OFFSET["BL_hum"]

def Back_Right_humerus(A):
    kit.servo[7].angle = A + OFFSET["BR_hum"]
    time.sleep(1)



#лучевая/локтевая

# Лучевая/локтевая
def Front_Right_radii(A):
    kit.servo[0].angle = 180 - A + OFFSET["FR_rad"]

def Front_Left_radii(A):
    kit.servo[1].angle = A + OFFSET["FL_rad"]

def Back_Left_radii(A):
    kit.servo[2].angle = A + OFFSET["BL_rad"]

def Back_Right_radii(A):
    kit.servo[3].angle = 180 - A + OFFSET["BR_rad"]






def collarbone(A):
    Front_Right_clauiculum(A)
    Front_Left_clauiculum(A)
    time.sleep(1)
    Back_Left_clauiculum(A)
    Back_Right_clauiculum(A)

def humerus(A):
    Front_Right_humerus(A)
    Front_Left_humerus(A)
    time.sleep(1)
    Back_Left_humerus(A)
    Back_Right_humerus(A)

def radii(A):
    Front_Right_radii(A)
    Front_Left_radii(A)
    time.sleep(1)
    Back_Left_radii(A)
    Back_Right_radii(A)



#инициализация сервомоторов для калибровки
def SetUp():
    print("Инициализация началась")    

    time.sleep(1)
    collarbone(90)
    radii(100)
    time.sleep(1)
    humerus(60)
    time.sleep(1)
    print("Инициализация закончена")
    

def lay():
    radii(0)
    humerus(0)
    collarbone(90)

def sit():
    collarbone(90)

    Front_Right_humerus(90)
    Front_Left_humerus(90)
    Back_Left_humerus(45)
    Back_Right_humerus(45)
    Front_Right_radii(100)
    Front_Left_radii(100)
    Back_Left_radii(45)
    Back_Right_radii(45)
    
def Heil():
    sit()
    
    Back_Right_radii(60)

    Front_Left_radii(60)
    Front_Left_clauiculum(130)
    Front_Left_radii(160)
    time.sleep(0.2)
    i=0
    while i<5:
        i=i+1
        time.sleep(0.2)
        Front_Right_radii(45)
        time.sleep(0.2)
        Front_Right_radii(90)
    sit()

def ready_for_game():
    collarbone(90)

    Front_Right_humerus(60)
    Front_Left_humerus(60)
    Back_Left_humerus(45)
    Back_Right_humerus(45)
    Front_Right_radii(120)
    Front_Left_radii(120)
    Back_Left_radii(45)
    Back_Right_radii(45)

# lay()
# time.sleep(2)
sit()
time.sleep(2)
# SetUp()
# ############################

Heil()
lay()      
