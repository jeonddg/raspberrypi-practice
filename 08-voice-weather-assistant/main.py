import speech_recognition as sr          # 음성 인식(STT) 라이브러리
import requests                          # API 요청 라이브러리
import json                              # JSON 데이터 처리 라이브러리
import os                                # 운영체제 명령 실행 라이브러리

API_KEY = "Enter your API key here"
# OpenWeatherMap에서 발급받은 API Key 입력

recognizer = sr.Recognizer()
# 음성 인식 객체 생성

mic = sr.Microphone()
# 기본 마이크 장치 객체 생성


def get_weather():
    # OpenWeatherMap API를 이용하여 서울의 현재 날씨 정보를 가져오는 함수

    url = f"https://api.openweathermap.org/data/2.5/weather?q=Seoul&appid={API_KEY}&units=metric"

    response = requests.get(url)
    # API 서버로 GET 요청 전송

    data = json.loads(response.text)
    # JSON 문자열 데이터를 Python 딕셔너리 형태로 변환

    temp = data["main"]["temp"]
    # 현재 기온 값 추출

    humidity = data["main"]["humidity"]
    # 현재 습도 값 추출

    text = f"현재 서울의 기온은 {temp}도이고 습도는 {humidity}퍼센트입니다."
    # 출력할 문자열 생성

    return text


while True:
    try:
        with mic as source:
            # 마이크 장치를 음성 입력 소스로 사용

            print("음성을 입력하세요...")
            
            recognizer.adjust_for_ambient_noise(source)
            # 주변 소음을 분석하여 노이즈 보정 수행

            audio = recognizer.listen(source)
            # 마이크 음성 데이터 수집

        text = recognizer.recognize_google(audio, language='ko-KR')
        # Google Speech Recognition API를 이용하여 음성을 텍스트로 변환

        print("인식 결과 :", text)

        if "날씨" in text:
            # 사용자의 음성에 '날씨' 키워드가 포함된 경우

            result = get_weather()
            # 현재 날씨 정보 가져오기

            print(result)

            os.system(f'espeak -v ko "{result}"')
            # espeak를 사용하여 문자열을 한국어 음성으로 출력

    except sr.UnknownValueError:
        # 음성을 제대로 인식하지 못한 경우

        print("음성을 인식하지 못했습니다.")

    except sr.RequestError:
        # Google STT 서버 연결 오류 발생 시

        print("Google Speech Recognition 서비스 연결 실패")

    except KeyboardInterrupt:
        # Ctrl + C 입력 시 프로그램 종료

        print("프로그램 종료")
        break