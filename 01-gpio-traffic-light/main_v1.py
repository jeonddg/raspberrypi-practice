from gpiozero import LED   # LED 제어를 위한 gpiozero 라이브러리
from time import sleep     # 시간 지연 함수

# -------------------------------
# LED 객체 생성 (GPIO 핀 번호 지정)
# -------------------------------
carLedRed = LED(2)         # 자동차 신호등 - 빨강
carLedYellow = LED(3)      # 자동차 신호등 - 노랑
carLedGreen = LED(4)       # 자동차 신호등 - 초록

humanLedRed = LED(20)      # 보행자 신호등 - 빨강
humanLedGreen = LED(21)    # 보행자 신호등 - 초록

# -------------------------------
# 메인 동작 (무한 반복)
# -------------------------------
try:
    while True:

        # 1️. 자동차: 초록 / 보행자: 빨강
        carLedRed.value = 0
        carLedYellow.value = 0
        carLedGreen.value = 1

        humanLedRed.value = 1
        humanLedGreen.value = 0

        sleep(3.0)  # 3초 유지

        # 2️. 자동차: 노랑 / 보행자: 빨강
        carLedRed.value = 0
        carLedYellow.value = 1
        carLedGreen.value = 0

        humanLedRed.value = 1
        humanLedGreen.value = 0

        sleep(1.0)  # 1초 유지

        # 3️. 자동차: 빨강 / 보행자: 초록
        carLedRed.value = 1
        carLedYellow.value = 0
        carLedGreen.value = 0

        humanLedRed.value = 0
        humanLedGreen.value = 1

        sleep(3.0)  # 3초 유지

# -------------------------------
# Ctrl + C 입력 시 종료 처리
# -------------------------------
except KeyboardInterrupt:
    pass  # 에러 메시지 없이 종료

# -------------------------------
# 프로그램 종료 시 LED 모두 OFF
# -------------------------------
carLedRed.value = 0
carLedYellow.value = 0
carLedGreen.value = 0
humanLedRed.value = 0
humanLedGreen.value = 0