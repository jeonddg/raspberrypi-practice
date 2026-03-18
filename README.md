# Raspberry Pi Practice

라즈베리파이를 활용한 GPIO 제어 및 IoT 실습을 정리한 저장소입니다.  
다양한 하드웨어 제어 실습을 통해 임베디드 시스템의 동작 원리와 구조를 학습합니다.

---

## Overview

- GPIO 기반 하드웨어 제어 실습
- 센서 및 액추에이터 인터페이스 구현
- IoT 시스템 기초 구조 이해

---

## Development Environment

- **Board** : Raspberry Pi 5  
- **OS** : Raspberry Pi OS  
- **Language** : Python 3  
- **Library** : gpiozero  

---

## Projects

| No | Project | Description |
|----|--------|------------|
| 00 | GPIO LED Beacon | LED 3개를 이용한 경광등 제어 |
| 01 | GPIO Traffic Light | 자동차 및 보행자 신호 제어 |

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
└─ README.md
```

---

## Key Learning

- GPIO 입력/출력 제어
- 상태 기반 제어(State Machine)
- 하드웨어와 소프트웨어 연동 구조 이해

---

## Author

전동규  
Hanshin University