import numpy as np
from scipy import signal

class DogRobotController:
    def __init__(self):
        # Фильтр для сглаживания данных с датчиков
        self.filter_accel = signal.butter(2, 0.1, 'lowpass', fs=10, output='sos')
        self.filter_gyro = signal.butter(2, 0.2, 'lowpass', fs=10, output='sos')
        
        # Параметры сервоприводов по умолчанию
        self.default_angles = {
            'FR_clav': 90, 'FL_clav': 90, 'BL_clav': 90, 'BR_clav': 90,
            'FR_hum': 60, 'FL_hum': 60, 'BL_hum': 60, 'BR_hum': 60,
            'FR_rad': 90, 'FL_rad': 90, 'BL_rad': 90, 'BR_rad': 90
        }
        
        # Коэффициенты коррекции
        self.kp_balance = 0.5  # Коэффициент коррекции баланса
        self.kp_step = 0.3     # Коэффициент шага
        
    def filter_sensor_data(self, accel, gyro):
        """Фильтрация данных с датчиков"""
        accel_filtered = signal.sosfiltfilt(self.filter_accel, accel)
        gyro_filtered = signal.sosfiltfilt(self.filter_gyro, gyro)
        return accel_filtered, gyro_filtered
    
    def calculate_balance_correction(self, accel, gyro):
        """Вычисление коррекции баланса"""
        # Углы наклона (упрощенный расчет)
        roll = np.arctan2(accel[1], accel[2]) * 180/np.pi
        pitch = np.arctan2(-accel[0], np.sqrt(accel[1]**2 + accel[2]**2)) * 180/np.pi
        
        # Коррекция для передних и задних ног
        front_correction = pitch * self.kp_balance
        rear_correction = -pitch * self.kp_balance
        
        # Коррекция для левых и правых ног
        left_correction = roll * self.kp_balance
        right_correction = -roll * self.kp_balance
        
        return {
            'FR_hum': front_correction + right_correction,
            'FL_hum': front_correction + left_correction,
            'BR_hum': rear_correction + right_correction,
            'BL_hum': rear_correction + left_correction
        }
    
    def generate_gait_pattern(self, step_phase):
        """Генерация паттерна походки"""
        # Фазовая переменная 0-1
        phase = step_phase % 1.0
        
        # Паттерн для ног (аллюр - рысь)
        leg_phases = {
            'FR': (phase + 0.5) % 1.0,
            'FL': phase % 1.0,
            'BR': phase % 1.0,
            'BL': (phase + 0.5) % 1.0
        }
        
        gait_pattern = {}
        for leg, ph in leg_phases.items():
            if ph < 0.5:  # Фаза опоры
                gait_pattern[f'{leg}_hum'] = 60 + 30 * np.sin(ph * np.pi)
                gait_pattern[f'{leg}_rad'] = 90 - 40 * np.sin(ph * np.pi)
            else:  # Фаза переноса
                gait_pattern[f'{leg}_hum'] = 90 - 60 * (ph - 0.5)
                gait_pattern[f'{leg}_rad'] = 50 + 80 * (ph - 0.5)
                
        return gait_pattern
    
    def walk_forward(self, sensor_data, step_phase):
        """Функция движения вперед с коррекцией баланса"""
        # Извлечение данных с датчиков
        accel = np.array([sensor_data['accel_x'], sensor_data['accel_y'], sensor_data['accel_z']])
        gyro = np.array([sensor_data['gyro_x'], sensor_data['gyro_y'], sensor_data['gyro_z']])
        
        # Фильтрация данных
        accel_filtered, gyro_filtered = self.filter_sensor_data(accel, gyro)
        
        # Вычисление коррекции баланса
        balance_correction = self.calculate_balance_correction(accel_filtered, gyro_filtered)
        
        # Генерация паттерна походки
        gait_pattern = self.generate_gait_pattern(step_phase)
        
        # Комбинирование коррекции баланса и паттерна походки
        servo_angles = self.default_angles.copy()
        
        for leg in ['FR', 'FL', 'BR', 'BL']:
            servo_angles[f'{leg}_hum'] += balance_correction[f'{leg}_hum']
            servo_angles[f'{leg}_rad'] = gait_pattern[f'{leg}_rad']
            
            # Небольшая коррекция ключиц для стабилизации
            servo_angles[f'{leg}_clav'] += balance_correction[f'{leg}_hum'] * 0.3
        
        return servo_angles

# Пример использования
controller = DogRobotController()

# Имитация данных с датчиков 
sensor_data = {
    'accel_x': 1.07, 'accel_y': -0.74, 'accel_z': -10.73,
    'gyro_x': -3.59, 'gyro_y': 0.39, 'gyro_z': -1.49
}

# Цикл шагов (0-1 - один полный шаг)
for step in range(10):
    step_phase = step * 0.1  # Прогресс шага от 0 до 1
    angles = controller.walk_forward(sensor_data, step_phase)
    print(f"\nШаг {step}: Фаза {step_phase:.1f}")
    print("Углы сервоприводов:")
    print(f"FR: hum={angles['FR_hum']:.1f}°, rad={angles['FR_rad']:.1f}°")
    print(f"FL: hum={angles['FL_hum']:.1f}°, rad={angles['FL_rad']:.1f}°")
    print(f"BR: hum={angles['BR_hum']:.1f}°, rad={angles['BR_rad']:.1f}°")
    print(f"BL: hum={angles['BL_hum']:.1f}°, rad={angles['BL_rad']:.1f}°")
