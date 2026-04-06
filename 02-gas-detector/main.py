from gpiozero import DigitalInputDevice   # 디지털 입력(GPIO 핀 상태 읽기용)
from gpiozero import OutputDevice         # 디지털 출력(GPIO 핀 제어용)
import time                               # 딜레이(시간 제어)

bz  = OutputDevice(18)                    # GPIO18 → 부저 출력 핀 (ON/OFF 제어)
gas = DigitalInputDevice(17)              # GPIO17 → 가스 센서 DO(디지털 출력) 입력

try:
    while True:
        # MQ-2 센서는 가스 감지 시 LOW(0), 평상시 HIGH(1) 출력
        if gas.value == 0:                # LOW → 가스 감지됨
            print("Gas Detected")
            bz.on()                       # 부저 울림 (경고)
        else:                             # HIGH → 정상 상태
            print("No gas Detected")
            bz.off()                      # 부저 정지

        time.sleep(0.2)                   # 센서 상태를 0.2초마다 반복 체크

except KeyboardInterrupt:
    pass                                  # Ctrl+C로 종료 시 예외 처리

bz.off()                                  # 프로그램 종료 시 부저 OFF (안전 처리).