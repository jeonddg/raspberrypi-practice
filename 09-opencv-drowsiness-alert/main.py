import cv2                                   # OpenCV 라이브러리
from gpiozero import Buzzer                  # GPIO 부저 제어 라이브러리

# GPIO 16번 핀에 연결된 능동부저 객체 생성
buzzerPin = Buzzer(16)

# OpenCV에서 제공하는 Haar Cascade 얼굴 탐지 모델 불러오기
faceCascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# OpenCV에서 제공하는 Haar Cascade 눈 탐지 모델 불러오기
eyeCascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_eye.xml'
)

# 웹캠 연결
# -1은 연결된 기본 카메라 자동 선택
cap = cv2.VideoCapture(-1)

# 카메라 해상도 설정
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

try:

    while True:
        # 웹캠 프레임 읽기
        ret, frame = cap.read()

        # 프레임 읽기 실패 시 반복문 종료
        if not ret:
            break

        # 컬러 이미지를 흑백 이미지로 변환
        # 얼굴 탐지 속도 향상 목적
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 얼굴 탐지 수행
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5
        )

        # 탐지된 얼굴 개수 출력
        print("face:", len(faces))

        # 탐지된 얼굴 반복 처리
        for (x, y, w, h) in faces:

            # 얼굴 영역에 파란색 사각형 표시
            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (255, 0, 0),
                2
            )

            # 얼굴 영역만 잘라내기
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

            # 얼굴 내부에서 눈 탐지
            eyes = eyeCascade.detectMultiScale(roi_gray)

            # 탐지된 눈 개수 출력
            print("eyes:", len(eyes))

            # 눈 영역에 초록색 사각형 표시
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(
                    roi_color,
                    (ex, ey),
                    (ex + ew, ey + eh),
                    (0, 255, 0),
                    2
                )

            # 눈이 2개 이상 감지되면 정상 상태
            if len(eyes) >= 2:
                buzzerPin.off()

            # 눈이 1개 이하이면 졸음 상태로 판단
            else:
                buzzerPin.on()

        # 결과 화면 출력
        cv2.imshow("result", frame)

        # q 키 입력 시 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    pass

# 종료 시 부저 OFF
buzzerPin.off()

# 카메라 해제
cap.release()

# OpenCV 창 종료
cv2.destroyAllWindows()