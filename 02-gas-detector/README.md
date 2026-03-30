# [02] Raspberry Pi 5 GPIO Practice - Gas/Smoke Detector

라즈베리파이 GPIO를 활용하여 **MQ-2 가스 센서와 능동부저를 이용한 가스/연기 감지 시스템**을 구현한 프로젝트입니다.

가스가 감지되면 부저가 울려 경고를 발생시키고, 정상 상태에서는 부저가 동작하지 않도록 구성하였습니다.

---

## Video

https://www.youtube.com/watch?v=mtqzYjezqSE

---

## Hardware

- Raspberry Pi 5
- MQ-2 Gas Sensor Module
- Active Buzzer
- Breadboard
- Jumper Wires

---

## Software

- Python 3.x
- gpiozero library

---

## System Overview

- MQ-2 센서를 통해 가스 감지 여부 확인
- 디지털 출력(DO)을 이용하여 상태 판별
- 가스 감지 시 부저 ON (경고)
- 정상 상태 시 부저 OFF

---

## GPIO Pin Configuration

| Device        | GPIO Pin |
|--------------|--------|
| Gas Sensor (DO) | GPIO 17 |
| Buzzer          | GPIO 18 |

---

## Key Concepts

- GPIO Digital Input / Output
- Sensor-Based Control System
- Active vs Passive Components
- Real-time Monitoring Loop

---

## Source Code

```python
from gpiozero import DigitalInputDevice
from gpiozero import OutputDevice
import time

bz  = OutputDevice(18)
gas = DigitalInputDevice(17)

try:
    while True:
        if gas.value == 0:
            print("Gas Detected")
            bz.on()
        else:
            print("No gas Detected")
            bz.off()

        time.sleep(0.2)

except KeyboardInterrupt:
    pass

bz.off()
```

---

## Future Improvements

- 아날로그(AO) 값 기반 농도 측정
- LED 경고 시스템 추가
- IoT (MQTT) 연동
- 모바일 알림 시스템 구현

---

## Project Structure

```
03-gas-detector
│
├─ main.py
└─ README.md
```

---

## What I Learned

- 센서 입력 기반 제어 구조 이해
- 디지털 신호 처리 (HIGH / LOW)
- 능동부저를 활용한 경고 시스템 구현
- GPIO를 이용한 실시간 반복 제어