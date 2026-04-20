# [04] Raspberry Pi 5 GPIO Practice - Web-Based LED Control (Flask)

라즈베리파이 GPIO와 Flask 웹 서버를 이용하여 웹 브라우저에서 LED를 제어하는 시스템을 구현한 프로젝트입니다.

사용자가 웹 페이지에서 버튼을 클릭하면 서버로 요청이 전달되고, 해당 요청에 따라 GPIO 핀에 연결된 LED를 ON/OFF 할 수 있도록 구성하였습니다.

---

## Video

👉 여기에 유튜브 링크 넣기

---

## Hardware

- Raspberry Pi 5
- LED
- Resistor (220Ω or 330Ω)
- Breadboard
- Jumper Wires

---

## Software

- Python 3.x
- Flask
- gpiozero

---

## System Overview

- 웹 브라우저에서 LED ON/OFF 요청 전송
- Flask 서버에서 POST 요청 처리
- 요청 값에 따라 GPIO 핀 제어
- LED 상태를 실시간으로 변경

---

## GPIO Pin Configuration

| Device | GPIO Pin |
|--------|----------|
| LED    | GPIO 21  |

---

## Key Concepts

- Web Server (Flask)
- HTTP Request Handling (GET / POST)
- GPIO Digital Output Control
- Web-Based Embedded Control System

---

## Source Code

```python
from flask import Flask, render_template, request
from gpiozero import LED

app = Flask(__name__)
red_led = LED(21)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/data', methods=['POST'])
def data():
    data = request.form['led']

    if data == 'on':
        red_led.on()
    elif data == 'off':
        red_led.off()

    return home()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
```

---

## Project Structure

```
04-flask-led-control
│
├─ main.py
├─ templates
│   └─ index.html
└─ README.md
```

---

## Future Improvements

- LED 상태 표시 UI 추가
- 다중 LED 제어 기능
- 로그인 기반 접근 제어
- IoT (MQTT) 연동

---

## What I Learned

- Flask를 이용한 웹 서버 구축
- HTTP 요청 처리 방식 이해 (GET / POST)
- 웹과 GPIO 제어 연동
- 웹 기반 임베디드 시스템 구현