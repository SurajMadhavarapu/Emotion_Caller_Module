import cv2
import time
import os
import pyautogui
from fer import FER

detector = FER(mtcnn=True)
cap = cv2.VideoCapture(0)

BEST_FRIEND_NAME = "9700616733" 
SAD_DURATION_THRESHOLD = 2 
SAD_CONFIDENCE_THRESHOLD = 0.6

def open_phone_link():
    """Open Phone Link app."""
    os.system("start ms-phone:")
    time.sleep(5)  

def call_best_friend():
    """Automate searching and calling best friend."""
    print("Opening Phone Link...")
    open_phone_link()

    print("Typing your best friend's name...")
    pyautogui.write(BEST_FRIEND_NAME, interval=0.1)
    time.sleep(2)

  
    pyautogui.press('enter')
    time.sleep(3)

    print("Pressing call button...")
    # Press Tab and Enter to reach call button (may vary by layout)
    for _ in range(3):
        pyautogui.press('tab')
        time.sleep(0.2)
    pyautogui.press('enter')

    print(f"📞 Calling {BEST_FRIEND_NAME}...")

sad_start_time = None

print("Monitoring sadness... Press 'q' to quit.")
while True:
    ret, frame = cap.read()
    if not ret:
        break

    dominant_emotion, score = (None, 0.0)
    try:
        dominant_emotion, score = detector.top_emotion(frame)
    except Exception:
        pass

    if dominant_emotion:
        cv2.putText(frame, f"{dominant_emotion}: {score:.2f}", (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Sadness Auto Call", frame)

    if dominant_emotion == "sad" and score >= SAD_CONFIDENCE_THRESHOLD:
        if sad_start_time is None:
            sad_start_time = time.time()
        else:
            elapsed = time.time() - sad_start_time
            print(f"Sad for {elapsed:.1f}s...")
            if elapsed >= SAD_DURATION_THRESHOLD:
                print("Detected sustained sadness 😢 — Calling your best friend...")
                call_best_friend()
                sad_start_time = None
    else:
        sad_start_time = None

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
