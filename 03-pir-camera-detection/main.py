from gpiozero import MotionSensor    # PIR 모션 센서 제어 클래스
import time                          # 시간 지연
from picamera2 import Picamera2      # 라즈베리파이 카메라 제어 라이브러리
import datetime                      # 날짜 및 시간 처리

pirPin = MotionSensor(16)            # GPIO 16번 핀에 PIR 센서 연결

# -------------------------------
# 📷 카메라 초기화 및 설정
# -------------------------------

picam2 = Picamera2()  
# Picamera2 객체 생성 (카메라 장치 제어를 위한 인스턴스)

camera_config = picam2.create_preview_configuration()  
# 프리뷰(미리보기)용 기본 설정 생성
# 해상도, 포맷 등의 기본값이 포함된 설정 객체를 반환

picam2.configure(camera_config)  
# 생성한 설정을 카메라에 적용
# 이 과정을 통해 카메라 동작 모드가 결정됨

picam2.start()  
# 카메라 스트리밍 시작 (센서 활성화)
# 이 이후부터 사진 촬영 가능 상태가 됨

# -------------------------------
# 메인 루프
# -------------------------------

try:
    while True:
        try:
            sensorValue = pirPin.value   # PIR 센서 값 읽기

            if sensorValue == 1:         # 움직임 감지 시
                now = datetime.datetime.now()   # 현재 시간 획득
                print(now)                      # 감지 시간 출력

                # 파일명 생성 (날짜_시간 기반)
                fileName = now.strftime('%y-%m-%d_%H-%M-%S')

                # 사진 촬영 및 파일 저장
                picam2.capture_file(fileName + '.jpg')

                time.sleep(0.5)          # 연속 촬영 방지

        except:
            pass                         # 촬영 중 오류 발생 시 무시

except KeyboardInterrupt:
    pass                                 # Ctrl + C 입력 시 종료