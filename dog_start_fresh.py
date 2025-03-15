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

# ключица
def Front_Right_clauiculum(A):
    kit.servo[8].angle = 180-A

def Front_Left_clauiculum(A):
    kit.servo[9].angle = A

def Back_Left_clauiculum(A):
    kit.servo[10].angle = 180-A

def Back_Right_clauiculum(A):
    kit.servo[11].angle = A
    


#плечевая кость

# правая передняя плечевая кость
def Front_Right_humerus(A):
    kit.servo[4].angle = A

# левая передняя плечевая кость
def Front_Left_humerus(A):
    kit.servo[5].angle = 180-A
    time.sleep(1)

# левая задняя плечевая кость
def Back_Left_humerus(A):
    kit.servo[6].angle = 180-A

# правая задняя плечевая кость
def Back_Right_humerus(A):
    kit.servo[7].angle = A
    time.sleep(1)




#лучевая/локтевая

# правая передняя
def Front_Right_radii(A):
    kit.servo[0].angle = 180-A

# левая передняя
def Front_Left_radii(A):

    kit.servo[1].angle = A

# левая задняя
def Back_Left_radii(A):
    kit.servo[2].angle = A

# правая задняя
def Back_Right_radii(A):
    kit.servo[3].angle =180-A


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
    radii(90)
    time.sleep(1)
    humerus(60)
    time.sleep(1)
    print("Инициализация закончена")
    

def lay():
    radii(0)
    humerus(0)

def sit():
    collarbone(90)

    Front_Right_humerus(90)
    Front_Left_humerus(90)
    Back_Left_humerus(45)
    Back_Right_humerus(45)
    Front_Right_radii(120)
    Front_Left_radii(120)
    Back_Left_radii(30)
    Back_Right_radii(30)
    
def Heil():
    sit()
    Front_Left_radii(90)
    Front_Left_clauiculum(120)
    Front_Left_radii(120)
    time.sleep(0.2)
    i=0
    while i<5:
        i=i+1
        time.sleep(0.2)
        Front_Right_radii(45)
        time.sleep(0.2)
        Front_Right_radii(90)


def ready_for_game():
    collarbone(90)

    Front_Right_humerus(60)
    Front_Left_humerus(60)
    Back_Left_humerus(45)
    Back_Right_humerus(45)
    Front_Right_radii(120)
    Front_Left_radii(120)
    Back_Left_radii(30)
    Back_Right_radii(30)

    
def Forward():
        
##forward right
    # поднимаем переднюю правую и левую заднюю 
    Front_Right_humerus(40)
    Back_Left_humerus(40)
    Front_Right_radii(60)
    Back_Left_radii(60)
    time.sleep(0.2)
    print('часть 1')
    # time.sleep(0.2)
    Front_Right_humerus(100)
    Back_Left_humerus(100)
    Front_Right_radii(80)
    Back_Left_radii(90)
    print('часть 2')

    Front_Left_radii(120)
    Back_Right_radii(120)
    print('часть 3')

    #делаем Х 2 и 4

    # Joint_2(120)  
    # Joint_4(60)
    Front_Right_humerus(60)
    Back_Left_humerus(60)
    Front_Right_radii(90)
    Back_Left_radii(90)
    time.sleep(0.2)


    ####################################################
    ### forward left
    Front_Left_radii(80)
    Back_Right_radii(80)

    Front_Right_radii(100)
    Back_Left_radii(100)
    # time.sleep(0.2)

    Front_Left_humerus(80)
    Back_Right_humerus(80)

    Front_Left_radii(100)
    Back_Right_radii(100)
SetUp() 
# ############################
# for i in range(3):
#     Forward()
