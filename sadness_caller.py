import cv2
import time
import os
from fer import FER

detector = FER(mtcnn=True)
cap = cv2.VideoCapture(0)

print("Monitoring sadness... Press 'q' to quit.")

sad_start_time = None
SAD_DURATION_THRESHOLD = 2  # seconds before triggering Phone Link

SAD_CONFIDENCE_THRESHOLD = 0.2  # emotion confidence required

while True:
    ret, frame = cap.read()
    if not ret:
        break

    result = detector.detect_emotions(frame)
    dominant_emotion, score = detector.top_emotion(frame)

    # show emotion on screen
    cv2.putText(frame, f"{dominant_emotion}: {score:.2f}", (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Sadness Monitor", frame)

    if dominant_emotion == "sad" and score >= SAD_CONFIDENCE_THRESHOLD:
        if sad_start_time is None:
            sad_start_time = time.time()
        else:
            elapsed = time.time() - sad_start_time
            print(f"Sad for {elapsed:.1f}s...")
            if elapsed >= SAD_DURATION_THRESHOLD:
                print("Detected sustained sadness 😢 — Opening Phone Link...")
                # Open Phone Link calls page (Windows 11+)
                os.system("start ms-phone:")
                time.sleep(5)
                print("Phone Link opened! You can call your best friend ❤️")
                sad_start_time = None
    else:
        sad_start_time = None

    # press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
