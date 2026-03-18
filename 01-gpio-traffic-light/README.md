# 01 - GPIO Traffic Light

라즈베리파이 GPIO를 이용하여 자동차 신호등과 보행자 신호등을 구현하였다.

---

## Overview

- GPIO 기반 다중 LED 제어
- 자동차 / 보행자 신호 흐름 구현
- 상태 기반 제어 구조 적용

---

## Hardware

- Raspberry Pi 5
- LED (Red ×2, Yellow ×1, Green ×2)
- 330Ω Resistor ×5
- Breadboard
- Jumper Cable

---

## Software

- Python 3
- gpiozero

---

## GPIO Mapping

| 기능 | GPIO |
|------|------|
| Car Red | GPIO2 |
| Car Yellow | GPIO3 |
| Car Green | GPIO4 |
| Human Red | GPIO20 |
| Human Green | GPIO21 |

---

## Execution

```bash
python main_v1.py
python main_v2.py
```

---

## Description

- 시간 기반으로 자동차 및 보행자 신호를 순차적으로 제어
- 각 상태는 일정 시간 유지 후 다음 상태로 전이

---

## Code Comparison

- main_v1.py : LED 개별 제어 방식
- main_v2.py : LEDBoard를 이용한 그룹 제어 방식

---

## Key Learning

- GPIO 다중 출력 제어
- 상태 기반 제어(State Machine) 개념 이해
- 코드 구조 개선 (개별 제어 vs 그룹 제어)


