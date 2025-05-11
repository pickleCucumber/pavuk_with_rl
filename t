from picamera2 import Picamera2
import cv2

# Инициализация камеры
picam2 = Picamera2()
picam2.preview_configuration.main.size = (640, 480)
picam2.preview_configuration.main.format = "RGB888"
picam2.configure("preview")
picam2.start()

while True:
    frame = picam2.capture_array()
    
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  # Потому что Picamera2 отдаёт RGB
    cv2.imshow("Picamera2 stream", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

picam2.stop()
cv2.destroyAllWindows()
