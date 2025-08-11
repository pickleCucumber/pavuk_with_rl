import time

def smooth_move(servo_func, target_angle, duration=1.0):
    """
    Плавное движение сервомотора от текущего угла до целевого.
    :param servo_func: Функция для управления углом сервомотора.
    :param target_angle: Целевой угол для сервомотора.
    :param duration: Время для перехода (в секундах).
    """
    current_angle = servo_angles.get(servo_func.__name__.split('_')[0], 90)  # Начальный угол
    steps = 20  # Количество шагов для плавного перехода
    step_time = duration / steps  # Время для одного шага
    angle_step = (target_angle - current_angle) / steps  # Шаг угла
    
    for i in range(steps):
        new_angle = current_angle + angle_step * (i + 1)
        servo_func(new_angle)
        time.sleep(step_time)

def lay():
    print("Плавно ложится...")
    # Плавное движение для всех сервомоторов в положение лежа
    smooth_move(Front_Right_clauiculum, 90, 1.0)
    smooth_move(Front_Left_clauiculum, 90, 1.0)
    smooth_move(Back_Left_clauiculum, 90, 1.0)
    smooth_move(Back_Right_clauiculum, 90, 1.0)
    
    smooth_move(Front_Right_humerus, 10, 1.0)
    smooth_move(Front_Left_humerus, 10, 1.0)
    smooth_move(Back_Left_humerus, 10, 1.0)
    smooth_move(Back_Right_humerus, 10, 1.0)
    
    smooth_move(Front_Right_radii, 0, 1.0)
    smooth_move(Front_Left_radii, 0, 1.0)
    smooth_move(Back_Left_radii, 0, 1.0)
    smooth_move(Back_Right_radii, 0, 1.0)

def sit():
    print("Плавно садится...")
    # Плавное движение для всех сервомоторов в положение сидя
    smooth_move(Front_Right_clauiculum, 90, 1.0)
    smooth_move(Front_Left_clauiculum, 90, 1.0)
    smooth_move(Back_Left_clauiculum, 45, 1.0)
    smooth_move(Back_Right_clauiculum, 45, 1.0)
    
    smooth_move(Front_Right_humerus, 60, 1.0)
    smooth_move(Front_Left_humerus, 60, 1.0)
    smooth_move(Back_Left_humerus, 45, 1.0)
    smooth_move(Back_Right_humerus, 45, 1.0)
    
    smooth_move(Front_Right_radii, 120, 1.0)
    smooth_move(Front_Left_radii, 120, 1.0)
    smooth_move(Back_Left_radii, 45, 1.0)
    smooth_move(Back_Right_radii, 45, 1.0)

def Stay():
    print("Плавно встает...")
    # Плавное движение для всех сервомоторов в положение стоя
    smooth_move(Front_Right_clauiculum, 90, 1.0)
    smooth_move(Front_Left_clauiculum, 90, 1.0)
    smooth_move(Back_Left_clauiculum, 90, 1.0)
    smooth_move(Back_Right_clauiculum, 90, 1.0)
    
    smooth_move(Front_Right_humerus, 60, 1.0)
    smooth_move(Front_Left_humerus, 60, 1.0)
    smooth_move(Back_Left_humerus, 60, 1.0)
    smooth_move(Back_Right_humerus, 60, 1.0)
    
    smooth_move(Front_Right_radii, 90, 1.0)
    smooth_move(Front_Left_radii, 90, 1.0)
    smooth_move(Back_Left_radii, 90, 1.0)
    smooth_move(Back_Right_radii, 90, 1.0)

def lay_to_stay(duration=2.0):
    # Плавный переход из положения лежа в положение стоя
    print("Плавно переходит из лежа в стоя...")
    smooth_move(Front_Right_clauiculum, 90, duration)
    smooth_move(Front_Left_clauiculum, 90, duration)
    smooth_move(Back_Left_clauiculum, 90, duration)
    smooth_move(Back_Right_clauiculum, 90, duration)
    
    smooth_move(Front_Right_humerus, 60, duration)
    smooth_move(Front_Left_humerus, 60, duration)
    smooth_move(Back_Left_humerus, 60, duration)
    smooth_move(Back_Right_humerus, 60, duration)
    
    smooth_move(Front_Right_radii, 90, duration)
    smooth_move(Front_Left_radii, 90, duration)
    smooth_move(Back_Left_radii, 90, duration)
    smooth_move(Back_Right_radii, 90, duration)

