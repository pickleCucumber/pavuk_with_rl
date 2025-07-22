from __future__ import division
import time
import csv
import math
from adafruit_servokit import ServoKit
import mpu6050
import numpy as np
import smbus


#задаем адресс объектов
# mpu6050 = mpu6050.mpu6050(0x68)
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
    "BL_hum": 5,
    "BR_hum": 0,
    "FR_rad": 0,
    "FL_rad": 7,
    "BL_rad": 7,
    "BR_rad": -17,
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
def Stay():
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
    while i<7:
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
    accel = mpu6050.get_accel_data()
    gyro = mpu6050.get_gyro_data()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

    row = [
        timestamp,
        accel['x'], accel['y'], accel['z'],
        gyro['x'], gyro['y'], gyro['z'],
        servo_angles['FR_clav'], servo_angles['FL_clav'], servo_angles['BL_clav'], servo_angles['BR_clav'],
        servo_angles['FR_hum'], servo_angles['FL_hum'], servo_angles['BL_hum'], servo_angles['BR_hum'],
        servo_angles['FR_rad'], servo_angles['FL_rad'], servo_angles['BL_rad'], servo_angles['BR_rad']
    ]

    with open('/home/rpi/Desktop/data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row)
    print('записано')


#инициализация файла
def init_csv():
    with open('/home/rpi/Desktop/data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            'timestamp',
            'accel_x', 'accel_y', 'accel_z',
            'gyro_x', 'gyro_y', 'gyro_z',
            'FR_clav', 'FL_clav', 'BL_clav', 'BR_clav',
            'FR_hum', 'FL_hum', 'BL_hum', 'BR_hum',
            'FR_rad', 'FL_rad', 'BL_rad', 'BR_rad'
        ])


def move_forward(step_count=5, step_time=0.5, step_length=15, step_height=30):

    Stay()
    time.sleep(1)
    
    # константы
    neutral_angle = 90
    half_step_time = step_time / 2
    
    for step in range(step_count):
        print(f"Шаг {step + 1}/{step_count}")
        
        # разбиваем шаг на 10 промежутков для плавности
        for i in range(10):
            t = i * 0.1 * step_time
            phase = (t % step_time) < half_step_time
            
            # нормализованное время для фазы
            t_norm = (t % half_step_time) / half_step_time
            
            # вычисляем высоту по параболе (плавный подъем/спуск)
            current_height = 4 * step_height * t_norm * (1 - t_norm)
            
            # фаза 1: FR и BL 
            if phase:
                # передняя правая нога (FR) - смена знака
                clav_angle = neutral_angle - step_length * (2*t_norm - 1)  
                hum_angle = 60 - current_height
                Front_Right_clauiculum(clav_angle)
                Front_Right_humerus(hum_angle)
                
                # Задняя левая нога (BL) - смена знака
                clav_angle = neutral_angle - step_length * (2*t_norm - 1) 
                hum_angle = 60 - current_height
                Back_Left_clauiculum(clav_angle)
                Back_Left_humerus(hum_angle)
                
                # остальные в опорной 
                Front_Left_clauiculum(neutral_angle)
                Front_Left_humerus(60)
                Back_Right_clauiculum(neutral_angle)
                Back_Right_humerus(60)
            
            # фаза 2: FL и BR 
            else:
                # передняя левая нога (FL) -смена знака
                clav_angle = neutral_angle - step_length * (2*t_norm - 1)  
                hum_angle = 60 - current_height
                Front_Left_clauiculum(clav_angle)
                Front_Left_humerus(hum_angle)
                
                # задняя правая нога (BR) - смена знака
                clav_angle = neutral_angle - step_length * (2*t_norm - 1)  
                hum_angle = 60 - current_height
                Back_Right_clauiculum(clav_angle)
                Back_Right_humerus(hum_angle)
                
                # остальные в опорной 
                Front_Right_clauiculum(neutral_angle)
                Front_Right_humerus(60)
                Back_Left_clauiculum(neutral_angle)
                Back_Left_humerus(60)
            
            time.sleep(step_time / 10)
    
    Stay()


sit
time.sleep(2)
Heil()
# lay_to_stay(duration=3.0)
time.sleep(2)
# # 
# Stay()
# time.sleep(3)
# move_forward(step_count=3, step_time=0.8, step_length=12, step_height=25)
