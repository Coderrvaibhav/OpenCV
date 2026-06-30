import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils

# Webcam
cap = cv2.VideoCapture(0)

# Canvas
canvas = np.zeros((480, 640, 3), dtype=np.uint8)

# Previous point
prev_x, prev_y = 0, 0

# Colors
colors = {
    "Blue": (255, 0, 0),
    "Green": (0, 255, 0),
    "Red": (0, 0, 255),
    "Black": (0, 0, 0)
}

current_color = colors["Blue"]

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (640, 480))

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    # Top color buttons
    cv2.rectangle(frame, (0, 0), (160, 50), (255, 0, 0), -1)
    cv2.rectangle(frame, (160, 0), (320, 50), (0, 255, 0), -1)
    cv2.rectangle(frame, (320, 0), (480, 50), (0, 0, 255), -1)
    cv2.rectangle(frame, (480, 0), (640, 50), (0, 0, 0), -1)

    cv2.putText(frame, "BLUE", (40, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255),2)

    cv2.putText(frame, "GREEN", (185, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255),2)

    cv2.putText(frame, "RED", (365, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255),2)

    cv2.putText(frame, "ERASE", (510, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255),2)

    if result.multi_hand_landmarks:

        hand_landmarks = result.multi_hand_landmarks[0]

        mp_draw.draw_landmarks(
            frame,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS
        )

        h, w, _ = frame.shape

        # Index fingertip
        x = int(hand_landmarks.landmark[8].x * w)
        y = int(hand_landmarks.landmark[8].y * h)

        cv2.circle(frame, (x, y), 10, (0,255,255), -1)

        # Select color
        if y < 50:
            if x < 160:
                current_color = colors["Blue"]
            elif x < 320:
                current_color = colors["Green"]
            elif x < 480:
                current_color = colors["Red"]
            else:
                current_color = colors["Black"]

            prev_x, prev_y = 0, 0

        else:
            if prev_x == 0 and prev_y == 0:
                prev_x, prev_y = x, y

            cv2.line(
                canvas,
                (prev_x, prev_y),
                (x, y),
                current_color,
                5
            )

            prev_x, prev_y = x, y

    else:
        prev_x, prev_y = 0, 0

    # Merge drawing with webcam
    gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
    _, inv = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY_INV)
    inv = cv2.cvtColor(inv, cv2.COLOR_GRAY2BGR)

    frame = cv2.bitwise_and(frame, inv)
    frame = cv2.bitwise_or(frame, canvas)

    cv2.putText(
        frame,
        "Press C = Clear | S = Save | Q = Quit",
        (10,470),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255,255,255),
        2
    )

    cv2.imshow("Air Canvas", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('c'):
        canvas = np.zeros((480,640,3), dtype=np.uint8)

    elif key == ord('s'):
        cv2.imwrite("drawing.png", canvas)
        print("Drawing Saved!")

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()