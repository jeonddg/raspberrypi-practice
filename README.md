# Raspberry Pi Practice

라즈베리파이를 활용한 GPIO 제어 및 IoT 실습을 정리한 저장소입니다.  
다양한 하드웨어 제어 및 API 연동 실습을 통해 임베디드 시스템과 IoT 구조를 학습합니다.

---

## Overview

- GPIO 기반 하드웨어 제어 실습
- 센서 및 액추에이터 인터페이스 구현
- 웹 기반 제어 시스템 구현 (Flask)
- API 기반 데이터 수집 및 GUI 시각화
- IoT 시스템 기초 구조 이해

---

## Development Environment

- **Board** : Raspberry Pi 5  
- **OS** : Raspberry Pi OS  
- **Language** : Python 3  
- **Library** : gpiozero, Flask, tkinter  

---

## Projects

| No | Project | Description |
|----|--------|------------|
| 00 | GPIO LED Beacon | LED 3개를 이용한 경광등 제어 |
| 01 | GPIO Traffic Light | 자동차 및 보행자 신호 제어 |
| 02 | GPIO Gas Detector | MQ-2 센서 기반 가스/연기 감지 시스템 |
| 03 | PIR Camera Detection | PIR 센서 기반 침입자 감지 및 사진 촬영 시스템 |
| 04 | Flask LED Control | Flask 웹 서버를 이용한 LED 원격 제어 시스템 |
| 05 | Weather GUI API | OpenWeatherMap API 기반 온습도 GUI 표시 시스템 |

> 지속적으로 실습 프로젝트 추가 예정

---

## Repository Structure

```
raspberrypi-practice
│
├─ 00-gpio-led-beacon
│   ├─ main.py
│   └─ README.md
│
├─ 01-gpio-traffic-light
│   ├─ main_v1.py
│   ├─ main_v2.py
│   └─ README.md
│
├─ 02-gas-detector
│   ├─ main.py
│   └─ README.md
│
├─ 03-pir-camera-detection
│   ├─ main.py
│   └─ README.md
│
├─ 04-flask-led-control
│   ├─ main.py
│   ├─ templates
│   │   └─ index.html
│   └─ README.md
│
├─ 05-weather-gui-api
│   ├─ main.py
│   └─ README.md
│
└─ README.md
```

---

## Key Learning

- GPIO 입력/출력 제어
- 상태 기반 제어 (State Machine)
- 센서 기반 이벤트 처리
- 웹 기반 제어 시스템 (Flask)
- API 기반 데이터 수집 (OpenWeatherMap)
- JSON 데이터 파싱 및 활용
- GUI 프로그램 설계 (Tkinter)
- 하드웨어와 소프트웨어 연동 구조 이해

---

## Author

전동규  
Hanshin University