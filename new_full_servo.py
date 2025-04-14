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

servo_angles = {
    "FR_clav": 90, "FL_clav": 90, "BL_clav": 90, "BR_clav": 90,
    "FR_hum": 60,  "FL_hum": 60,  "BL_hum": 60,  "BR_hum": 60,
    "FR_rad": 90,  "FL_rad": 90,  "BL_rad": 90,  "BR_rad": 90,
}

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
    servo_angles['FR_clav'] = 180 - A + OFFSET["FR_clav"]

def Front_Left_clauiculum(A):
    kit.servo[9].angle = A + OFFSET["FL_clav"]
    servo_angles['FL_clav'] = A + OFFSET["FR_clav"]

def Back_Left_clauiculum(A):
    kit.servo[10].angle = 180 - A + OFFSET["BL_clav"]
    servo_angles['BL_clav'] = 180 - A + OFFSET["BL_clav"]
    
def Back_Right_clauiculum(A):
    kit.servo[11].angle = A + OFFSET["BR_clav"]
    servo_angles['BR_clav'] = A + OFFSET["BR_clav"]
    

# Плечевая кость
def Front_Right_humerus(A):
    kit.servo[4].angle = A + OFFSET["FR_hum"]
    servo_angles['FR_hum'] = A + OFFSET["FR_hum"]

def Front_Left_humerus(A):
    kit.servo[5].angle = 180 - A + OFFSET["FL_hum"]
    servo_angles['FL_hum'] = 180 - A + OFFSET["FL_hum"]

def Back_Left_humerus(A):
    kit.servo[6].angle = 180 - A + OFFSET["BL_hum"]
    servo_angles['BL_hum'] =180 - A + OFFSET["BL_hum"]

def Back_Right_humerus(A):
    kit.servo[7].angle = A + OFFSET["BR_hum"]
    servo_angles['BR_hum'] = A + OFFSET["BR_hum"]


#лучевая/локтевая

# Лучевая/локтевая
def Front_Right_radii(A):
    kit.servo[0].angle = 180 - A + OFFSET["FR_rad"]
    servo_angles['FR_rad'] = 180 - A + OFFSET["FR_rad"]

def Front_Left_radii(A):
    kit.servo[1].angle = A + OFFSET["FL_rad"]
    servo_angles['FL_rad'] =  A + OFFSET["FL_rad"]


def Back_Left_radii(A):
    kit.servo[2].angle = A + OFFSET["BL_rad"]
    servo_angles['BL_rad'] =  A + OFFSET["BL_rad"]

def Back_Right_radii(A):
    kit.servo[3].angle = 180 - A + OFFSET["BR_rad"]
    servo_angles['BR_rad'] = 180 - A + OFFSET["BR_rad"]






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

def log_data():
    accel = sensor.get_accel_data()
    gyro = sensor.get_gyro_data()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

    row = [
        timestamp,
        accel['x'], accel['y'], accel['z'],
        gyro['x'], gyro['y'], gyro['z'],
        servo_angles['FR_clav'], servo_angles['FL_clav'], servo_angles['BL_clav'], servo_angles['BR_clav'],
        servo_angles['FR_hum'], servo_angles['FL_hum'], servo_angles['BL_hum'], servo_angles['BR_hum'],
        servo_angles['FR_rad'], servo_angles['FL_rad'], servo_angles['BL_rad'], servo_angles['BR_rad']
    ]

    with open('robot_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row)


### --- ИНИЦИАЛИЗАЦИЯ ФАЙЛА ---
def init_csv():
    with open('robot_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            'timestamp',
            'accel_x', 'accel_y', 'accel_z',
            'gyro_x', 'gyro_y', 'gyro_z',
            'FR_clav', 'FL_clav', 'BL_clav', 'BR_clav',
            'FR_hum', 'FL_hum', 'BL_hum', 'BR_hum',
            'FR_rad', 'FL_rad', 'BL_rad', 'BR_rad'
        ])
