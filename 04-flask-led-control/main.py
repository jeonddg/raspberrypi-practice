from flask import Flask, render_template, request  # Flask 웹 서버, HTML 렌더링, 폼 데이터 처리
from gpiozero import LED                           # 라즈베리파이 GPIO LED 제어용 클래스

app = Flask(__name__)                             
# Flask 애플리케이션 객체 생성
# __name__은 현재 실행 중인 파이썬 파일 이름을 의미하며,
# Flask가 템플릿 폴더나 정적 파일의 위치를 찾을 때 사용된다.

red_led = LED(21)                                 
# GPIO 21번 핀에 연결된 LED 객체 생성
# 이후 red_led.on(), red_led.off()를 통해 LED를 켜고 끌 수 있다.


@app.route('/')                                   
def home():
    # 사용자가 웹 브라우저에서 기본 주소('/')로 접속했을 때 실행되는 함수
    # 예: http://라즈베리파이IP/
    
    return render_template("index.html")
    # templates 폴더 안에 있는 index.html 파일을 사용자에게 보여준다.
    # 즉, 웹 페이지의 기본 화면을 브라우저에 출력하는 역할을 한다.


@app.route('/data', methods=['POST'])             
def data():
    # 사용자가 웹 페이지에서 폼(form)을 제출했을 때 실행되는 함수
    # '/data' 주소로 POST 방식 요청이 들어오면 이 함수가 호출된다.

    data = request.form['led']
    # HTML form에서 name="led"인 입력값을 가져온다.
    # 예를 들어 버튼이나 입력값이 'on', 'off'라면 그 값을 읽어온다.

    if data == 'on':
        red_led.on()
        # 전달받은 값이 'on'이면 GPIO 21번 핀을 HIGH 상태로 만들어
        # 연결된 LED를 켠다.

    elif data == 'off':
        red_led.off()
        # 전달받은 값이 'off'이면 GPIO 21번 핀을 LOW 상태로 만들어
        # 연결된 LED를 끈다.

    return home()
    # LED 제어 후 다시 메인 페이지(index.html)를 보여준다.
    # 사용자는 LED 상태를 바꾼 뒤에도 같은 웹 화면으로 돌아오게 된다.


if __name__ == "__main__":
    # 현재 파일이 직접 실행된 경우에만 아래 코드를 수행한다.
    # 다른 파일에서 import된 경우에는 실행되지 않는다.

    app.run(host="0.0.0.0", port=80)
    # Flask 웹 서버 실행
    # host="0.0.0.0" → 같은 네트워크의 다른 장치에서도 접속 가능
    # port=80         → 기본 HTTP 포트로 웹 브라우저에서 접속 가능