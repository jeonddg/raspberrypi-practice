# [03] Raspberry Pi 5 GPIO Practice - Intruder Detection with PIR Sensor

라즈베리파이 GPIO를 활용하여 PIR 인체 감지 센서와 카메라를 이용한 침입자 감지 시스템을 구현한 프로젝트입니다.

움직임이 감지되면 현재 시간을 기준으로 사진을 촬영하여 저장하고, 감지되지 않을 경우에는 대기 상태를 유지하도록 구성하였습니다.

---

## Video

유튜브 링크

---

## Hardware

- Raspberry Pi 5
- PIR Motion Sensor
- Raspberry Pi Camera Module
- Breadboard
- Jumper Wires

---

## Software

- Python 3.x
- gpiozero library
- picamera2 library

---

## System Overview

- PIR 센서를 통해 움직임(인체) 감지
- 감지 시 현재 시간 기반 파일명 생성
- 카메라를 이용하여 사진 촬영 및 저장
- 일정 시간 딜레이로 연속 촬영 방지

---

## GPIO Pin Configuration

| Device      | GPIO Pin |
|-------------|----------|
| PIR Sensor  | GPIO 16  |

---

## Key Concepts

- Motion Detection (PIR Sensor)
- Event-driven System
- Camera Control (Picamera2)
- Real-time Monitoring

---

## Source Code

```python
from gpiozero import MotionSensor
import time
from picamera2 import Picamera2
import datetime

pirPin = MotionSensor(16)

# Camera setup
picam2 = Picamera2()
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)
picam2.start()

try:
    while True:
        try:
            sensorValue = pirPin.value

            if sensorValue == 1:
                now = datetime.datetime.now()
                print(now)

                fileName = now.strftime('%y-%m-%d_%H-%M-%S')
                picam2.capture_file(fileName + '.jpg')

                time.sleep(0.5)

        except:
            pass

except KeyboardInterrupt:
    pass
```

---

## Future Improvements

- 영상 녹화 기능 추가
- 얼굴 인식 기반 보안 시스템
- IoT (MQTT) 연동
- 모바일 알림 시스템 구현

---

## Project Structure

```
03-pir-camera-detection
│
├─ main.py
└─ README.md
```

---

## What I Learned

- PIR 센서를 이용한 움직임 감지 구조 이해
- 이벤트 기반 제어 시스템 구현
- 카메라 모듈을 활용한 이미지 캡처
- GPIO를 이용한 실시간 시스템 설계