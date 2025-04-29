def clamp_angle(angle):
    """Ограничивает угол в диапазоне 0-180 градусов"""
    return max(0, min(180, angle))

def apply_angles_safe(angles):
    """Безопасное применение углов с проверкой границ"""
    # Ключица
    Front_Right_clauiculum(clamp_angle(angles['FR_clav'] + OFFSET.get('FR_clav', 0)))
    Front_Left_clauiculum(clamp_angle(angles['FL_clav'] + OFFSET.get('FL_clav', 0))))
    Back_Left_clauiculum(clamp_angle(angles['BL_clav'] + OFFSET.get('BL_clav', 0))))
    Back_Right_clauiculum(clamp_angle(angles['BR_clav'] + OFFSET.get('BR_clav', 0))))
    
    # Плечи
    Front_Right_humerus(clamp_angle(angles['FR_hum'] + OFFSET.get('FR_hum', 0))))
    Front_Left_humerus(clamp_angle(angles['FL_hum'] + OFFSET.get('FL_hum', 0))))
    Back_Left_humerus(clamp_angle(angles['BL_hum'] + OFFSET.get('BL_hum', 0))))
    Back_Right_humerus(clamp_angle(angles['BR_hum'] + OFFSET.get('BR_hum', 0))))
    
    # Предплечья
    Front_Right_radii(clamp_angle(angles['FR_rad'] + OFFSET.get('FR_rad', 0))))
    Front_Left_radii(clamp_angle(angles['FL_rad'] + OFFSET.get('FL_rad', 0))))
    Back_Left_radii(clamp_angle(angles['BL_rad'] + OFFSET.get('BL_rad', 0))))
    Back_Right_radii(clamp_angle(angles['BR_rad'] + OFFSET.get('BR_rad', 0))))

def smooth_transition(start_angles, end_angles, duration=2.0, steps=50):
    """Безопасный переход с проверкой углов"""
    delay = duration / steps
    for i in range(steps+1):
        ratio = i / steps
        current_angles = {}
        for key in start_angles:
            current_angles[key] = start_angles[key] + (end_angles[key] - start_angles[key]) * ratio
        apply_angles_safe(current_angles)
        time.sleep(delay)

# Позы с безопасными углами
def get_lay_pose():
    return {
        'FR_clav': 90, 'FL_clav': 90, 'BL_clav': 90, 'BR_clav': 90,
        'FR_hum': 30,  'FL_hum': 30,  'BL_hum': 30,  'BR_hum': 30,  # Увеличен минимум для избежания 0
        'FR_rad': 30,  'FL_rad': 30,  'BL_rad': 30,  'BR_rad': 30
    }

def get_stay_pose():
    return {
        'FR_clav': 90, 'FL_clav': 90, 'BL_clav': 90, 'BR_clav': 90,
        'FR_hum': 60,  'FL_hum': 60,  'BL_hum': 60,  'BR_hum': 60,
        'FR_rad': 90,  'FL_rad': 90,  'BL_rad': 90,  'BR_rad': 90  # Уменьшен максимум для избежания 120
    }

def get_sit_pose():
    return {
        'FR_clav': 90, 'FL_clav': 90, 'BL_clav': 90, 'BR_clav': 90,
        'FR_hum': 80,  'FL_hum': 80,  'BL_hum': 50,  'BR_hum': 50,  # Скорректированные углы
        'FR_rad': 80,  'FL_rad': 80,  'BL_rad': 50,  'BR_rad': 50
    }

# Обновленные функции переходов
def lay_to_stay(duration=3.0):
    smooth_transition(get_lay_pose(), get_stay_pose(), duration)

def stay_to_lay(duration=3.0):
    smooth_transition(get_stay_pose(), get_lay_pose(), duration)

def lay_to_sit(duration=2.0):
    smooth_transition(get_lay_pose(), get_sit_pose(), duration)

def sit_to_lay(duration=2.0):
    smooth_transition(get_sit_pose(), get_lay_pose(), duration)

def sit_to_stay(duration=2.0):
    smooth_transition(get_sit_pose(), get_stay_pose(), duration)

def stay_to_sit(duration=2.0):
    smooth_transition(get_stay_pose(), get_sit_pose(), duration)






from __future__ import division
import time
import math
import numpy as np
from adafruit_servokit import ServoKit

# Инициализация серво-контроллера
kit = ServoKit(channels=16)

# Параметры робота
LEG_LENGTHS = {
    'shoulder': 5.0,  # Длина плечевого звена (см)
    'leg': 7.0,       # Длина бедренного звена (см)
    'foot': 10.0      # Длина голени (см)
}

# Текущие углы сервоприводов
servo_angles = {
    "FR_clav": 90, "FL_clav": 90, "BL_clav": 90, "BR_clav": 90,
    "FR_hum": 60,  "FL_hum": 60,  "BL_hum": 60,  "BR_hum": 60,
    "FR_rad": 90,  "FL_rad": 90,  "BL_rad": 90,  "BR_rad": 90,
}

OFFSET = {
    "FR_clav": -12, "FL_clav": 0, "BL_clav": -5, "BR_clav": 0,
    "FR_hum": 0, "FL_hum": -2, "BL_hum": 0, "BR_hum": 0,
    "FR_rad": 0, "FL_rad": 7, "BL_rad": 0, "BR_rad": -11,
}

