from gpiozero import LED
from time import sleep

# GPIO 핀 설정
led1 = LED(16)
led2 = LED(20)
led3 = LED(21)

try:
    while True:
        # LED ON
        led1.on()
        led2.on()
        led3.on()
        sleep(0.1)

        # LED OFF
        led1.off()
        led2.off()
        led3.off()
        sleep(0.1)

except KeyboardInterrupt:
    pass

# 프로그램 종료 시 LED OFF
led1.off()
led2.off()
led3.off()