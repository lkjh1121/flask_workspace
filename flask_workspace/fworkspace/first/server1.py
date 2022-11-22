from flask import Flask 

app = Flask(__name__) # Flask 객체를 생성한다 
                      #생성자에서 파일명을 받아간다 
                      #__name__ 를 매개변수로 전달해야 한다 

#데코레이터 - @ 함수나 클래스를 만들어서 다른 함수르 납치해와서 
#기능을 부여할 수 있다 

@app.route("/")  #라우트(경로배정) - 이문구가 지정된 함수는 라우터로 
                 #사용한다. 
def index():
    return "Hello, Flask"

if __name__ == "__main__":
    app.run('0.0.0.0', port=7000)  #서버 시작 
    #python server1.py 
    #0.0.0.0 - 현재 서버가 작동중인 컴푸터 아이피를 사용하라 