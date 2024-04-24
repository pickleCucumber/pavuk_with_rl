from __future__ import division
import time
import math
from adafruit_servokit import ServoKit
import mpu6050
import numpy as np

#задаем адресс объектов
##mpu6050 = mpu6050.mpu6050(0x68)
kit = ServoKit(channels=16)

#читаем данные с датчика
def read_sensor_data():
    accelerometer_data = mpu6050.get_accel_data()
    gyroscope_data = mpu6050.get_gyro_data()
    temperature = mpu6050.get_temp()

    return accelerometer_data, gyroscope_data, temperature

#дальше описываем движения павука

def Joint_1(A):
    kit.servo[10].angle = 180-A
def Joint_2(A):
    kit.servo[5].angle = A
def Joint_3(A):
    kit.servo[2].angle = 180-A
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


def Left():
    Calf_4(90)
    Calf_1(90)
     
    Thigh_1(120) 
    Thigh_3(110) #желательно заменить на 120
    Joint_1(90) 
    Joint_3(90)
    time.sleep(0.2)
    Joint_2(120) 
    Joint_4(120)
    time.sleep(0.2)
    Thigh_1(100) 
    Thigh_3(90)

    time.sleep(0.2)
    Thigh_2(120) 
    Thigh_4(120)
    Joint_2(90) 
    Joint_4(90)
    time.sleep(0.2)
    Joint_1(60) 
    Joint_3(60)
    time.sleep(0.3)
    Thigh_2(90) 
    Thigh_4(90)

    time.sleep(0.2)
 
def Right():
    Calf_4(90)
    Calf_1(90)
     
    Thigh_1(120) 
    Thigh_3(110) #желательно заменить на 120
    Joint_1(90) 
    Joint_3(90)
    time.sleep(0.2)
    Joint_2(60) 
    Joint_4(60)
    time.sleep(0.2)
    Thigh_1(100) 
    Thigh_3(90)

    time.sleep(0.2)
    Thigh_2(120) 
    Thigh_4(120)
    Joint_2(90) 
    Joint_4(90)
    time.sleep(0.2)
    Joint_1(120) 
    Joint_3(120)
    time.sleep(0.3)
    Thigh_2(90) 
    Thigh_4(90)
    time.sleep(0.2)
    
    
    
def Forward():
    

     
    Thigh_1(120) #приподнимаем 1 и 3
    Thigh_3(110) #желательно заменить на 120
    Joint_1(90) 
    Joint_3(90)
    time.sleep(0.2)
    Joint_2(120) #делаем Х 2 и 4 
    Joint_4(60)
    time.sleep(0.2)
    Thigh_1(100) #опускаем 1 и 3
    Thigh_3(90)

    time.sleep(0.2)
    #Обраточка
    Thigh_2(120) #
    Thigh_4(120)
    Joint_2(90) #фиксируем 2 и 4
    Joint_4(90)
    time.sleep(0.2)
    Joint_1(120) #делаем Х 1 и 3
    Joint_3(60)
    time.sleep(0.3)
    Thigh_2(90) #опускаем 2 и 4 ногу 
    Thigh_4(90)
    time.sleep(0.2)    
    


SetUp()
time.sleep(1)
for i in range(10):
    Forward()



    #accelerometer_data, gyroscope_data, temperature = read_sensor_data()
    #print('куда я? ', accelerometer_data, 'хде я? ', gyroscope_data, 'как обстановочка?', temperature)
    #time.sleep(1)
