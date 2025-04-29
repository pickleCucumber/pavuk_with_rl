from __future__ import division
import time
import math
import numpy as np
from adafruit_servokit import ServoKit
import csv
import os

kit = ServoKit(channels=16)

# Глобальный OFFSET для каждого сустава
OFFSET = {
    'Front_Right': {'claviculum': 90, 'humerus': 60, 'radii': 90},
    'Front_Left': {'claviculum': 90, 'humerus': 60, 'radii': 90},
    'Back_Left': {'claviculum': 90, 'humerus': 60, 'radii': 90},
    'Back_Right': {'claviculum': 90, 'humerus': 60, 'radii': 90},
}

# Управление сервами
SERVOS = {
    'Front_Right': {'claviculum': 8, 'humerus': 4, 'radii': 0},
    'Front_Left':  {'claviculum': 9, 'humerus': 5, 'radii': 1},
    'Back_Left':   {'claviculum': 10, 'humerus': 6, 'radii': 2},
    'Back_Right':  {'claviculum': 11, 'humerus': 7, 'radii': 3},
}

SYMMETRY = {
    'Front_Right': {'claviculum': True, 'humerus': False, 'radii': True},
    'Front_Left':  {'claviculum': False, 'humerus': True, 'radii': False},
    'Back_Left':   {'claviculum': True, 'humerus': True, 'radii': False},
    'Back_Right':  {'claviculum': False, 'humerus': False, 'radii': True},
}

def set_servo_angle(leg, joint, angle):
    channel = SERVOS[leg][joint]
    sym = SYMMETRY[leg][joint]
    offset = OFFSET[leg][joint]
    corrected_angle = offset + angle
    if sym:
        corrected_angle = 180 - corrected_angle
    kit.servo[channel].angle = corrected_angle

def apply_offsets():
    for leg in SERVOS:
        for joint in SERVOS[leg]:
            set_servo_angle(leg, joint, 0)

def set_pose(pose):
    for leg in pose:
        for joint in pose[leg]:
            set_servo_angle(leg, joint, pose[leg][joint])

def lay():
    pose = {
        'Front_Right': {'claviculum': 0, 'humerus': 0, 'radii': 0},
        'Front_Left': {'claviculum': 0, 'humerus': 0, 'radii': 0},
        'Back_Left': {'claviculum': 0, 'humerus': 0, 'radii': 0},
        'Back_Right': {'claviculum': 0, 'humerus': 0, 'radii': 0},
    }
    set_pose(pose)

def stay():
    pose = {
        'Front_Right': {'claviculum': 0, 'humerus': 0, 'radii': 0},
        'Front_Left': {'claviculum': 0, 'humerus': 0, 'radii': 0},
        'Back_Left': {'claviculum': 0, 'humerus': 0, 'radii': 0},
        'Back_Right': {'claviculum': 0, 'humerus': 0, 'radii': 0},
    }
    set_pose(pose)

# Балансировка (автономная функция)
def stabilize_robot(balance_data):
    global OFFSET
    for leg in OFFSET:
        for joint in OFFSET[leg]:
            delta = balance_data.get(leg, {}).get(joint, 0)
            OFFSET[leg][joint] += delta
    apply_offsets()
    save_offsets()

def save_offsets(filepath="offsets.csv"):
    with open(filepath, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Leg", "Joint", "Offset"])
        for leg in OFFSET:
            for joint in OFFSET[leg]:
                writer.writerow([leg, joint, OFFSET[leg][joint]])

def load_offsets(filepath="offsets.csv"):
    if not os.path.exists(filepath):
        return
    with open(filepath, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            leg = row["Leg"]
            joint = row["Joint"]
            OFFSET[leg][joint] = int(row["Offset"])

# Походка вперёд

def walk_forward_step():
    # Подъём 
    set_servo_angle('Front_Right', 'humerus', -25)
    set_servo_angle('Back_Left', 'humerus', -25)
    time.sleep(0.2)

    # Движение вперёд
    set_servo_angle('Front_Right', 'claviculum', 20)
    set_servo_angle('Back_Left', 'claviculum', -20)
    time.sleep(0.2)

    #  Опускание лап
    set_servo_angle('Front_Right', 'humerus', 0)
    set_servo_angle('Back_Left', 'humerus', 0)
    time.sleep(0.2)

    # Подъём других лап
    set_servo_angle('Front_Left', 'humerus', -25)
    set_servo_angle('Back_Right', 'humerus', -25)
    time.sleep(0.2)

    # Движение вперёд
    set_servo_angle('Front_Left', 'claviculum', 20)
    set_servo_angle('Back_Right', 'claviculum', -20)
    time.sleep(0.2)

    #  Опускание лап
    set_servo_angle('Front_Left', 'humerus', 0)
    set_servo_angle('Back_Right', 'humerus', 0)
    time.sleep(0.2)



def walk_forward(steps=3):
    for _ in range(steps):
        walk_forward_step()
