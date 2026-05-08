import paho.mqtt.client as mqtt      # MQTT 통신 라이브러리
from gpiozero import LED             # GPIO LED 제어 라이브러리
import threading                     # 스레드(동시 처리) 라이브러리
import time                          # 시간 제어 라이브러리


# GPIO 핀에 연결된 LED 객체 생성
green_led = LED(16)                  # 초록 LED → GPIO 16
blue_led = LED(20)                   # 파랑 LED → GPIO 20
red_led = LED(21)                    # 빨강 LED → GPIO 21


# MQTT 브로커 주소 설정
# 자신의 라즈베리파이 IP 주소 입력
broker_address = "192.168.0.10"


# MQTT 클라이언트 객체 생성
client = mqtt.Client()


# MQTT 메시지 수신 시 자동 실행되는 콜백 함수
def on_message(client, userdata, msg):

    # 수신된 payload 데이터를 문자열로 변환
    data = msg.payload.decode()

    # 수신된 메시지 출력
    print(data)

    # 초록 LED ON
    if data == "green_on":
        green_led.on()

    # 초록 LED OFF
    elif data == "green_off":
        green_led.off()

    # 파랑 LED ON
    elif data == "blue_on":
        blue_led.on()

    # 파랑 LED OFF
    elif data == "blue_off":
        blue_led.off()

    # 빨강 LED ON
    elif data == "red_on":
        red_led.on()

    # 빨강 LED OFF
    elif data == "red_off":
        red_led.off()


# 별도의 스레드에서 실행될 함수
# hello 토픽으로 숫자 데이터를 계속 발행
def send_thread():

    count = 1

    while True:

        # hello 토픽으로 count 값 발행
        client.publish("hello", count)

        # 현재 값 출력
        print(count)

        # 숫자 증가
        count += 1

        # 1초 대기
        time.sleep(1)


# 메시지 수신 시 실행할 콜백 함수 등록
client.on_message = on_message


# MQTT 브로커 연결
client.connect(broker_address)


# led 토픽 구독
# QoS = 1
client.subscribe("led", 1)


# send_thread 함수를 별도 스레드로 실행
thread = threading.Thread(target=send_thread)

# 스레드 시작
thread.start()


# MQTT 메시지 무한 대기
# 계속해서 메시지를 수신
client.loop_forever()