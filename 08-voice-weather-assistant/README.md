# [08] Voice Weather Assistant

라즈베리파이에서 Google Speech Recognition(STT), OpenWeatherMap API, 그리고 TTS(Text To Speech)를 활용하여 음성 기반 날씨 안내 시스템을 구현한 프로젝트입니다.

사용자가 마이크에 “날씨”라고 말하면 음성을 텍스트로 변환하고, 현재 서울의 기온 및 습도 정보를 가져와 스피커로 음성 출력하도록 구성하였습니다.

---

## Video

https://www.youtube.com/watch?v=XP68ltvX9q0

---

## Hardware

- Raspberry Pi 5
- USB Microphone
- Speaker

---

## Software

- Python 3.12
- SpeechRecognition
- PyAudio
- requests
- espeak
- OpenWeatherMap API

---

## System Overview

- 마이크를 통해 사용자 음성 입력
- Google Speech Recognition을 이용한 STT 처리
- “날씨” 키워드 인식
- OpenWeatherMap API를 이용한 현재 날씨 데이터 요청
- JSON 데이터 파싱
- espeak 기반 TTS 음성 출력

---

## Key Concepts

- Speech To Text (STT)
- Text To Speech (TTS)
- OpenWeatherMap API
- JSON Parsing
- 음성 기반 IoT 시스템
- API 기반 데이터 처리

---

## Source Code

```python
import speech_recognition as sr
import requests
import json
import os

API_KEY = "Enter your API key here"

recognizer = sr.Recognizer()
mic = sr.Microphone()

def get_weather():

    url = f"https://api.openweathermap.org/data/2.5/weather?q=Seoul&appid={API_KEY}&units=metric"

    response = requests.get(url)

    data = json.loads(response.text)

    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]

    text = f"현재 서울의 기온은 {temp}도이고 습도는 {humidity}퍼센트입니다."

    return text


while True:
    try:
        with mic as source:

            print("음성을 입력하세요...")

            recognizer.adjust_for_ambient_noise(source)

            audio = recognizer.listen(source)

        text = recognizer.recognize_google(audio, language='ko-KR')

        print("인식 결과 :", text)

        if "날씨" in text:

            result = get_weather()

            print(result)

            os.system(f'espeak -v ko "{result}"')

    except sr.UnknownValueError:

        print("음성을 인식하지 못했습니다.")

    except sr.RequestError:

        print("Google Speech Recognition 서비스 연결 실패")

    except KeyboardInterrupt:

        print("프로그램 종료")
        break
```

---

## Future Improvements

- 다양한 음성 명령 처리
- 지역별 날씨 검색 기능
- AI 챗봇 연동
- GUI 기반 음성 비서 시스템
- MQTT 기반 스마트홈 연동

---

## What I Learned

- Google Speech Recognition 기반 STT 처리 구조 이해
- OpenWeatherMap API 활용 방법 학습
- JSON 데이터 파싱 구조 이해
- espeak 기반 TTS 음성 출력 구조 학습
- 음성 기반 IoT 시스템 동작 원리 이해