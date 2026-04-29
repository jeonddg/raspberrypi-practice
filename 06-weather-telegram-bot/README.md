# [06] Raspberry Pi 5 IoT Practice - Weather Telegram Bot

OpenWeatherMap API를 활용하여 서울의 날씨 예보 데이터를 가져오고,  
텔레그램 봇을 통해 사용자에게 자동으로 일기예보 메시지를 전송하는 프로젝트입니다.

Python 프로그램이 설정된 알림 시간을 반복적으로 확인하고,  
해당 시간이 되면 OpenWeatherMap API에서 24시간 예보 데이터를 가져와  
텔레그램 메시지로 전송하도록 구성하였습니다.

---

## Video

https://www.youtube.com/watch?v=aV4Ci8kZJao

---

## Hardware

- Raspberry Pi 5

---

## Software

- Python 3.x
- OpenWeatherMap API
- python-telegram-bot
- urllib
- json
- datetime
- asyncio

---

## System Overview

- OpenWeatherMap API Key 발급
- Telegram BotFather를 통한 봇 생성
- Telegram Bot Token 및 chat_id 설정
- OpenWeatherMap API로 서울 날씨 예보 데이터 요청
- JSON 데이터에서 시간, 기온, 습도, 날씨 설명 추출
- 설정된 시간에 텔레그램 메시지 자동 전송

---

## Message Flow

1. Python 프로그램 실행
2. 현재 시간 확인
3. 설정된 알림 시간인지 판단
4. OpenWeatherMap API에 날씨 데이터 요청
5. JSON 응답 데이터 파싱
6. 날씨 정보를 문자열로 가공
7. Telegram Bot API를 통해 사용자에게 메시지 전송

---

## API Settings

이 프로젝트는 OpenWeatherMap API를 사용합니다.

코드의 아래 부분에 본인의 API Key를 입력해야 합니다.

```python
api_key = 'Enter your API key here'
```

---

## Telegram Settings

텔레그램 메시지를 전송하기 위해서는 BotFather에서 발급받은 Bot Token과  
메시지를 받을 대상의 chat_id가 필요합니다.

```python
telegram_id = 'Enter your chat ID here'
my_token = 'Enter your bot token here'
```

---

## Alert Time Settings

기본적으로 3시간 간격의 정각 알림을 설정할 수 있습니다.

```python
ALERT_HOURS = [7, 10, 13, 16, 19, 22]
```

추가 테스트용 알림 시간은 아래 리스트에 직접 입력할 수 있습니다.

```python
ALERT_TIMES = ["08:30", "14:45"]
```

---

## Key Concepts

- OpenWeatherMap API
- Telegram Bot API
- API Key Authentication
- JSON Parsing
- Async Programming
- Scheduled Notification System
- IoT Alert System

---

## Source Code

```python
import urllib.request
import json
import datetime
import asyncio
from telegram import Bot

telegram_id = 'Enter your chat ID here'
my_token = 'Enter your bot token here'
api_key = 'Enter your API key here'

bot = Bot(token=my_token)

ALERT_HOURS = [7, 10, 13, 16, 19, 22]
ALERT_TIMES = ["08:30", "14:45"]


def getWeather():
    url = (
        f"https://api.openweathermap.org/data/2.5/forecast"
        f"?q=Seoul&appid={api_key}&units=metric&lang=en&cnt=8"
    )

    with urllib.request.urlopen(url) as r:
        data = json.loads(r.read())

    text = ""

    for i in range(8):
        item = data['list'][i]
        hour = str((int(item['dt_txt'][11:13]) + 9) % 24).zfill(2)
        temp = item['main']['temp']
        humi = item['main']['humidity']
        desc = item['weather'][0]['description']

        text += f"({hour}h {temp}C {humi}% {desc})\n"

    return text


async def main():
    try:
        while True:
            now = datetime.datetime.now()
            hm = now.strftime('%H:%M')

            is_alert_hour = (
                now.hour in ALERT_HOURS
                and now.minute == 0
                and now.second == 0
            )

            is_alert_time = (
                hm in ALERT_TIMES
                and now.second == 0
            )

            if is_alert_hour or is_alert_time:
                msg = getWeather()
                print(msg)
                await bot.send_message(chat_id=telegram_id, text=msg)

            await asyncio.sleep(1)

    except KeyboardInterrupt:
        pass


asyncio.run(main())
```

---

## Project Structure

```text
06-weather-telegram-bot
│
├─ main.py
└─ README.md
```

---

## Future Improvements

- 도시 선택 기능 추가
- 날씨 설명 한글화
- 강수 확률 및 풍속 정보 추가
- 에러 발생 시 예외 처리 강화
- 환경변수(.env)를 이용한 API Key 및 Token 관리
- 매일 아침 자동 알림 서비스로 확장

---

## What I Learned

- OpenWeatherMap API를 이용한 날씨 데이터 요청
- JSON 응답 데이터 파싱 방법
- Telegram Bot API를 활용한 메시지 전송
- asyncio 기반 비동기 처리 구조
- 시간 조건 기반 자동 알림 시스템 구현