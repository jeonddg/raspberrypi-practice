# [05] Raspberry Pi 5 Python Practice - Weather GUI with OpenWeatherMap API

OpenWeatherMap API를 활용하여 서울의 현재 온도와 습도를 가져오고,  
Python Tkinter GUI 창에 실시간으로 표시하는 프로그램입니다.

API 요청을 통해 JSON 형식의 날씨 데이터를 받아오고,  
해당 데이터에서 온도와 습도 값을 추출하여 GUI 화면에 출력하도록 구성하였습니다.

---

## Video

https://www.youtube.com/watch?v=eMeI-fFabfY

---

## Hardware

- Raspberry Pi 5

---

## Software

- Python 3.x
- OpenWeatherMap API
- urllib
- json
- tkinter

---

## System Overview

- OpenWeatherMap API Key 발급
- API 요청 URL 생성
- 서울의 현재 날씨 데이터 수신
- JSON 데이터에서 온도와 습도 추출
- Tkinter GUI 화면에 온습도 표시
- 1분마다 자동 갱신

---

## API

이 프로젝트는 OpenWeatherMap API를 사용합니다.

API Key는 OpenWeatherMap 공식 웹사이트에서 발급받아야 하며,  
코드의 아래 부분에 본인의 API Key를 입력해야 합니다.

```python
API_KEY = "Enter your API key here"
```

---

## Key Concepts

- API Key 인증
- HTTP Request
- JSON Parsing
- Tkinter GUI
- Periodic Data Update
- IoT Data Visualization

---

## Source Code

```python
import urllib.request
import json
import tkinter
import tkinter.font

API_KEY = "Enter your API key here"

def tick1Min():
    url = f"https://api.openweathermap.org/data/2.5/weather?q=Seoul&appid={API_KEY}&units=metric"

    with urllib.request.urlopen(url) as r:
        data = json.loads(r.read())

    temp = data["main"]["temp"]
    humi = data["main"]["humidity"]

    label.config(text=f"{temp:.1f}C   {humi}%")

    window.after(60000, tick1Min)

window = tkinter.Tk()
window.title("TEMP HUMI DISPLAY")
window.geometry("400x100")
window.resizable(False, False)

font = tkinter.font.Font(size=30)
label = tkinter.Label(window, text="", font=font)
label.pack()

tick1Min()
window.mainloop()
```

---

## Project Structure

```text
05-weather-gui-api
│
├─ main.py
└─ README.md
```

---

## Future Improvements

- 도시 선택 기능 추가
- 날씨 상태 아이콘 표시
- 최저/최고 온도 표시
- 습도 기반 알림 기능 추가
- 센서 데이터와 API 데이터 비교 기능 구현

---

## What I Learned

- OpenWeatherMap API 사용 방법
- API Key 기반 데이터 요청 구조 이해
- JSON 데이터 파싱 방법
- Tkinter를 이용한 GUI 프로그램 구성
- 일정 시간마다 데이터를 갱신하는 구조 이해