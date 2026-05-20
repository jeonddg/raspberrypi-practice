# [09] Raspberry Pi 5 OpenCV Practice - Drowsiness Alert System

라즈베리파이와 OpenCV를 활용하여 얼굴 및 눈을 탐지하고,  
눈 감김 상태를 기준으로 부저를 제어하는 졸음방지 시스템을 구현한 프로젝트입니다.

눈이 정상적으로 감지되면 부저가 꺼지고,  
눈이 감기거나 제대로 감지되지 않으면 경고음을 출력하도록 구성하였습니다.

---

## Video

https://www.youtube.com/watch?v=BwXGbZI_S9Y

---

## Hardware

- Raspberry Pi 5
- USB Webcam
- Active Buzzer
- Breadboard
- Jumper Wires

---

## Software

- Python 3.x
- OpenCV
- gpiozero

---

## System Overview

- 웹캠을 통해 실시간 영상 입력
- OpenCV Haar Cascade를 이용한 얼굴 탐지
- 얼굴 영역 내부에서 눈 탐지 수행
- 눈 개수 기준 졸음 여부 판단
- 졸음 상태 시 부저 ON
- 정상 상태 시 부저 OFF

---

## GPIO Pin Configuration

| Device | GPIO Pin |
|---|---|
| Active Buzzer (+) | GPIO 16 |
| Active Buzzer (-) | GND |

---

## Key Concepts

- OpenCV Image Processing
- Haar Cascade Face Detection
- Eye Detection
- Real-time Video Processing
- GPIO Buzzer Control
- AIoT Monitoring System

---

## Source Code

```python
import cv2
from gpiozero import Buzzer

buzzerPin = Buzzer(16)

faceCascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

eyeCascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_eye.xml'
)

cap = cv2.VideoCapture(-1)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray)

    for (x, y, w, h) in faces:

        roi_gray = gray[y:y+h, x:x+w]

        eyes = eyeCascade.detectMultiScale(roi_gray)

        if len(eyes) >= 2:
            buzzerPin.off()
        else:
            buzzerPin.on()

    cv2.imshow("result", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

buzzerPin.off()
cap.release()
cv2.destroyAllWindows()
```

---

## Future Improvements

- Eye Aspect Ratio(EAR) 기반 정확도 향상
- 딥러닝 기반 얼굴/눈 탐지 적용
- 졸음 지속 시간 측정 기능 추가
- 차량 운전자 경고 시스템 확장
- MQTT 기반 원격 모니터링 시스템 추가

---

## Project Structure

```text
09-opencv-drowsiness-alert
│
├─ main.py
└─ README.md
```

---

## What I Learned

- OpenCV 기반 영상 처리 구조 이해
- Haar Cascade 얼굴/눈 탐지 구현
- 실시간 프레임 처리 방식 이해
- GPIO 기반 부저 제어
- 컴퓨터 비전과 하드웨어 제어 통합 방법 이해