import urllib.request
# OpenWeatherMap API에 HTTP 요청을 보내기 위한 라이브러리

import json
# API 응답으로 받은 JSON 데이터를 Python 딕셔너리로 변환하기 위한 라이브러리

import datetime
# 현재 날짜와 시간을 확인하기 위한 라이브러리

import asyncio
# 비동기 실행을 위한 라이브러리
# python-telegram-bot 20버전 이상에서는 메시지 전송에 async/await 구조를 사용한다.

from telegram import Bot
# 텔레그램 Bot 객체를 사용하기 위한 클래스


# 메시지를 받을 텔레그램 채팅 ID
# 본인의 chat_id로 변경해야 한다.
telegram_id = 'Enter your chat ID here'

# BotFather에서 발급받은 텔레그램 봇 토큰
# 본인의 bot token으로 변경해야 한다.
my_token = 'Enter your bot token here'

# OpenWeatherMap에서 발급받은 API Key
# 본인의 API Key로 변경해야 한다.
api_key = 'Enter your API key here'


# 텔레그램 봇 객체 생성
# 이후 bot.send_message()를 이용해 메시지를 전송할 수 있다.
bot = Bot(token=my_token)


# 3시간 간격으로 알림을 보낼 정각 시간 목록
# 예: 7시, 10시, 13시, 16시, 19시, 22시에 알림 전송
ALERT_HOURS = [7, 10, 13, 16, 19, 22]

# 추가로 알림을 보낼 특정 시간 목록
# 실험할 때 현재 시간 기준 1분 뒤를 넣어 테스트하기 좋다.
ALERT_TIMES = ["08:30", "14:45"]


def getWeather():
    """
    OpenWeatherMap API를 호출하여
    서울의 24시간 날씨 예보 데이터를 가져오고,
    시간, 기온, 습도, 날씨 설명을 문자열로 가공하여 반환하는 함수
    """

    # OpenWeatherMap 5일/3시간 예보 API 요청 URL
    # q=Seoul        → 서울 날씨 요청
    # appid=api_key  → API 인증 키 사용
    # units=metric   → 섭씨 단위 사용
    # lang=en        → 날씨 설명을 영어로 받음
    # cnt=8          → 3시간 간격 데이터 8개, 즉 약 24시간 예보 요청
    url = (
        f"https://api.openweathermap.org/data/2.5/forecast"
        f"?q=Seoul&appid={api_key}&units=metric&lang=en&cnt=8"
    )

    # API 서버에 요청을 보내고 응답을 받는다.
    with urllib.request.urlopen(url) as r:
        # 응답 데이터는 JSON 형식이므로 Python 딕셔너리로 변환한다.
        data = json.loads(r.read())

    # 텔레그램으로 전송할 결과 문자열 초기화
    text = ""

    # data['list']에는 3시간 간격의 날씨 예보 데이터가 들어있다.
    # cnt=8로 요청했기 때문에 8개 시간대의 데이터를 순회한다.
    for i in range(8):
        item = data['list'][i]

        # dt_txt에서 시간 부분만 추출한다.
        # OpenWeatherMap의 시간은 UTC 기준이므로 +9를 하여 한국 시간(KST)으로 변환한다.
        # zfill(2)는 한 자리 숫자일 경우 앞에 0을 붙여 두 자리로 만든다.
        hour = str((int(item['dt_txt'][11:13]) + 9) % 24).zfill(2)

        # main 객체에서 기온 추출
        temp = item['main']['temp']

        # main 객체에서 습도 추출
        humi = item['main']['humidity']

        # weather 리스트의 첫 번째 요소에서 날씨 설명 추출
        desc = item['weather'][0]['description']

        # 한 시간대의 날씨 정보를 보기 좋은 형태로 문자열에 추가
        text += f"({hour}h {temp}C {humi}% {desc})\n"

    # 완성된 날씨 예보 문자열 반환
    return text


async def main():
    """
    현재 시간을 반복적으로 확인하다가
    설정한 알림 시간에 도달하면 날씨 정보를 가져와
    텔레그램으로 전송하는 비동기 메인 함수
    """

    try:
        while True:
            # 현재 날짜와 시간 가져오기
            now = datetime.datetime.now()

            # 현재 시간을 "시:분" 형태 문자열로 변환
            # 예: 08:30
            hm = now.strftime('%H:%M')

            # 정각 알림 조건 확인
            # 현재 시간이 ALERT_HOURS 목록에 있고, 분과 초가 모두 0이면 True
            is_alert_hour = (
                now.hour in ALERT_HOURS
                and now.minute == 0
                and now.second == 0
            )

            # 지정 시간 알림 조건 확인
            # 현재 시:분이 ALERT_TIMES 목록에 있고, 초가 0이면 True
            is_alert_time = (
                hm in ALERT_TIMES
                and now.second == 0
            )

            # 정각 알림 조건 또는 지정 시간 알림 조건 중 하나라도 만족하면 메시지 전송
            if is_alert_hour or is_alert_time:
                # OpenWeatherMap API에서 날씨 정보를 가져와 문자열로 가공
                msg = getWeather()

                # 터미널에 전송할 메시지 출력
                print(msg)

                # 텔레그램으로 메시지 전송
                await bot.send_message(chat_id=telegram_id, text=msg)

            # 1초마다 현재 시간을 확인
            await asyncio.sleep(1)

    except KeyboardInterrupt:
        # Ctrl + C 입력 시 프로그램 정상 종료
        pass


# 비동기 메인 함수 실행
asyncio.run(main())