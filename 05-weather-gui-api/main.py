import urllib.request          # OpenWeatherMap API에 HTTP 요청을 보내기 위한 라이브러리
import json                    # API 응답으로 받은 JSON 데이터를 Python 딕셔너리로 변환하기 위한 라이브러리
import tkinter                 # GUI 창을 만들기 위한 Python 기본 GUI 라이브러리
import tkinter.font            # Tkinter에서 폰트 크기와 스타일을 설정하기 위한 라이브러리

# OpenWeatherMap에서 발급받은 API Key 입력
# 실제 실행 시 "Enter your API key here" 부분을 본인의 API Key로 변경해야 한다.
API_KEY = "Enter your API key here"


def tick1Min():
    """
    OpenWeatherMap API를 호출하여 서울의 현재 온도와 습도를 가져오고,
    GUI 화면의 Label 내용을 갱신하는 함수
    """

    # 서울(Seoul)의 현재 날씨 정보를 요청하는 API URL
    # units=metric 옵션을 사용하여 온도를 섭씨(°C) 단위로 받는다.
    url = f"https://api.openweathermap.org/data/2.5/weather?q=Seoul&appid={API_KEY}&units=metric"

    # API 서버에 요청을 보내고 응답 데이터를 받는다.
    with urllib.request.urlopen(url) as r:
        # 응답 데이터는 JSON 형식이므로 Python 딕셔너리 형태로 변환한다.
        data = json.loads(r.read())

    # JSON 데이터의 main 객체에서 현재 온도 값을 가져온다.
    temp = data["main"]["temp"]

    # JSON 데이터의 main 객체에서 현재 습도 값을 가져온다.
    humi = data["main"]["humidity"]

    # GUI Label에 온도와 습도를 출력한다.
    # 온도는 소수점 첫째 자리까지 표시한다.
    label.config(text=f"{temp:.1f}C   {humi}%")

    # 60,000ms = 60초 = 1분 후 tick1Min 함수를 다시 실행한다.
    # 이를 통해 날씨 정보를 1분마다 자동 갱신한다.
    window.after(60000, tick1Min)


# Tkinter GUI 창 생성
window = tkinter.Tk()

# GUI 창 제목 설정
window.title("TEMP HUMI DISPLAY")

# GUI 창 크기 설정 (가로 400px, 세로 100px)
window.geometry("400x100")

# 창 크기 조절 불가능하도록 설정
window.resizable(False, False)

# GUI에 표시할 글자 크기 설정
font = tkinter.font.Font(size=30)

# 온도와 습도를 표시할 Label 위젯 생성
label = tkinter.Label(window, text="", font=font)

# Label 위젯을 창에 배치
label.pack()

# 프로그램 시작 시 즉시 날씨 데이터를 한 번 호출
tick1Min()

# GUI 창을 유지하고 사용자 이벤트를 처리하는 이벤트 루프 실행
window.mainloop()