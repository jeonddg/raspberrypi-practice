# [07] Raspberry Pi 5 MQTT Practice - Bidirectional LED Control System

라즈베리파이와 MQTT 통신을 이용하여 양방향 LED 제어 시스템을 구현한 프로젝트입니다.

Mosquitto MQTT 브로커를 기반으로  
PC(MQTT.fx)와 라즈베리파이 간에 메시지를 송수신하며,  
LED 제어와 데이터 발행을 동시에 수행하도록 구성하였습니다.

또한 Python의 threading 기법을 사용하여  
하나의 프로그램에서 여러 작업을 동시에 처리하는 구조를 구현하였습니다.

---

# Video

https://www.youtube.com/watch?v=SGlDwfLpHvo

---

# Hardware

- Raspberry Pi 5
- Breadboard
- Red LED
- Green LED
- Blue LED
- 330Ω Resistors
- Jumper Wires

---

# Software

- Python 3.x
- Mosquitto MQTT Broker
- paho-mqtt
- gpiozero
- threading
- MQTT.fx

---

# System Overview

- MQTT Publish / Subscribe 구조 사용
- PC에서 LED 제어 명령 발행
- 라즈베리파이에서 LED 제어 수행
- hello 토픽으로 숫자 데이터 주기적 발행
- threading 기반 동시 처리 구현

---

# MQTT Topic Structure

| Topic | Description |
|------|-------------|
| led | LED 제어 명령 |
| hello | 숫자 데이터 전송 |

---

# GPIO Pin Configuration

| Device | GPIO Pin |
|------|----------|
| Green LED | GPIO 16 |
| Blue LED | GPIO 20 |
| Red LED | GPIO 21 |

---

# Source Code

```python
import paho.mqtt.client as mqtt
from gpiozero import LED
import threading
import time

green_led = LED(16)
blue_led = LED(20)
red_led = LED(21)

broker_address = "192.168.0.10"

client = mqtt.Client()

def on_message(client, userdata, msg):

    data = msg.payload.decode()

    print(data)

    if data == "green_on":
        green_led.on()

    elif data == "green_off":
        green_led.off()

    elif data == "blue_on":
        blue_led.on()

    elif data == "blue_off":
        blue_led.off()

    elif data == "red_on":
        red_led.on()

    elif data == "red_off":
        red_led.off()


def send_thread():

    count = 1

    while True:

        client.publish("hello", count)

        print(count)

        count += 1

        time.sleep(1)


client.on_message = on_message

client.connect(broker_address)

client.subscribe("led", 1)

thread = threading.Thread(target=send_thread)

thread.start()

client.loop_forever()
```

---

# Key Concepts

- MQTT Publish / Subscribe
- MQTT Broker
- GPIO LED Control
- Bidirectional Communication
- Threading
- Concurrent Processing
- Real-time Message Transfer

---

# Future Improvements

- 센서 데이터 MQTT 연동
- 모바일 앱 제어 기능 추가
- 웹 기반 MQTT 대시보드 구현
- JSON 데이터 구조 적용

---

# Project Structure

```text
07-mqtt-led-control
│
├─ main.py
└─ README.md
```

---

# What I Learned

- MQTT 기반 IoT 통신 구조 이해
- Publish / Subscribe 메시지 흐름 학습
- GPIO 기반 LED 제어
- Python threading 기반 동시 처리
- 실시간 양방향 데이터 통신 구현