def stay_to_lay(duration=2.0):
    # Плавный переход из положения стоя в положение лежа
    print("Плавно переходит из стоя в лежа...")
    smooth_move(Front_Right_clauiculum, 90, duration)
    smooth_move(Front_Left_clauiculum, 90, duration)
    smooth_move(Back_Left_clauiculum, 0, duration)
    smooth_move(Back_Right_clauiculum, 0, duration)
    
    smooth_move(Front_Right_humerus, 10, duration)
    smooth_move(Front_Left_humerus, 10, duration)
    smooth_move(Back_Left_humerus, 10, duration)
    smooth_move(Back_Right_humerus, 10, duration)
    
    smooth_move(Front_Right_radii, 0, duration)
    smooth_move(Front_Left_radii, 0, duration)
    smooth_move(Back_Left_radii, 0, duration)
    smooth_move(Back_Right_radii, 0, duration)
-----------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------
import time

# Задаем начальные углы для всех сервомоторов (состояния)
state = {
    "FR_clav": 90, "FL_clav": 90, "BL_clav": 90, "BR_clav": 90,
    "FR_hum": 60,  "FL_hum": 60,  "BL_hum": 60,  "BR_hum": 60,
    "FR_rad": 90,  "FL_rad": 90,  "BL_rad": 90,  "BR_rad": 90,
}

# Применяем OFFSET
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

# Задаем каналы для сервомоторов
kit = ServoKit(channels=16)

def set_servo_angle(servo_name, angle):
    """ Функция для плавного изменения угла сервомотора """
    kit.servo[servo_name].angle = angle
    state[servo_name] = angle

def smooth_move(servo_name, target_angle, duration=1.0):
    """ Плавное движение сервомотора """
    current_angle = state[servo_name]
    steps = 20
    step_time = duration / steps
    angle_step = (target_angle - current_angle) / steps
    
    for i in range(steps):
        new_angle = current_angle + angle_step * (i + 1)
        set_servo_angle(servo_name, new_angle)
        time.sleep(step_time)

def move_to_state(target_state, duration=2.0):
    """ Плавный переход к заданному состоянию (градусам) для всех сервомоторов """
    for servo_name, target_angle in target_state.items():
        smooth_move(servo_name, target_angle, duration)

# Состояния для разных положений
LAY_STATE = {
    "FR_clav": 90, "FL_clav": 90, "BL_clav": 90, "BR_clav": 90,
    "FR_hum": 10, "FL_hum": 10, "BL_hum": 10, "BR_hum": 10,
    "FR_rad": 0,  "FL_rad": 0,  "BL_rad": 0,  "BR_rad": 0,
}

SIT_STATE = {
    "FR_clav": 90, "FL_clav": 90, "BL_clav": 45, "BR_clav": 45,
    "FR_hum": 60,  "FL_hum": 60,  "BL_hum": 45,  "BR_hum": 45,
    "FR_rad": 120, "FL_rad": 120, "BL_rad": 45, "BR_rad": 45,
}

STAY_STATE = {
    "FR_clav": 90, "FL_clav": 90, "BL_clav": 90, "BR_clav": 90,
    "FR_hum": 60,  "FL_hum": 60,  "BL_hum": 60,  "BR_hum": 60,
    "FR_rad": 90,  "FL_rad": 90,  "BL_rad": 90,  "BR_rad": 90,
}

def lay():
    print("Плавно ложится...")
    move_to_state(LAY_STATE, 2.0)

def sit():
    print("Плавно садится...")
    move_to_state(SIT_STATE, 2.0)

def Stay():
    print("Плавно встает...")
    move_to_state(STAY_STATE, 2.0)

def lay_to_stay(duration=2.0):
    print("Плавно переходит из лежа в стоя...")
    move_to_state(STAY_STATE, duration)

def stay_to_lay(duration=2.0):
    print("Плавно переходит из стоя в лежа...")
    move_to_state(LAY_STATE, duration)

def turn_left(angle=15, duration=1.0):
    """
    Функция поворота направо (влево) собаки.
    :param angle: угол поворота в градусах.
    :param duration: время плавного поворота (в секундах).
    """
    print(f"Поворот налево на {angle} градусов.")
    
    # Плавно двигаем каждую ногу
    smooth_move(Front_Right_clauiculum, 90 - angle, duration)
    smooth_move(Back_Left_clauiculum, 90 - angle, duration)
    smooth_move(Front_Left_clauiculum, 90 + angle, duration)
    smooth_move(Back_Right_clauiculum, 90 + angle, duration)
    
    smooth_move(Front_Right_humerus, 60 - angle, duration)
    smooth_move(Back_Left_humerus, 60 - angle, duration)
    smooth_move(Front_Left_humerus, 60 + angle, duration)
    smooth_move(Back_Right_humerus, 60 + angle, duration)
    
    smooth_move(Front_Right_radii, 90 - angle, duration)
    smooth_move(Back_Left_radii, 90 - angle, duration)
    smooth_move(Front_Left_radii, 90 + angle, duration)
    smooth_move(Back_Right_radii, 90 + angle, duration)

