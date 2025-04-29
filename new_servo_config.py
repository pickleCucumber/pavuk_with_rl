from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)

# Смещения для точной калибровки
OFFSET = {
    "FR_clav": 2,
    "FL_clav": -3,
    "BL_clav": 0,
    "BR_clav": 0,
    "FR_hum": 0,
    "FL_hum": 0,
    "BL_hum": 0,
    "BR_hum": 0,
    "FR_rad": 0,
    "FL_rad": 0,
    "BL_rad": 0,
    "BR_rad": 0,
}

# --- Функции управления суставами ---

# Ключица
def Front_Right_claviculum(A):
    kit.servo[8].angle = 180 - A + OFFSET["FR_clav"]

def Front_Left_claviculum(A):
    kit.servo[9].angle = A + OFFSET["FL_clav"]

def Back_Left_claviculum(A):
    kit.servo[10].angle = 180 - A + OFFSET["BL_clav"]

def Back_Right_claviculum(A):
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
    Front_Right_claviculum(A)
    Front_Left_claviculum(A)
    time.sleep(1)
    Back_Left_claviculum(A)
    Back_Right_claviculum(A)

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
