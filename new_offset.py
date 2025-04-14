# Пример: функция для задания угла с учётом смещения
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

def set_servo(servo_function, angle, offset_key):
    # Оборачиваем установку угла, прибавляя offset
    real_angle = angle + OFFSET.get(offset_key, 0)
    servo_function(real_angle)
