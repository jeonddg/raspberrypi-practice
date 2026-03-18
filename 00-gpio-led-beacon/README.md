# 00 - GPIO LED Beacon

라즈베리파이 GPIO를 이용하여 LED 3개를 동시에 제어하고,
주기적으로 점등/소등을 반복하는 경광등(Beacon) 패턴을 구현하였다.

---

## Overview

- GPIO 출력 제어 기초 학습
- LED를 활용한 간단한 임베디드 제어 구현
- 반복문과 시간 지연을 이용한 패턴 제어

---

## Hardware

- Raspberry Pi 5
- Breadboard
- LED (Red) × 3
- 220Ω Resistor × 3
- Jumper Cable

---

## Software

- Python 3
- gpiozero

---

## GPIO Mapping

| LED | GPIO Pin |
|-----|--------|
| LED1 | GPIO16 |
| LED2 | GPIO20 |
| LED3 | GPIO21 |

각 LED는 220Ω 저항과 직렬로 연결하여 사용하였다.

---

## Execution

```bash
python main.py