def turn_right(angle=15, duration=1.0):
    """
    Функция поворота направо (вправо) собаки.
    :param angle: угол поворота в градусах.
    :param duration: время плавного поворота (в секундах).
    """
    print(f"Поворот направо на {angle} градусов.")
    
    # Плавно двигаем каждую ногу
    smooth_move(Front_Right_clauiculum, 90 + angle, duration)
    smooth_move(Back_Left_clauiculum, 90 + angle, duration)
    smooth_move(Front_Left_clauiculum, 90 - angle, duration)
    smooth_move(Back_Right_clauiculum, 90 - angle, duration)
    
    smooth_move(Front_Right_humerus, 60 + angle, duration)
    smooth_move(Back_Left_humerus, 60 + angle, duration)
    smooth_move(Front_Left_humerus, 60 - angle, duration)
    smooth_move(Back_Right_humerus, 60 - angle, duration)
    
    smooth_move(Front_Right_radii, 90 + angle, duration)
    smooth_move(Back_Left_radii, 90 + angle, duration)
    smooth_move(Front_Left_radii, 90 - angle, duration)
    smooth_move(Back_Right_radii, 90 - angle, duration)
-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
def turn_left(step_count=5, step_time=0.5, step_angle=15, step_height=30):
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
            
            # фаза 1: FR и BL (поворот влево)
            if phase:
                # передняя правая нога (FR) - смена знака
                clav_angle = neutral_angle - step_angle * (2 * t_norm - 1)  
                hum_angle = 60 - current_height
                Front_Right_clauiculum(clav_angle)
                Front_Right_humerus(hum_angle)
                
                # Задняя левая нога (BL) - смена знака
                clav_angle = neutral_angle - step_angle * (2 * t_norm - 1) 
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
                # передняя левая нога (FL) - смена знака
                clav_angle = neutral_angle - step_angle * (2 * t_norm - 1)  
                hum_angle = 60 - current_height
                Front_Left_clauiculum(clav_angle)
                Front_Left_humerus(hum_angle)
                
                # задняя правая нога (BR) - смена знака
                clav_angle = neutral_angle - step_angle * (2 * t_norm - 1)  
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

def turn_right(step_count=5, step_time=0.5, step_angle=15, step_height=30):
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
            
            # фаза 1: FR и BL (поворот вправо)
            if phase:
                # передняя левая нога (FL) - смена знака
                clav_angle = neutral_angle + step_angle * (2 * t_norm - 1)  
                hum_angle = 60 - current_height
                Front_Left_clauiculum(clav_angle)
                Front_Left_humerus(hum_angle)
                
                # Задняя правая нога (BR) - смена знака
                clav_angle = neutral_angle + step_angle * (2 * t_norm - 1) 
                hum_angle = 60 - current_height
                Back_Right_clauiculum(clav_angle)
                Back_Right_humerus(hum_angle)
                
                # остальные в опорной 
                Front_Right_clauiculum(neutral_angle)
                Front_Right_humerus(60)
                Back_Left_clauiculum(neutral_angle)
                Back_Left_humerus(60)
            
            # фаза 2: FL и BR
            else:
                # передняя правая нога (FR) - смена знака
                clav_angle = neutral_angle + step_angle * (2 * t_norm - 1)  
                hum_angle = 60 - current_height
                Front_Right_clauiculum(clav_angle)
                Front_Right_humerus(hum_angle)
                
                # задняя левая нога (BL) - смена знака
                clav_angle = neutral_angle + step_angle * (2 * t_norm - 1)  
                hum_angle = 60 - current_height
                Back_Left_clauiculum(clav_angle)
                Back_Left_humerus(hum_angle)
                
                # остальные в опорной 
                Front_Left_clauiculum(neutral_angle)
                Front_Left_humerus(60)
                Back_Right_clauiculum(neutral_angle)
                Back_Right_humerus(60)
            
            time.sleep(step_time / 10)
    
    Stay()