# Функции управления сервоприводами (оставлены без изменений)
def Front_Right_clauiculum(A): 
    kit.servo[8].angle = 180 - A + OFFSET["FR_clav"]
    servo_angles['FR_clav'] = 180 - A + OFFSET["FR_clav"]
    
# ... (остальные функции управления сервоприводами остаются без изменений)

def inverse_kinematics(x, y, z, leg):
    """Обратная кинематика для одной ноги"""
    L1 = LEG_LENGTHS['shoulder']
    L2 = LEG_LENGTHS['leg']
    L3 = LEG_LENGTHS['foot']
    
    # Угол поворота основания (ключица)
    theta1 = math.atan2(y, x)
    
    # Углы для бедра и колена
    D = (x**2 + y**2 + z**2 - L1**2 - L2**2 - L3**2) / (2 * L2 * L3)
    theta3 = math.atan2(math.sqrt(1 - D**2), D)
    theta2 = math.atan2(z, math.sqrt(x**2 + y**2)) - math.atan2(L3 * math.sin(theta3), L2 + L3 * math.cos(theta3))
    
    # Конвертируем радианы в градусы
    theta1_deg = math.degrees(theta1)
    theta2_deg = math.degrees(theta2)
    theta3_deg = math.degrees(theta3)
    
    return theta1_deg, theta2_deg, theta3_deg

def set_leg_position(leg, x, y, z):
    """Устанавливает позицию ноги в пространстве"""
    angles = inverse_kinematics(x, y, z, leg)
    
    if leg == "FR":
        Front_Right_clauiculum(90 - angles[0])
        Front_Right_humerus(60 + angles[1])
        Front_Right_radii(90 - angles[2])
    elif leg == "FL":
        Front_Left_clauiculum(90 + angles[0])
        Front_Left_humerus(60 - angles[1])
        Front_Left_radii(90 + angles[2])
    elif leg == "BL":
        Back_Left_clauiculum(90 - angles[0])
        Back_Left_humerus(60 + angles[1])
        Back_Left_radii(90 - angles[2])
    elif leg == "BR":
        Back_Right_clauiculum(90 + angles[0])
        Back_Right_humerus(60 - angles[1])
        Back_Right_radii(90 + angles[2])

def walk_cycle(step_length=5, step_height=3, step_time=1.0, steps=4):
    """Цикл ходьбы с троттинг-алгоритмом"""
    half_step = step_time / 2
    
    for i in range(steps):
        # Фаза 1: FR и BL ноги двигаются
        for t in np.linspace(0, half_step, num=10):
            # Параболическая траектория
            progress = t / half_step
            z = 4 * step_height * progress * (1 - progress)
            x = step_length * (2 * progress - 1)
            
            # Движущиеся ноги
            set_leg_position("FR", x, 5, -10 + z)
            set_leg_position("BL", x, -5, -10 + z)
            
            # Опорные ноги
            set_leg_position("FL", -x, 5, -10)
            set_leg_position("BR", -x, -5, -10)
            
            time.sleep(half_step / 10)
        
        # Фаза 2: FL и BR ноги двигаются
        for t in np.linspace(0, half_step, num=10):
            progress = t / half_step
            z = 4 * step_height * progress * (1 - progress)
            x = step_length * (2 * progress - 1)
            
            set_leg_position("FL", x, 5, -10 + z)
            set_leg_position("BR", x, -5, -10 + z)
            
            set_leg_position("FR", -x, 5, -10)
            set_leg_position("BL", -x, -5, -10)
            
            time.sleep(half_step / 10)

def move_body(dx, dy, dz, duration=1.0):
    """Сдвигает тело в указанном направлении"""
    steps = 10
    delay = duration / steps
    
    for i in range(steps + 1):
        ratio = i / steps
        for leg in ["FR", "FL", "BL", "BR"]:
            y = 5 if leg in ["FR", "FL"] else -5
            x = -dx * ratio
            z = -10 - dz * ratio
            set_leg_position(leg, x, y, z)
        time.sleep(delay)

def rotate_body(angle_deg, duration=1.0):
    """Поворачивает тело вокруг оси Z"""
    steps = 10
    delay = duration / steps
    
    for i in range(steps + 1):
        ratio = i / steps
        current_angle = angle_deg * ratio
        
        for leg in ["FR", "FL", "BL", "BR"]:
            radius = 8  # Примерное расстояние от центра до ноги
            angle_rad = math.radians(current_angle)
            
            if leg == "FR":
                x = -radius * math.sin(angle_rad)
                y = radius * math.cos(angle_rad)
            elif leg == "FL":
                x = -radius * math.sin(angle_rad)
                y = -radius * math.cos(angle_rad)
            elif leg == "BL":
                x = radius * math.sin(angle_rad)
                y = -radius * math.cos(angle_rad)
            elif leg == "BR":
                x = radius * math.sin(angle_rad)
                y = radius * math.cos(angle_rad)
            
            set_leg_position(leg, x, y, -10)
        
        time.sleep(delay)

if __name__ == "__main__":
    Stay()
    time.sleep(1)
    
    # Пройти вперед 4 шага
    walk_cycle(step_length=6, step_height=4, steps=4)
    
    # Сдвинуть тело влево
    move_body(dx=3, dy=0, dz=0)
    
    # Повернуть направо
    rotate_body(angle_deg=30)
    
    # Вернуться в исходную позу
    Stay()
