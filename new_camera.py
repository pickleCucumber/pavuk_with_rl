from picamera import PiCamera
from time import sleep
import os

def capture_and_save_image(folder_path="images", filename_prefix="capture"):
    """    
    :param folder_path: Папка, куда будет сохранено изображение.
    :param filename_prefix: Префикс имени файла изображения.
    :return: Полный путь к сохраненному файлу.
    """
    # убедимся, что папка существует
    os.makedirs(folder_path, exist_ok=True)
    
    # создаем уникальное имя файла
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    filename = f"{filename_prefix}_{timestamp}.jpg"
    full_path = os.path.join(folder_path, filename)

    # инициализация камеры и захват
    camera = PiCamera()
    camera.resolution = (1024, 768)
    sleep(2)  
    camera.capture(full_path)
    camera.close()
    
    return full_path
if __name__ == "__main__":
    image_path = capture_and_save_image()
