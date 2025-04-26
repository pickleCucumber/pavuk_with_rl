import cv2
import mediapipe as mp

# MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

# пальцы(1 — поднят, 0 — согнут)
def get_finger_states(hand_landmarks):
    lm = hand_landmarks.landmark
    fingers = []

    # Указательный, средний, безымянный, мизинец
    tip_ids = [8, 12, 16, 20]
    pip_ids = [6, 10, 14, 18]

    for tip, pip in zip(tip_ids, pip_ids):
        fingers.append(1 if lm[tip].y < lm[pip].y else 0)

    # Большой палец (по X — для правой руки)
    fingers.append(1 if lm[4].x > lm[3].x else 0)

    return fingers  # [index, middle, ring, pinky, thumb]

# Распознавание жеста 
def recognize_gesture(fingers):
    index, middle, ring, pinky, thumb = fingers

    if fingers == [1, 1, 1, 1, 1]:
        return "Открытая ладонь"
    elif fingers == [0, 0, 0, 0, 0]:
        return "Кулак"
    elif fingers == [1, 0, 0, 0, 0]:
        return "Палец вверх"
    elif fingers == [1, 1, 0, 0, 0]:
        return "Peace ✌️"
    else:
        return "Неизвестно"

while True:
    success, img = cap.read()
    if not success:
        break

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    gesture = "Нет руки"

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            fingers = get_finger_states(hand_landmarks)
            gesture = recognize_gesture(fingers)

    # Вывод текста
    cv2.putText(img, f'Жест: {gesture}', (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.imshow("Gesture Recognition", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
